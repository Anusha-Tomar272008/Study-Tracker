def show_progress(tasks,completed):
    print("\nCONGRATULATIONS TASK COMPLETED!")

    print("\nCOMPLETED TASKS:")
    for task in completed:
        print("-",task)
    print("\nTotal completed:",len(completed))
    pending=len(tasks)-len(completed)
    print("Total pending",pending)

    if pending==0:
        print("CONGRATULATIONS! YOU COMPLETED ALL THE TASKS🎉")
        print("HAVE FUN NOW!")
    else:
        print("KEEP GOING!YOU ARE DOING GREAT!💪🏻")
