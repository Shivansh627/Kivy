from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size=(400,600)


class Calculator(App):
    def cal(self, instance):
        current = self.text.text
        button_text = instance.text

        if button_text == 'C':
            self.text.text = ''
        elif button_text == '=':
            try:
                self.text.text = str(eval(current))
            except Exception as e:
                self.text.text = 'Error'
        elif button_text in self.operations:
            if self.last_was_operator:
                return
            self.text.text += button_text
            self.last_was_operator = True
        else:
            if self.text.text == 'Error':
                self.text.text = ''
            self.text.text += button_text
            self.last_was_operator = False

    def build(self):
        self.layout=GridLayout(rows=2)
        self.operations = ['+', '-', '*', '/']
        self.text=TextInput(multiline=False,size_hint=(None,None),width="400sp")
        self.layout.add_widget(self.text)
        # self.but()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        self.grd= GridLayout(rows=4,cols=4)
        for b in buttons:
            self.button=Button(text=b,on_press=self.cal)

            self.grd.add_widget(self.button)
        self.layout.add_widget(self.grd)
        # self.layout.add_widget(self.but())

        return self.layout
    
    

Calculator().run()