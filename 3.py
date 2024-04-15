from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

Window.clearcolor=(1,1,1)

class MyImageApp(App):
    def build(self):
        layout = BoxLayout()
        i = Image(source="C:\\Users\\shukl\\OneDrive\\Pictures\\wallpaper\\1337368.png", size_hint=(0.13, 0.134), pos_hint={"center_x": 0.3, "center_y": 0.7})
        m = AsyncImage(source="https://imgs.search.brave.com/ggW4-wpo0xucpDwGm57mPa8eMTL6VhW2BIc-RGWZEFc/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9nZWVr/eWJ5dGVzLm5ldC93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyMi8w/OS9Hb2pvLXBmcC0y/MS5qcGVn", size_hint=(0.13, 0.134), pos_hint={"center_x": 0.3, "center_y": 0.4})
        layout.add_widget(i)
        layout.add_widget(m)
        return layout

MyImageApp().run()
