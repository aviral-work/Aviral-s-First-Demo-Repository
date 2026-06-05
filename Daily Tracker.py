
print("Welcome to program for daily tasks management.")
name=input("Enter your name= ")
print("Hello",name)
age=int(input("Enter your age="))
date=int(input("Enter date of month= "))
print("For adding a task press 1.")
print("For changing a task press 2.")
print("List of daily tasks press 4.")
print("Know your profile press 5.")
choice=int(input("From 1 2 4 5"))
if choice==1:
    task=input("Enter task. /It is recommended to keep numbered tasks.")
    wt=len(task)
    while wt>0:
        task=input("Enter task. /It is recommended to keep numbered tasks.")
        s=open("Tasks.txt","w")
        s=s.write(str(task))
        task=input('Y/N to add another task.')
        if task=='N':
            wt=0
            print("Done from tasks recording for", date, "\n Go complete them.")
        else:
            continue
elif choice==2:
    print("To views tasks here:")
    s=open("Tasks.txt","r")
    s=s.read()
    s.close()
