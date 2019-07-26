import pickle
import os
import numpy as np

task_list = []

print("Tasks: ", end = "")

if os.path.exists("./task.pkl"):
    pickle_load = open("task.pkl","rb")
    task_list = pickle.load(pickle_load)
    task_list = task_list.tolist()
    for key in task_list:
        print(key, end = ", ")
        # task_list.append(key)

print("")

while True:
    x = input("Enter Task: ")
    x = str(x)
    if x == "":
        break
    if x == "delete" or x == "del" or x =="rm":
        index = input("Enter index to delete task: ")
        task_list.remove(index)
    else:
        task_list.append(x)

task_list = np.array(task_list)

pickle_save = open("task.pkl","wb")
pickle.dump(task_list, pickle_save)
pickle_save.close()

print("Tasks: ", end = "")
for key in task_list:
    print(key, end = ", ")

# print(task_list)