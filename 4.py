from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor="#ffccff"
Window.size=(300,200)

class Input(App):
    def build(self):
        layout=GridLayout(rows=4,spacing=20,padding=50)
        self.e=TextInput(text="Enter Email",size_hint=(None,None),width=170,height=30,font_size=12)
        self.p=TextInput(text="Enter Password",size_hint=(None,None),width=170,height=30,font_size=12)
        self.f=TextInput(text="Enter first number",size_hint=(None,None),width=170,height=30,font_size=12)
        self.s=TextInput(text="Enter second number",size_hint=(None,None),width=170,height=30,font_size=12)
        self.sm=TextInput(text="sum is:",size_hint=(None,None),width=170,height=30,font_size=12)
        self.b=Button(text="submit",on_release=self.get,size_hint=(None,None),width=170,height=30,font_size=12)
    
        layout.add_widget(self.e)
        layout.add_widget(self.p)
        layout.add_widget(self.f)
        layout.add_widget(self.s)
        layout.add_widget(self.sm)
        layout.add_widget(self.b)
        return layout
    
    def get(self,obj):
        print("your email is :",self.e.text)
        print("your password is :",self.p.text)
        sum=int(self.f.text) + int(self.s.text)
        self.sm.text=str(sum)

    
Input().run()