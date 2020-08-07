# Python Programming Language
# User Interface

import tkinter

win = tkinter.Tk()
win.geometry("200x70")
win.title("First Window")


def exit_window():
    label["text"] = "Exit Winwow"
    button["text"] = "Wait..."
    button["state"] = "disabled"
    win.after(2000, win.destroy)


label = tkinter.Label(text="Hello Tkinter")
label.pack()

button = tkinter.Button(text="Exit",
                        command=exit_window)
button.pack()


win.protocol("WM_DELETE_WINDOW", exit_window)
win.mainloop()
