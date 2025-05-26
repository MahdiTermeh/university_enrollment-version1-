from tkinter import *
from PIL import Image, ImageTk
from view.About_me import AboutMe
from view.lesson_view import LessonView
from view.login import Login
from view.student_view import StudentView


class HomePage:

    def run_login(self):
        ui=Login()
    def run_student_view(self):
        ui = StudentView()

    def run_lesson_view(self):
        ui = LessonView()

    def run_about_me(self):
        ui=AboutMe()
    def __init__(self):
        self.win = Tk()
        self.win.title("Homepage")
        self.win.geometry("400x400")

        self.lesson_icon = Image.open("images\\book2.png")
        self.lesson_icon = self.lesson_icon.resize((32, 32))
        self.lesson_icon = ImageTk.PhotoImage(self.lesson_icon)

        self.student_icon = Image.open("images\\student2.jpeg")
        self.student_icon = self.student_icon.resize((32, 32))
        self.student_icon = ImageTk.PhotoImage(self.student_icon)

        Button(self.win, text="Enrollment" , font=("Arial",13),command=self.run_login).place(x=90,y=20,width=200,height=70)
        Button(self.win, text="Student", image=self.student_icon, compound="left", font=("Arial", 13),
               command=self.run_student_view).place(x=90, y=120, width=200, height=70)

        Button(self.win, text="Lesson", image=self.lesson_icon, compound="left", font=("Arial", 13),
               command=self.run_lesson_view).place(x=90, y=220, width=200, height=70)

        Button(self.win, text="About me",font=("Arial",13),command=self.run_about_me).place(x=90,y=320,width=200,height=70)





        self.win.mainloop()