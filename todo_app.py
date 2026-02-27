print("TODO APP")
print()
task=["LEARN PYTHON LIST","BUILD A TODO APP"]
print(task)
print()
print("TASK WITH SERIAL NUMBER")
if task==[]:
    print("Task is empty")
for i in range(len(task)):
    print(i+1, task[i])
print()
add_task=input("Enter the task you want to add: ")
task.append(add_task)
print("TASK HAS BEEN ADDED")

print(task)
print()
if task==[]:
    print("Task is empty")
for i in range(len(task)):
    print(i+1, task[i])
print()
remove_option=int(input("Enter the serial number of the task you want to remove: "))
if remove_option>len(task) or remove_option<=0:
    print("Invalid serial number")
else:
    removed_task=task.pop(remove_option-1)
    print(f"Task '{removed_task}' has been removed")
print()
#BONUS

clear_list=str(input("if you want to clear the list, type 'clear': "))
if clear_list=="clear":
    task.clear()
    print("Task list has been cleared")