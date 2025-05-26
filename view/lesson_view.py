from controller.lesson_controller import LessonController
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from tkinter import *
from model.lesson import Lesson
import tkinter.messagebox as msg
class LessonView:
    def save_click(self):
        #todo:despite controller module the programm crashes when get input of type string in room_number,credit and capacity entry
        status,message=self.controller.save(self.title.get(),
        self.start_date.get(),self.end_date.get(),
        self.professor.get(),self.room_number.get(),self.credit.get(),self.capacity.get())

        if status:
            msg.showinfo("Saved", message)
            self.reset_form()
        else:
            msg.showerror("Error",message)



    def edit_click(self):
        status,message = self.controller.edit(self.id.get(), self.title.get(),
                          self.start_date.get(), self.end_date.get(),
                          self.professor.get(), self.room_number.get(),self.credit.get(),self.capacity.get())
        if status:
            msg.showinfo("Edited", message)
            self.reset_form()
        else:
            msg.showerror("Error",message)
    def remove_click(self):
        status, message = self.controller.remove(self.id.get())
        if status:
            msg.showinfo("Deleted", message)
            self.reset_form()
        else:
            msg.showerror("Deleted", message)
    def reset_form(self):
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())
        self.id.set(0)
        self.title.set("")
        self.start_date.set("")
        self.end_date.set("")
        self.professor.set("")
        self.room_number.set(0)
        self.credit.set(0)
        self.capacity.set(0)


    def select_table(self,selected_row):
        lesson=Lesson(*selected_row)
        self.id.set(lesson.id)
        self.title.set(lesson.title)
        self.start_date.set(lesson.start_date)
        self.end_date.set(lesson.end_date)
        self.professor.set(lesson.professor)
        self.room_number.set(lesson.room_number)
        self.credit.set(lesson.credit)
        self.capacity.set(lesson.capacity)


    def __init__(self):
        self.controller=LessonController()

        self.win=Tk()
        self.win.geometry("935x385")
        self.win.title("Lesson")


        self.id=LabelAndEntry(self.win,"Id",20,20,IntVar,80,state="readonly")
        self.title=LabelAndEntry(self.win,"Title",20,61,StringVar,80)
        self.start_date=LabelAndEntry(self.win,"StartDate",20,102,StringVar,80)
        self.end_date=LabelAndEntry(self.win,"EndDate",20,143,StringVar,80)
        self.professor=LabelAndEntry(self.win,"Professor",20,184,StringVar,80)
        self.room_number=LabelAndEntry(self.win,"RoomNumber",20,225,IntVar,80)
        self.credit=LabelAndEntry(self.win,"Credit",20,266,IntVar,80)
        self.capacity=LabelAndEntry(self.win,"Capacity",20,307,IntVar,80)



        Button(self.win,text="Save",width=7,command=self.save_click).place(x=20,y=343)
        Button(self.win,text="Edit",width=7,command=self.edit_click).place(x=93,y=343)
        Button(self.win,text="Remove",width=7,command=self.remove_click).place(x=166,y=343)
        self.table=Table(self.win,
                    ["Id","Title","StartDate","EndDate","Professor","RoomNumber","Credit","Capacity"],
                    [60,100,100,100,100,100,60,60],240,20,14,self.select_table)

        self.reset_form()

        self.win.mainloop()
