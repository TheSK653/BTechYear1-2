import tkinter as tk
from tkinter import messagebox as mb

class MassagePopUp:
    def __init__(self, win) -> None:
        self.win = win
        win.geometry('200x100')

        self.entry = tk.Entry(win)
        self.entry.pack()

        self.bt1 = tk.Button(win, text = 'Pop', command=self.action)
        self.bt1.pack()

        tk.Button(win, text='Exit', command=self.exit).pack()

    def action(self):
        mb.showinfo('Greating', self.entry.get())

    def exit(self):
        self.win.destroy()

if __name__ == '__main__':
    root=tk.Tk()
    exc=MassagePopUp(root)
    root.mainloop()