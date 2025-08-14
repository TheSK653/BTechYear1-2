import time
import threading

def f(t):
    time.sleep(t)

t=int(input('Enter the delay time (in seconds): '))

tt=threading.Thread(target=f,args=[t])
tt.start()

print('Timer started...')

f(t)

print('Timer expired!')