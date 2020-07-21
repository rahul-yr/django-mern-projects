

# Button Widget
def button_widget(ttk,space,input_text,function_name,col,row):
    button_event = ttk.Button(space,text=input_text,command=function_name)
    button_event.grid(column=col,row=row)
    return button_event

# Input Widget
def input_widget(tk,ttk,space,width,col,row):
    fields = tk.StringVar()
    input_box = ttk.Entry(space,width=width,textvariable=fields)
    input_box.grid(column =col,row=row)
    return input_box

# Label Widget
def label_widget(ttk,space,label_text,col,row):
    label_event= ttk.Label(space,text=label_text)
    label_event.grid(column=col,row=row)
    return label_event

# Label Frame
def label_frame_widget(ttk,space,label_text,col,row):
    label_event= ttk.LabelFrame(space,text=label_text)
    label_event.grid(column=col,row=row)
    return label_event

# Combo Box
def combo_box_for_model(tk,ttk,space,width,col,row,drop_down_values):
    number = tk.StringVar()
    inputComboBox = ttk.Combobox(space,width=width,textvariable=number)
    inputComboBox['values']=drop_down_values
    inputComboBox.current(0)
    inputComboBox.grid(column = col,row=row)
    return inputComboBox