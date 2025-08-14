import numpy as np
l=[]
for i in range(10):
    l.append(int(input()))
arr=np.array(l)
print(arr[1:8])
print(arr.reshape(5,2))