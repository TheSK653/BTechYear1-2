import tkinter as tk

class ToDoList:
    def __init__(self, win) -> None:
        self.win = win
        win.title('To-Do list')
        self.lst = []
        self.entry = tk.Entry(win)
        self.entry.grid(row=0,column=0)

        tk.Button(win, text = 'Add', command=self.AddItem).grid(row=0,column=1)

        self.listBox = tk.Listbox(win)
        self.listBox.grid(row=1,column=0,columnspan=2)
        
        tk.Button(win, text = 'del', command=self.DelItem).grid(row=2,column=0)

        tk.Button(win, text = 'del all', command=self.DelAll).grid(row=2,column=1)
        tk.Button(win, text = 'undo', command=self.undo).grid(row=3,column=0,columnspan=2)

    def AddItem(self):
        # self.backup()
        self.lst.append((-2, tk.END))
        self.listBox.insert(tk.END, self.entry.get())
        self.entry.delete(0, tk.END)

    def DelItem(self):
        # self.backup()
        index = self.listBox.curselection()
        ele = self.listBox.get(index)
        self.listBox.delete(index)
        self.lst.append((index, ele))

    def DelAll(self):
        # self.backup()
        self.lst.append((-1, self.listBox.get(0,tk.END)))
        self.listBox.delete(0,tk.END)

    def undo(self):
        if self.lst:
            index, ele = self.lst.pop()
            if index==-1:
                for item in ele:
                    self.listBox.insert(tk.END, item)
            elif index==-2:
                self.listBox.delete(ele)
            else:
                self.listBox.insert(index, ele)
        # self.listBox.delete(0,tk.END)
        # for item in self.listBoxBackup:
        #     self.listBox.insert(tk.END, item)

    def backup(self):
        self.listBoxBackup=self.listBox.get(0,tk.END)

if __name__ == '__main__':
    root=tk.Tk()
    exc=ToDoList(root)
    root.mainloop()