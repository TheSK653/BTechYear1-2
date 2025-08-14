patient_database={}
name=input("Enter the patient name=> ")
b=input("Enter the retrieve patient information=> ")
c=input("enter the update patient medical history=>")
while True:
    choice=input("Patient Database Menu:\n\
1. Add new patient\n\
2. Retrieve patient information\n\
3. Update patient medical history\n\
4. Display all patients\n\
5. Exit\n\
enter your choice(1-5)")
    if choice=="1":
        name=input("Enter the patient name=> ")
        print("Patient added successfully.")
    elif choice=="2":
        print(b)
    elif choice=="3":
        print(c)
    elif choice=="4":
        print(name,b,c)
    elif choice=="5":
        print("existing the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")