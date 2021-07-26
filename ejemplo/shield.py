from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

class ShieldMain(FloatLayout):
    def cifra(self, s, clave=3):
        buff = []
        for c in s:
            num = ord(c)
            if 65 <= num < 91:
                new_num = ((num - 65 + clave) % 26) + 65
                buff.append(str(chr(new_num)))
            elif 97 <= num < 123:
                new_num = ((num - 97 + clave) % 26) + 97
                buff.append(str(chr(new_num)))
            else:
                buff.append(c)
        
        self.ids.texto_cifrado.text = ''.join(buff)
        
    def intercambiar(self, sin_cifrar, cifrado):
        new_sin_cifrar = sin_cifrar
        self.ids.texto_cifrar.text = cifrado
        self.ids.texto_cifrado.text = new_sin_cifrar 


class ShieldApp(App):
    pass


def main():
    app = ShieldApp()
    app.run()


if __name__ == '_main_':
    main()