import tkinter as tk

root=tk.Tk()
root.geometry('50x110')
root.title('hehe')

var=tk.IntVar(value=0)
def add():
    var.set(var.get()+1)
    c()
def sub():
    if var.get()!=0:
        var.set(var.get()-1)
    c()
def c():
    if var.get()<10:
        disp.config(fg='green')
    else:
        disp.config(fg='red')

disp=tk.Label(root,textvariable=var,font=('bold',30),fg='green')
disp.pack()
bt=tk.Button(root,text='+',command=add,font=('bold',20))
bt.pack(side=tk.RIGHT)
bt2=tk.Button(root,text='-',command=sub,font=('bold',20))
bt2.pack(side=tk.LEFT)

root.mainloop()