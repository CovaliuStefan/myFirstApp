from tkinter import *
from tkinter import font
from tkinter import colorchooser
from Task import *
from time import *


def update_time():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000,update_time)

window = Tk()
window.title("MyFirstApp")

#centrare window
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_for_window_width = int((screen_width / 2) - (window_width / 2))
position_for_window_height = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width,window_height,position_for_window_width,position_for_window_height))
window.config(bg="#666666")

#to do list
#menu


def drag_start(event):
    widget = event.widget
    widget.startX=event.x
    widget.startY=event.y
    if widget.winfo_x()<0 or widget.winfo_y()<0:
        widget.place(x=10,y=10)

def drag_motion(event):
    widget=event.widget
    x=widget.winfo_x() - widget.startX + event.x
    y=widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    if widget.winfo_x()<10 or widget.winfo_y()<10:
        widget.place(x=10,y=10)
    
def leave_Mouse(event):
    widget=event.widget
    widget.place(x=100,y=100)

def create_a_task(text,color):
    #task = Task(window,text,color,100,100)
    task=Label(window,text=text,bg=color)
    task.place(x=100,y=100)
    task.bind("<Button-1>",drag_start)
    task.bind("<B1-Motion>",drag_motion)
    #task.bind("<Leave>",leave_Mouse)

def add_a_task():

    def pick_color():
        color=colorchooser.askcolor(title="pick a color")
        text=entry.get()
        create_a_task(text,color[1])
        add_a_task_window.destroy()
        
    add_a_task_window = Toplevel()
    entry=Entry(add_a_task_window,font=("Arial",20))
    entry.pack()
    pick_acolor=Button(add_a_task_window,text="color",command=pick_color)
    pick_acolor.pack()
    
    

menubar = Menu(window)
window.config(menu=menubar)

task_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Tasks",menu=task_menu)
task_menu.add_command(label="Add a Task",command=add_a_task)



#orar


#clock
time_label=Label(window,fg="black",bg="white")
time_label.pack()
update_time()

window.mainloop()