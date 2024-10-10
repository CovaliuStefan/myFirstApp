from tkinter import Label


class Task:
    def __init__(self,window,text,bg,x,y):
        self.task = Label(window,text=text,bg=bg,fg="black")
        self.x=x
        self.y=y
        self.task.place(x=self.x,y=self.y)