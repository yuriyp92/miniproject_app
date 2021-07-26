from settings import PAD_HEIGHT
from settings import WIDTH
from settings import HEIGHT
from settings import DARKGREY
from settings import BLACK
import pygame
from settings import *
from pygame import Vector2
from ball import Ball
from pad import Pad
from brick import Brick
from os import path

# El jugador controla una PALA que mueve en horizontal, con inercia
# Debe evitar que las bolas caigan por la parte inferior de la pantalla 
# Las bolas van rebotando por el espacio del juego contra los laterales,
# contra la pala del jugador y los ladrillos


class Game:
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        root_folder = path.dirname(__file__)
        sound_folder = path.join(root_folder, "sound")
        img_folder = path.join(root_folder, "img")
        self.load_images(img_folder)
        self.load_sounds(sound_folder)
    
    def load_images(self, img_folder):
        self.ball_image = pygame.image.load(path.join(img_folder, "ballBlue.png"))
        self.pad_image = pygame.image.load(path.join(img_folder, "paddleRed.png"))
        brick_colors = ["blue","green","grey","purple","red","yellow"]
        self.brick_images = []
        for color in brick_colors:
            filename = f'element_{color}_rectangle.png'
            img = pygame.image.load(path.join(img_folder, filename))
            self.brick_images.append(img)

    def load_sounds(self, sound_folder):
        self.bounce_fx = pygame.mixer.Sound(path.join(sound_folder, 'bounce.wav'))
        self.bounce_fx.set_volume(0.1)
        self.break_fx = pygame.mixer.Sound(path.join(sound_folder, 'break.wav'))
        self.break_fx.set_volume(0.1)

    def start(self):
        self.all_sprites = pygame.sprite.Group()    
        self.balls = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.pad = Pad(WIDTH//2, HEIGHT-PAD_HEIGHT*2, (self.all_sprites), self.pad_image)
        self.ball = self.create_ball_at(self.pad.rect.centerx, self.pad.rect.top - PAD_HEIGHT*2)
        self.brick_wall()
        self.lifes = 3
        self.run()
    
    def brick_wall(self):
        for x in range(10):
            for y in range(7):
                brick_x = BRICK_WIDTH + x * BRICK_WIDTH + x*5
                brick_y = BRICK_HEIGHT*2 + y * BRICK_HEIGHT + y*5
                Brick(brick_x, brick_y, (self.all_sprites, self.bricks), self.brick_images, self.break_fx)

    def run(self):
        self.playing = True
        while (self.playing):
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.K_SPACE:
                self.powerup_multiball()

       
    def create_ball_at(self,x,y):
        Ball(self.pad.rect.centerx,self.pad.rect.top-PAD_HEIGHT*2, (self.balls), self.ball_image, self.bounce_fx)
    
    def update(self):
        self.pad.update()
        self.balls.update(self.bricks, self.pad, self.ball_lost)
        hits = pygame.sprite.spritecollide(self.pad,self.balls,False)
        for ball in hits:
            self.pad.hit(ball)
    
    def powerup_multiball(self):
        for _ in range(5):
            reference_ball = self.balls.sprites()[0]
            ball = self.create_ball_atcreate_ball_at(reference_ball.rect.center)
            ball.asleep = False
            ball.velocity = Vector2(ball.velocity.x + random.uniform(-0.5, 0.5), reference_ball.velocity.y)
            

    def ball_lost(self):
        self.pad.velocity = 0
        self.lifes -= 1
        if self.lifes > 0:
            self.create_ball_at(self.pad.rect.centerx, self.pad.rect.top- PAD_HEIGHT*2)
        else:
            print('Game over')
            pass

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.balls.draw(self.screen)
        pygame.display.flip()
    

game = Game()
game.start()