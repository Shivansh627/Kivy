from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor=('#1E90FF')

Window.clearcolor=(0.3,0.25,0.34)

class Firstapp(App):
    def build(self):
        btn=Button(text="click me",size_hint=(0.2,0.1),pos_hint={"center_x":0.3,"center_y":0.7},color=(0.1,0.9,0))
        return btn
    
Firstapp().run()