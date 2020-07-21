import tkinter  as tk
from tkinter import ttk
from sys import argv,exit

win = tk.Tk()
win.title('Python GUI')
win.resizable(0,0)

alabel = ttk.Label(win,text='A Label')
alabel.grid(column=0,row=0)
# ttk.Label(win,text='Another Label').grid(column = 0,row =1)

def click_me():
    action.configure(text='I have clicked')
    alabel.configure(foreground='red')
    # action.configure


action = ttk.Button(win,text='Click Me',command=click_me)
action.grid(column =1,row=0)








win.mainloop()




# 0-----------------------------

# def generateFields():
#     count = int(fieldsCount.get())
#     # Fields Label Creator Space
#     addFieldSpace = ttk.LabelFrame(modelframe,text='Add Fields Creator')
#     addFieldSpace.grid(column =0,row=2)
#     for i in range(count):
#         # Input Fields
#         # fieldsName =fields+i
#         fieldsName= str(tk.StringVar())
#         fieldsCountInputBox = ttk.Entry(addFieldSpace,width=12,textvariable=fieldsName)
#         fieldsCountInputBox.grid(column = 0,row =i)
#         listOfFields.append(fieldsCountInputBox)


# Model Label Code Generator Label Frame
# modelspace = ttk.LabelFrame(win,text='Model Creator')
# modelspace.grid(column =0,row=0)

# Fields Label Creator Space
# fieldSpace = ttk.LabelFrame(modelspace,text='Fields Creator')
# fieldSpace.grid(column =0,row=0)



# # Label
# nofields = ttk.Label(fieldSpace,text='Add Number of Fields')
# nofields.grid(column=0,row=0)


# # Input Fields
# fieldsCount = tk.StringVar()
# fieldsCountInputBox = ttk.Entry(fieldSpace,width=12,textvariable=fieldsCount)
# fieldsCountInputBox.grid(column = 1,row =0)

# # Button
# generateNofields = ttk.Button(fieldSpace,text='Generate Fields',command=generateFields)
# generateNofields.grid(column=2,row=0)

# # Button
# generateNofields = ttk.Button(fieldSpace,text='Copy Fields',command=copyFields)
# generateNofields.grid(column=3,row=0)