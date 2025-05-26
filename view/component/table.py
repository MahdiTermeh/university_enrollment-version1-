from tkinter import ttk
from tkinter import *
class Table:
    def __init__(self,window,columns,width,x,y,height=10,function_name=NONE):
        self.function_name=function_name
        self.table = ttk.Treeview(window, columns=list(range(len(columns))),height=height ,show="headings")
        for i in range(len(columns)):
            self.table.heading(i, text=columns[i])
            self.table.column(i, width=width[i],anchor=CENTER)
        self.table.bind("<<TreeviewSelect>>", self.table_select)

        self.table.place(x=x, y=y)

    def table_select(self,event):
        row_id=self.table.focus()
        item=self.table.item(row_id)["values"]
        self.function_name(item)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
    def show_data(self,data_list):
        for data in data_list:
            self.table.insert("", END ,values=data)



# print(list(range(7)))
