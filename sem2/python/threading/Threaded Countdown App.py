import time
import threading
def f1(t):
    for i in range(10,0,-2):
        print(i)
        time.sleep(t)
def f2(t):
    time.sleep(.5)
    for i in range(9,0,-2):
        print(i)
        time.sleep(t)
t1=threading.Thread(target=f1,args=[1])
t2=threading.Thread(target=f2,args=[1])
t1.start()
t2.start()