from tkinter import *

from controller.student_controller import StudentController

import tkinter.messagebox as msg
from view.enrollment_view import EnrollmentView



class Login:

    def login(self):

        # student=self.repo.find_by_username_and_password(self.username.get(),self.password.get())
        _user=self.username.get()
        _pass=self.password.get()



        if _user!="root" and _pass !="root123":
            msg.showerror("Error","User is not the manager")
        else:
            self.win.destroy()
            ui=EnrollmentView()





    def __init__(self):
        self.repo=StudentController()

        self.win = Tk()
        self.win.title("Login Window")
        self.win.geometry("350x250")

        Label(self.win, text="Login",font=("Arial",15)).place(x=150, y=20)

        Label(self.win, text="Username").place(x=20 ,y=80 )
        self.username = StringVar(self.win)
        Entry(self.win, textvariable=self.username,width=50).place(x=20 ,y=100 )

        Label(self.win, text="Password").place(x=20, y=120)
        self.password = StringVar(self.win)
        Entry(self.win, textvariable=self.password, width=50).place(x=20, y=140)

        Button(self.win,text="Login",width=42,fg="gray99",bg="Blue2",command=self.login).place(x=20,y=165)

        self.win.mainloop()




