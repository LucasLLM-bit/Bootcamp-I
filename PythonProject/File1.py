import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
window = ttk.Window(themename = 'darkly')
window.title('Milhas para Km')
window.geometry('500x500')

#title
title_label = ttk.Label(master = window, text = 'Milhas para kilometros', font = 'Calibri 28 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(
    master = input_frame,
    textvariable = entry_int)
button = ttk.Button(
    master = input_frame,
    text = 'Converter',
    command = convert)
entry.pack(side = 'left',
           padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                         font = 'Calibri 20 bold',
                         textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()