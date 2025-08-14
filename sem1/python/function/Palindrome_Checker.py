def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")