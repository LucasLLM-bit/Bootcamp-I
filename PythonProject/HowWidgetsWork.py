import tkinter as tk
from tkinter import ttk

def button_func():
    #get content
    entry_text = entry.get()
    #update label
    label['text'] = entry_text
    entry['state'] = 'disabled'


#window
window = tk.Tk()
window.title('Getting and setting Widgets')
window.geometry('700x500')

#Widgets
label = ttk.Label(master = window, text = "Label 1", font = "Calibri 24 bold")
label.pack(pady = 10)

entry = ttk.Entry(master = window)
entry.pack(pady = 5)

button = ttk.Button(master = window,
                    text = "Button",
                    command = button_func)
button.pack(pady = 10)

#run
window.mainloop()

