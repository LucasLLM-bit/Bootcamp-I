import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def button_hi():
    print('hell0')

#creat a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('900x900')

#ttk widgets
label = ttk.Label(master = window, text = 'Isso é um teste')
label.pack(pady = 10)

#create widgets
text = tk.Text(master = window)
text.pack(pady = 20)

#ttk entry
entry = ttk.Entry(master = window,)
entry.pack()

#hello button
button_h = ttk.Button(master = window, text = 'diga hello', command = button_hi)
button_h.pack(pady = 5)

#my label
my_label = ttk.Label(master = window, text = 'My label')
my_label.pack(pady = 5)

#ttk button
button = ttk.Button(master = window, text = 'Butão', command = button_func)
button.pack(pady = 5)


#run
window.mainloop()
print('App closed')
