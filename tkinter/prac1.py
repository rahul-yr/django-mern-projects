import tkinter  as tk
from tkinter import ttk
from sys import argv,exit


if argv[1:]:
    file_name= argv[1]
    file_name2= argv[2]
    with open(file_name) as file:
        f = file.read()
else:
    print('Please enter file name at start of the program')
    exit(0)

win = tk.Tk()
win.title('Python Copy GUI')
win.resizable(0,0)

aLabel = ttk.Label(win , text = 'File names are {} and {} '.format(file_name,file_name2))
aLabel.grid(column = 0,row= 0)

def Copy():
    f2 = open(file_name2,'w')
    f2.write(f)
    # action.configure(f2.write(f))
    aLabel.configure(foreground='red')
    f2.close()
    exit(0)

action = ttk.Button(win,text = 'Copy files data',command=Copy)
action.grid(column =1,row = 0)




win.mainloop()