############################ Button ################

from tkinter import *

window = Tk()

window.title("Abdul @ life.com", )

window.minsize(width=500, height=300)
my_label = Label(text="My Text", font=("Arial", 24, "bold"))
my_label.pack()

# my_label["text"] = "Text Area"
my_label.config(text="Text New")

# Button
def button_click():
    print("Am clicked")

button = Button(text="Click Me", command=button_click, fg="red", bg="black", width=50)
button.pack()

window.mainloop()