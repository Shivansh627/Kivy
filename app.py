from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ExpenseTracker(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expenses = []
        self.total_expenses = 0
        self.layout = BoxLayout(orientation='vertical')
        self.expense_desc_input = TextInput(hint_text='Expense Description')
        self.expense_amount_input = TextInput(hint_text='Expense Amount')
        self.add_expense_button = Button(text='Add Expense')
        self.add_expense_button.bind(on_press=self.add_expense)
        self.total_expenses_label = Label(text=f'Total Expenses: {self.total_expenses}')
        self.layout.add_widget(self.expense_desc_input)
        self.layout.add_widget(self.expense_amount_input)
        self.layout.add_widget(self.add_expense_button)
        self.layout.add_widget(self.total_expenses_label)

    def build(self):
        return self.layout

    def add_expense(self, instance):
        desc = self.expense_desc_input.text
        amount = float(self.expense_amount_input.text)
        self.expenses.append({'description': desc, 'amount': amount})
        self.total_expenses += amount
        self.total_expenses_label.text = f'Total Expenses: {self.total_expenses}'
        self.expense_desc_input.text = ''
        self.expense_amount_input.text = ''

if __name__ == '__main__':
    ExpenseTracker().run()
