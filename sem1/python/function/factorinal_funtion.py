def cal_fun(x):
    if x==1 or x==0:
        return 1
    else:
        return x*cal_fun(x-1)

input=int(input())
print(cal_fun(input))