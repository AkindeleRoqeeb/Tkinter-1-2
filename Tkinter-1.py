import tkinter

window = tkinter.Tk()

window.title("Abdul @ life.com", )

window.minsize(width=500, height=300)
my_label = tkinter.Label(text="My Text", font=("Arial", 24, "bold"))
my_label.pack()

# my_label["text"] = "Text Area"
my_label.config(text="Text New")

message = tkinter.Label(text="This is my first tkinter,\n all together i will be add and removing\n as well as creating new once......", font=("Arial",34, "bold"))
message.pack()


window.mainloop()