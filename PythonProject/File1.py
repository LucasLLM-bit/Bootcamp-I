import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Teste')
window.geometry('500x500')

#title
title_label = ttk.Label(master = window, text = 'Milhas para kilometros', font = 'Calibri 28 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Converter')
entry.pack()
button.pack()
input_frame.pack()

#run
window.mainloop()