from tkinter import *

class LabelAndEntry:
    def __init__(self,window,text,x,y,variable_type=StringVar,distance=60,**kwargs):
        self.variable = variable_type(window)
        self.label=Label(window, text=text)
        self.label.place(x=x, y=y)
        self.entry=Entry(window, textvariable=self.variable,**kwargs)
        self.entry.place(x=x + distance, y=y)

    def get(self):
        return self.variable.get()

    def set(self,value):
        return self.variable.set(value)




