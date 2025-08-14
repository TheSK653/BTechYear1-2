import tkinter as tk

class Counter:
    def __init__(self,win) -> None:
        self.win = win
        win.geometry('200x100')
        win.title('Reverser')
        self.entry=tk.Entry(win)
        self.entry.pack()
        tk.Button(root, text='reverse', command=self.action).pack()

    def action(self):
        x=self.entry.get()[::-1]
        self.entry.delete(0,tk.END)
        self.entry.insert(0,x)

root=tk.Tk()
exc=Counter(root)

root.mainloop()