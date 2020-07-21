import tkinter as tk
from tkinter import ttk
from helper.widget_helper import button_widget,input_widget,label_widget,label_frame_widget,combo_box_for_model
from helper.constants import input_fields_for_model
from helper.helper_functions import generateRandomVariable

listOfFields = []

def generateFields():
    count = int(input_fields_count.get())

    for i in range(count):
        li =[]
        li.append(input_widget(tk,ttk,dynamic_fields_frame,12,0,i))
        li.append(combo_box_for_model(tk,ttk,dynamic_fields_frame,15,5,i,input_fields_for_model))
        li.append(input_widget(tk,ttk,dynamic_fields_frame,30,10,i))

        listOfFields.append(li)


def copyFields():
    show=''
    for i in range(len(listOfFields)):
        show=show+'{} = models.{}({})\n'.format(listOfFields[i][0].get(),listOfFields[i][1].get(),listOfFields[i][2].get())
    label_widget(ttk,dynamic_fields_frame,show,15,0)


win = tk.Tk() 
win.title("Code Generator")

# create a frame for model
modelframe = label_frame_widget(ttk,win,'Model Frame',0,0)
# Setup Frame
setup_frame = label_frame_widget(ttk,win,'Setup Frame',0,2)

# Input Fields Frame In Setup Frame
dynamic_fields_frame = label_frame_widget(ttk,setup_frame,'Input Fields Frame',0,2)


label_widget(ttk,setup_frame,'Model Name',0,0)

model_name = input_widget(tk,ttk,setup_frame,12,1,0)


label1 = label_widget(ttk,setup_frame,'Add Number of Fields',2,0)

input_fields_count = input_widget(tk,ttk,setup_frame,12,3,0)

button_widget(ttk,setup_frame,'Generate Fields',generateFields,4,0)

button_widget(ttk,setup_frame,'Copy Fields',copyFields,5,0)



win.mainloop()