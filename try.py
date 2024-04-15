from tkinter import *

root = Tk()
root.title("Menu Example")

def hello():
    print("Hello!")

menu = Menu(root)
root.config(menu=menu)

app_men=Menu(root)
app_men.add_command(label="shivansh")
app_men.add_command(label="shukla")
menu.add_cascade(label="shivansh",menu=app_men)

option=["shivansh","shukla"]

var=StringVar()
var.set(option[0])

op=OptionMenu(root,var,*option).pack()

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=hello)
file_menu.add_command(label="Open", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)

root.mainloop()
