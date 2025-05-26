from controller.student_controller import StudentController
from service.student_service import StudentService
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from tkinter import *
from model.student import Student
import tkinter.messagebox as msg
class StudentView:
    def save_click(self):
        status,message=self.controller.save(self.name.get(),
                        self.family.get(),self.birth_date.get(),
                        self.username.get(),self.password.get())

        if status:
            msg.showinfo("Saved", message)
            self.reset_form()

        else:
            msg.showerror("Error",message)





    def edit_click(self):
        status, message = self.controller.edit(
        self.id.get(),self.name.get(),
        self.family.get(), self.birth_date.get(),
        self.username.get(), self.password.get())

        if status:
            msg.showinfo("Saved", message)
            self.reset_form()

        else:
            msg.showerror("Error", message)

    def remove_click(self):

        status, message = self.controller.remove(self.id.get())
        if status:
            msg.showinfo("Removed", message)
            self.reset_form()

        else:
            msg.showerror("Error", message)


    def reset_form(self):
        self.table.clear_table()
        self.table.show_data(self.controller.find_all())
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")
        self.username.set("")
        self.password.set("")

    def select_table(self,selected_row):
        student=Student(*selected_row)
        self.id.set(student.id)
        self.name.set(student.name)
        self.family.set(student.family)
        self.birth_date.set(student.birth_date)
        self.username.set(student.username)
        self.password.set(student.password)


    def __init__(self):
        self.controller=StudentController()

        self.win=Tk()
        self.win.geometry("720x300")
        self.win.title("Student")

        self.id=LabelAndEntry(self.win,"Id",20,20,IntVar,70)
        self.name=LabelAndEntry(self.win,"Name",20,61,StringVar,70)
        self.family=LabelAndEntry(self.win,"Family",20,102,StringVar,70)
        self.birth_date=LabelAndEntry(self.win,"Birth_Date",20,143,StringVar,70)
        self.username=LabelAndEntry(self.win,"Username",20,184,StringVar,70)
        self.password=LabelAndEntry(self.win,"Password",20,225,StringVar,70)

        Button(self.win,text="Save",width=7,command=self.save_click).place(x=20,y=261)
        Button(self.win,text="Edit",width=7,command=self.edit_click).place(x=88,y=261)
        Button(self.win,text="Remove",width=7,command=self.remove_click).place(x=156,y=261)
        self.table=Table(self.win,
                    ["Id","Name","Family","Birth_date","Username"],
                    [60,100,100,100,100],240,20,12,self.select_table)

        self.reset_form()

        self.win.mainloop()
