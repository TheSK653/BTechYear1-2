db={}
print("1. Add new student\n\
2. Display student details\n\
3. Display average marks\n\
4. Display percentage of all students\n\
5. Display grade of a specific student\n\
6. Exit")
while True:
    i=int(input("\nEnter your choice: "))
    print()
    if i==1:
        name=input("Enter student name: ")
        roll=int(input("Enter roll number: "))
        s1=int(input("Enter marks in Subject 1: "))
        s2=int(input("Enter marks in Subject 2: "))
        s3=int(input("Enter marks in Subject 3: "))
        db[roll]=[name,s1,s2,s3]
    if i==2:
        print("roll no., name, subject 1, subject 2, subject 3")
        for k in db:
            print(k,db[k])
    if i==3:
        avg1,avg2,avg3=0,0,0
        l=len(db)
        for k in db:
            avg1+=db[k][1]
            avg2+=db[k][2]
            avg3+=db[k][3]
        print(f"Average Marks:\n\
Subject 1: {avg1/l}\n\
Subject 2: {avg2/l}\n\
Subject 3: {avg3/l}")
    if i==4:
        per=0
        print("Percentage of Students:")
        for k in db:
            per=sum(db[k][1:])/3
            print(f"{db[k][0]} (Roll Number {k}): {per}%")
    if i==5:
        req=int(input("Enter roll number of the student: "))
        per=sum(db[req][1:])/3
        if per>=90:
            g="A+"
        elif per>=80:
            g="A"
        elif per>=70:
            g="B"
        elif per>=60:
            g="C"
        elif per>=50:
            g="D"
        elif per>=40:
            g="E"
        else:
            g="F"
        print(f"\nGrade of Student:\n\
Name: {db[req][0]}\n\
Roll Number: {req}\n\
Percentage: {per}%\n\
Grade: {g}")
    if i==6:
        break