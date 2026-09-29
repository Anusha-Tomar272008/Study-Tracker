def add_tasks(tasks):
    number=int(input("Enter the amount of tasks you want to add:"))
    for i in range(number):
        task=input("Enter your task:")
        tasks.append(task)
    return tasks
