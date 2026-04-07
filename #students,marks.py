#students,marks 


s=[]

n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter name of student= ")
    marks=int(input("Enter marks= "))
    s.append((name,marks))

for i in s:
    print(i)

order=sorted(s,key=lambda x:x[1],reverse=True)
print("Sorted list of students based on marks: ")

for i in order:
    print(i)
