str=input()
k=int(input())
dict={}
for char in str:
    if char in dict.keys():
        dict[char]+=1
    else:
        dict[char]=1
result=''
for char in str:
    if dict[char]<k:
        result+=char
print(result)
print(dict)