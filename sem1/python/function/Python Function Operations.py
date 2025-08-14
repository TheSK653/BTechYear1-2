def input_(str):
    in_put=(input(str))
    try :
        int(in_put)
        return in_put
    except ValueError:
        print('Input is not a number.')
    return 0
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_palindrome(number):
    return str(number) == str(number)[::-1]
while True:
    print("\nFunction Menu:\n\
1. Check Leap Year\n\
2. Calculate Factorial\n\
3. Check Prime Number\n\
4. Check Palindrome\n\
5. Exit")
    choice = input_("Enter your choice (1-5): ")
    if choice == '1':
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    elif choice == '2':
        num = int(input("Enter a number to calculate factorial: "))
        print(f"The factorial of {num} is: {factorial(num)}")
    elif choice == '3':
        num = int(input("Enter a number to check for prime: "))
        if is_prime(num):
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is not a Prime Number.")
    elif choice == '4':
        number = int(input("Enter a number to check for palindrome: "))
        if is_palindrome(number):
            print(f"{number} is a Palindrome.")
        else:
            print(f"{number} is not a Palindrome.")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.",choice)