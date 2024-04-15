from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor=('#1E90FF')


class Firstapp(App):
    def build(self):
        k=Label(text="Shivansh",font_size="40",pos_hint={"center_x":0.1,"center_y":0.9})
        # btn=Button(text="click me",size_hint=(0.1,0.3),pos_hint={"center_x":0.2,"center_y":0.7})
        return k
    
Firstapp().run()