import numpy as np
arr=np.random.randint(0,20,20)
print(arr)
arr.sort()
print(arr)
arr=arr.reshape((4,5))
print(arr)
print(arr.reshape(2,10))