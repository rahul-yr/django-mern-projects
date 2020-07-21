import tkinter as tk
from tkinter import ttk


def add_model_name():
    displayModelName.configure(text = inputModelName.get()+' - '+number.get())
    displayModelName.configure(foreground='green',background='yellow')


win = tk.Tk()
win.title('Input GUI')
win.resizable(0,0)

modelName = ttk.Label(win,text = 'Enter Model Name')
modelName.grid(column = 0,row =0)

displayModelName = ttk.Label(win,text = '')
displayModelName.grid(column = 1,row =0)


inputModelName = tk.StringVar()
inputTextBox = ttk.Entry(win,width=12, textvariable=inputModelName)
inputTextBox.grid(column = 0,row=1)


inputModelButton = ttk.Button(win,text = 'Add Name & Category',command = add_model_name)
inputModelButton.grid(column =1,row =1)


n2Label = ttk.Label(win,text = 'Choose a Category Id')
n2Label.grid(column = 0,row =2)

# Combo Box
number = tk.StringVar()
inputComboBox = ttk.Combobox(win,width=12, textvariable=number)
inputComboBox['values']=(5,10,15,20,25,30,35,40,45,50)
inputComboBox.current(0)
inputComboBox.grid(column = 1,row=2)


win.mainloop()