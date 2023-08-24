import tkinter as tk 
from tkinter import ttk

'''window=tk.Tk()
window.title('playground')
first_frame=ttk.Frame()
my_label=ttk.Label(first_frame,text='first label')
my_entry_var=tk.StringVar(value='')
my_entry=ttk.Entry(first_frame,textvariable=my_entry_var)
my_button=ttk.Button(first_frame,text='first button')
my_button.pack(side=tk.LEFT)
my_label.pack(side=tk.RIGHT,expand=True)
my_entry.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)
first_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
window.mainloop()'''

window=tk.Tk()
first_frame=tk.Frame(window)

ttk.Label(first_frame, text='grid 1').grid(row=0,column=0)
ttk.Label(first_frame, text='grid 2').grid(row=0, column=1)
ttk.Label(first_frame,text= 'grid 3').grid(row=1,column=0)
ttk.Label(first_frame, text='grid 4').grid(row=1,column=1)

first_frame.pack()
window.mainloop()

