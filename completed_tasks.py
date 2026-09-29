def completed_tasks(tasks,completed):
    while True:
        choice=int(input("\nWhich task did you complete?Enter the task number: "))

        completed_task=tasks[choice-1]
        completed.append(completed_task)

        again=input("Do you have more completed tasks? (yes/no):")
        if again.lower()=="no":
            break
    return completed
