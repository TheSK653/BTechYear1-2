import tkinter as tk

root=tk.Tk()
root.geometry('200x100')
root.title('Greeting App')

def action():
    disp.config(text='hello, '+entry.get())
    entry.delete(0, tk.END)

tk.Label(root, text='Type your name', font=('bold')).pack()

entry=tk.Entry(root)
entry.pack()

tk.Button(root, text='Enter', command=action).pack()

disp=tk.Label(text='')
disp.pack()

root.mainloop()