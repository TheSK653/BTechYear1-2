# Problem Statement: Student Grades Management with List Comprehension

#     You are tasked with developing a Python program to manage the grades of students in a class. 
#     The program should perform the following tasks:

#     Define a function "calculate_average" that takes a list of grades as input and returns the average grade.

#     Define a function "highest_grade_student" that takes a dictionary of student names and their corresponding grades and 
#     returns the name of the student with the highest grade.

#     Take input from the user for the number of students.

#     For each student, take input for their name and grades.
#     Store the information in a dictionary where the keys are student names, and values are lists of their grades.

#     Calculate and display the average grade for each student.

#     Identify and display the student with the highest grade.

#     IMPLEMENT LIST COMPREHENSION WHEREEVER YOU CAN!

#     Example:
#         Enter the number of students: 3

#         Enter the name of student 1: Alice
#         Enter the grades of Alice separated by spaces: 85 90 88
        
#         Enter the name of student 2: Bob
#         Enter the grades of Bob separated by spaces: 78 92 89
        
#         Enter the name of student 3: Charlie
#         Enter the grades of Charlie separated by spaces: 92 95 91
        
#         Average grades for each student:
#         Alice: 87.67
#         Bob: 86.33
#         Charlie: 92.67
        
#         Student with the highest grade: Charlie  


def calculate_average(grades):
    return sum(grades)/len(grades)
# print(calculate_average([1,2,3,4,5]))

def highest_grade_student(dict):
    # return dict.get(max(dict.values()))
    for key,val in dict.items():
        if val==max(dict.values()):
            return key
# print(highest_grade_student(dict({"a":2,"c":6,"b":100})))

user  = int(input("Enter the number of students: "))
dict = {}
for  i in range(user):
    name=input(f"\nEnter the name of student {i+1}: ")
    grades=list(map(int,input(f"Enter the grades of {name} separated by spaces: ").split()))
    dict[name]=grades

print("\nAverage grades for each student:")
for name in list(dict.keys()):
    print(f"{name}: {calculate_average(dict[name]):.2f}")

print(f"\nStudent with the highest grade: {highest_grade_student(dict)}")