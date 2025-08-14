import tkinter as tk

class Counter:
    def __init__(self,win) -> None:
        self.win = win
        win.geometry('100x100')
        win.title('Counter')
        self.var = tk.IntVar(value=0)
        self.disp=tk.Label(root, textvariable=self.var, font=('bold', 30))
        self.disp.pack()
        tk.Button(win, text='⬆️', command=self.inc).pack(side=tk.LEFT)
        tk.Button(win, text='⬇️', command=self.dec).pack(side=tk.RIGHT)

    def inc(self):
        self.var.set(self.var.get()+1)
        
    def dec(self):
        self.var.set(self.var.get()-1)

root=tk.Tk()
exc=Counter(root)

root.mainloop()