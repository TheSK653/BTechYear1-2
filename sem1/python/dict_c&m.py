n=int(input('No. of items =>'))
d={input('Key =>'):input('Value =>') for x in range(n)}
print('Enter:\t1 (enter new item)\n\t2 (update value)\n\t3 (delete item)\n\t4 (print dict)\n\tanything else to exit operation')
while True:
    task=int(input())
    if task==1:
        k=input('new key=>')
        v=input('new value=>')
        d[k]=v
    elif task==2:
        k=input('key=>')
        d[k]=input('new value=>')
    elif task==3:
        x=input('item to del')
        d.pop(x)
    elif task==4:
        print(d)
    else:
        print('Operation finished')
        break