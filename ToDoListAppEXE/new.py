import json
from os import write
#from Task import Task
from datetime import datetime

#task creator
class New_task():
    def __init__(self,task_content,task_priority,expiration_date):
        self.task_content=task_content
        self.task_priority=task_priority
        self.expiration_date=expiration_date

    def addTask(self):
        now = datetime.now()
        tasks.append(
            {
            "task_content":self.task_content,
            "task_priority":self.task_priority,
            "expiration_date":self.expiration_date,
            "creation_date":now.strftime("%d/%m/%Y-%H:%M:%S")
            }
        )
        #print(tasks)

#global task list
tasks=[]

#read from json file
def read():
    global tasks
    with open('tasks.json','r') as json_file:
        json_object = json.load(json_file)
    #print(json_object)
    tasks=json_object
    return tasks


#write in json file
def writeTask():
    with open('tasks.json', 'w') as fp:
        json.dump(tasks, fp,indent=3)

#create a task
def new_task(task_content,task_priority,expiration_date):  
    New_task(task_content,task_priority,expiration_date).addTask()
    writeTask()

#delete a task
def delete_task(data):
    global tasks
    for i in range(len(tasks)):
        if tasks[i]["task_content"].startswith(data):
            del tasks[i]
            break
    writeTask()
    #print(tasks)

#show in priority order
def show_in_priority_order():
    priorities = lambda priority:priority["task_priority"]
    tasks.sort(key=priorities)
    if __name__=='__main__':
        for i in tasks:
            print(i["task_content"]+" : "+str(i["task_priority"]))


if __name__=='__main__':
    read()
    #print(tasks[1])
    show_in_priority_order()
    #new_task("sport",4,"never")
    #new_task("info",6,"today")
    delete_task("so")
    #writeTask()





