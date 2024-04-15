from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

class First(Screen):
    pass
class Second(Screen):
    pass


class Manager(ScreenManager):
    pass
class screen(App):
    def build(self):
        
        pass

screen().run()