import tkinter as tk
from tkinter import messagebox as mb

class MassagePopUp:
    def __init__(self, win) -> None:
        self.win = win
        win.geometry('200x100')

        tk.Label(win,text='Enter Celsios Temperature:').pack()

        self.entry = tk.Entry(win)
        self.entry.pack()

        self.bt1 = tk.Button(win, text = 'Pop', command=self.action)
        self.bt1.pack()

    def action(self):
        C=float(self.entry.get())
        mb.showinfo('Greating', f'{C} degrees Celsius is equal to\n{C*9/5+32} degrees Fahrenhiet')

if __name__ == '__main__':
    root=tk.Tk()
    exc=MassagePopUp(root)
    root.mainloop()