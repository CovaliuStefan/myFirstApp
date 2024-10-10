from tkinter import *
from tkinter import font
from tkinter import colorchooser
#from Task import *
from time import *
from new import *

def initialize_listbox():
    global tasks
    try:
        tasks = read()
        show_in_priority_order()
        for i in tasks:
            listbox.insert(listbox.size(),str(i["task_content"]))
    except:print("error")
    

def update_time():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000,update_time)

def update_listbox():
    listbox.delete(0,END)
    for i in tasks:
        listbox.insert(listbox.size(),str(i["task_content"]))


def delete_from_listbox():
    for index in reversed(listbox.curselection()):
        delete_task(listbox.get(index))
        listbox.delete(0,END)
        initialize_listbox()
    


def add_a_task_button():
    entry_task_content=entry_task.get()
    priority_task_scale=scale.get()
    if entry_task_content != "":
        new_task(entry_task_content,priority_task_scale,"random_date")
        show_in_priority_order()
        update_listbox()
        #listbox.insert(listbox.size(),entry_task_content)
        entry_task.delete(0,END)
    
window = Tk()
window.title("TO DO APP")

#centrare window
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_for_window_width = int((screen_width / 2) - (window_width / 2))
position_for_window_height = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width,window_height,position_for_window_width,position_for_window_height))
window.config(bg="#666666")


#clock
time_label=Label(window,fg="black",bg="white",font=("Arial",20))
time_label.pack()
update_time()

#lsitbox
listbox = Listbox(window,selectmode=MULTIPLE)
listbox.pack()

tasks=[]
initialize_listbox()


#add task frame
add_task_frame= Frame(window,bg="#666666")
add_task_frame.pack()

#add task button
add_button = Button(add_task_frame,text="Add task",command=add_a_task_button)
#add_button.pack(side=LEFT)

#delete from listbox button
delete_button = Button(add_task_frame,text="Delete tasks",command=delete_from_listbox)

#entry for task
entry_task_content=""
entry_task = Entry(add_task_frame,textvariable=entry_task_content)
#entry_task.pack(side=LEFT)


#scale
scale = Scale(add_task_frame,
                from_=1,
                to=10,
                orient=HORIZONTAL,
                tickinterval=1,
                bg="#666666")

delete_button.pack(side=RIGHT)
entry_task.pack(side=LEFT)
add_button.pack(side=RIGHT)
scale.pack(side=RIGHT)



window.mainloop()