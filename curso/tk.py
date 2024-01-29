import tkinter as tk

ws = tk.Tk()

nameLb = tk.Label(ws, text="Enter Name", foreground='yellow', background='black', width=30, height=10)
entry = tk.Entry()
nameLb.pack()
entry.pack()
name = entry.get()
print(name)

bt = tk.Button(ws,text="Click me!",command='OK')
bt.pack()
ws.mainloop()