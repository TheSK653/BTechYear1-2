#  Problem Statement: Finding Common Even and Odd Elements

#                 Write a Python program that takes input from the user for two lists and finds the common even and odd elements 
#                 between them. The program should follow these steps:

#                 Define a function "find_common_even_odd_elements" that takes two lists as parameters.
#                 Inside the function, use sets and list comprehensions to find and return two lists:

#                     - List containing the common even elements.
#                     - List containing the common odd elements.
                
#                 Take input from the user for the elements of the first and second lists.
#                 Call the find_common_even_odd_elements function with the user-input lists.
#                 Display the common even and odd elements between the two lists.
                
#                 Example:
#                     Enter elements of the first list separated by spaces: 1 2 3 4 5 6
#                     Enter elements of the second list separated by spaces: 3 4 5 6 7 8
#                     Common even elements: [4, 6]
#                     Common odd elements: [3, 5]

def find_common_even_odd_elements(l1,l2):
    t=list(set(l1).intersection(set(l2)))
    even=[x for x in t if x%2==0]
    odd=[x for x in t if x%2!=0]
    print(even,odd)

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
find_common_even_odd_elements(l1,l2)