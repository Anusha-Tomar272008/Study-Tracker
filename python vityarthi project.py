#STUDY TRACKER FOR FIRST SEMESTER CAT2 AT VIT 
#Module 1 SUBJECT TRACKER
print("WELCOME TO STUDY TRACKER FOR FIRST SEMESTER CAT2 AT VIT!")
x=input("Enter the subject you want to keep a track on(Enter all 4 subject wuth a gap in between):")
y=x.split()
print("You chose ",y)
a=y[0]
print("\n")
A=input("Did you complete "+a+"? (yes/no)")
if A.lower()=="yes":
    l=float(input("How many hours you studied it for:"))
    print("TIME SPENT ON "+a+":"+str(l)+ "HOURS")
    print("STATUS:COMPLETED")
    print("CONGRATULATIONS🎉!")
else:
    m=float(input("How many hours you studied it for:"))
    n=float(input("How much more time you think you would require more"))
    print("TIME SPENT ON "+a+":"+str(m)+ "HOURS")
    print("TIME MORE REQUIRED "+str(n)+ "HOURS")
    print("STATUS:PENDING🚫")
    print("DEADLINE:4 OCTOBER")      
b=y[1]
print("\n")
B=input("Did you complete "+b+"? (yes/no)")
if B.lower()=="yes":
    o=float(input("How many hours you studied it for"))
    print("TIME SPENT ON "+b+":"+str(o)+ "HOURS")
    print("STATUS:COMPLETED")
    print("CONGRATULATIONS🎉!")
else:
    p=float(input("How many hours you studied it for:"))
    q=float(input("How much more time you think you would require more"))
    print("TIME SPENT ON "+b+":"+str(p)+ "HOURS")
    print("TIME MORE REQUIRED "+str(q)+ "HOURS")
    print("STATUS:PENDING🚫")
    print("DEADLINE:4 OCTOBER")      
    

c=y[2]
print("\n")
C=input("Did you complete "+c+"? (yes/no)")
if C.lower()=="yes":
    r=float(input("How many hours you studied it for:"))
    print("TIME SPENT ON "+c+":"+str(r)+ "HOURS")
    print("STATUS:COMPLETED")
    print("CONGRATULATIONS🎉!")
else:
    s=float(input("How many hours you studied it for:"))
    t=float(input("How much more time you think you would require more"))
    print("TIME SPENT ON "+c+":"+str(s)+ "HOURS")
    print("TIME MORE REQUIRED "+str(t)+ "HOURS")
    print("STATUS:PENDING🚫")
    print("DEADLINE:4 OCTOBER")      
d=y[3]
print("\n")
D=input("Did you complete "+d+"? (yes/no)")
if D.lower()=="yes":
    u=float(input("How many hours you studied it for:"))
    print("TIME SPENT ON "+d+":"+str(u)+ "HOURS")
    print("STATUS:COMPLETED")
    print("CONGRATULATIONS🎉!")
else:
    v=float(input("How many hours you studied it for:"))
    w=float(input("How much more time you think you would require more:"))
    print("TIME SPENT ON "+d+":"+str(v)+ "HOURS")
    print("TIME MORE REQUIRED "+str(w)+ "HOURS")
    print("STATUS:PENDING🚫")
    print("DEADLINE:4 OCTOBER")      
    print("\n")
#Module 2 TASK TRACKER
print("WELCOME TO TASK TRACKER!")
print("\n")
tasks=[]
completed=[]
#Functional Module1: Add tasks
from add_tasks import add_tasks
#Functional Module2: Show tasks
from show_tasks import show_tasks
#Functional Module3: Completed Tasks
from completed_tasks import completed_tasks
#Functional Module4: Show Progress
from show_progress import show_progress
tasks=add_tasks(tasks)
show_tasks(tasks)
completed=completed_tasks(tasks,completed)

show_progress(tasks,completed)
#MODULE 3 STUDY SUMMARY
total_task=len(tasks)
comp_task=len(completed)
progress=(comp_task/total_task)*100

#MODULE 3 STUDY SUMMARY
print("YOUR PROGRESS PERCENTAGE IS = ",progress,"%")
if progress in range(90,101):
    print("\nQUOTE OF THE DAY: 90% of the friction is behind you. The remaining 10% is just execution👏🏻. ")
elif progress in range(80,91):
    print("\nQUOTE OF THE DAY: The last 20% of the effort yields 80% of the rewards🌟 ")
elif progress in range(70,81):
    print("\nQUOTE OF THE DAY: Most people quit when things get heavy, but you’ve already carried the weight this far🔥. ")
elif  progress in range(60,71):
    print("\nQUOTE OF THE DAY: It always seems impossible until it's done👌🏻. ")
elif progress in range(50,61):
    print("\n QUOTE OF THE DAY: Finishing more than half of your to-do list means the hardest part is officially behind you, and momentum is on your side👍🏻. ")
elif progress in range(40,51):
    print("\nQUOTE OF THE DAY:You are almost halfway there🎉!")
elif progress in range(30,41):
    print("\nQUOTE OF THE DAY: Keep moving forward💪🏻 ")
else:
    print("\nQUOTE OF THE DAY: It's time to lock in and keep your focus high✍. ")
    
    



    

    

    

    

