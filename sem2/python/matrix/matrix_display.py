class array:

    def __init__(self,ls):
        self.ls=ls

    def validity(self,m,n):
        return len(self.ls)==m*n
    
    def create_matrix(self,m,n):
        self.M=[]
        x,y=0,n
        z=y
        for r in range(m):
            self.M.append(self.ls[x:y])
            x,y=y,y+z

    def display_matrix(self):
        for i in self.M:
            print(*i,sep='\t')

lst=list(map(int,input().split()))
row,column=list(map(int,input().split()))

arr=array(lst)
if arr.validity(row,column):
    arr.create_matrix(row,column)
    arr.display_matrix()
else:
    print('invalid Dimension')

# class array:
#     def _init_(self,ls):
#         self.ls=ls
#     def validity(self,m,n):
#         return len(self.ls)==m*n
#     def create_matrix(self,m,n):
#         self.M=[]
#         tmp=[]
#         count=0
#         for i in self.ls:
#             tmp.append(i)
#             count+=1
#             if count==n:
#                 self.M.append(tmp)
#                 tmp=[]
#                 count=0
#     def display_matrix(self):
#         for i in self.M:
#             print(*i,sep=' ')

# ls=list(map(int,input().split()))
# row,column=list(map(int,input().split()))

# arr=array(ls)
# if arr.validity(row,column):
#     arr.create_matrix(row,column)
#     arr.display_matrix()

# else:
#     print('invalid Dimension')