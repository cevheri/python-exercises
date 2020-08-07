# Python Programming Language
# User Interface

import tkinter


class MainWindow(tkinter.Tk): # is-a relationship
    def __init__(self):
        super().__init__()
        # window
        self.geometry("200x70")
        self.title("First Window")
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

        # label
        # has-a relationship
        self.label = tkinter.Label(text="Hello Tkinter") #
        self.label.pack()

        # button
        # has-a relationship
        self.button = tkinter.Button(text="Exit", command=self.exit_window)
        self.button.pack()

    def exit_window(self):
        self.label["text"] = "Exit Winwow"
        self.button["text"] = "Wait..."
        self.button["state"] = "disabled"
        self.after(2000, self.destroy)


win = MainWindow()
win.mainloop()
