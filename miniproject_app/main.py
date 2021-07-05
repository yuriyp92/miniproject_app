from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

class Controles(FloatLayout):

    label_text = StringProperty("SHIELD DECO")
    counter = 0

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
        return ''.join(buff)
    
class ControlesApp(App):
    pass

def main():
    app = ControlesApp()
    app.run()


if __name__ == '__main__':
    main()