from tkinter import *
import tkinter.messagebox as msg
from controller.enrollment_controller import EnrollmentController
from controller.lesson_controller import LessonController
from controller.student_controller import StudentController
from model.lesson import Lesson
from view.component.table import Table

from model.student import Student



class EnrollmentView:
    def reset_student_form(self):
        self.student_table.clear_table()
        self.student_table.show_data(self.student_controller.find_all())


    def reset_lesson_form(self):
        self.lesson_table.clear_table()
        self.lesson_table.show_data(self.lesson_controller.find_all())

    def update_selected_courses_table(self,student_id):
        self.selected_courses_table.clear_table()
        self.selected_courses_table.show_data(self.enrollment_controller.find_enrolled_courses_by_student_id(student_id))

    def update_credits_display(self):
        self.taken = self.enrollment_controller.get_total_credits(self.student.id)
        self.taken_label = Label(self.win, text=f"Taken Credits: {self.taken}/17") #todo:sometimes the number 17 is displayed with a small extra 7
        self.taken_label.place(x=815, y=350)

    def select_student(self, selected_row):
        self.student = Student(*self.student_controller.find_by_id(selected_row[0]))
        self.update_credits_display()



        self.update_selected_courses_table(self.student.id)


    def select_lesson(self, selected_row):
        self.lesson = Lesson(*self.lesson_controller.find_by_id(selected_row[0]))

    def select_selected_courses(self,selected_row):
        self.my_lesson = Lesson(*self.lesson_controller.find_by_id(selected_row[0]))

    def save_enrollment(self):
        status,message=self.enrollment_controller.enroll_student_in_course(self.lesson,self.student)
        if status:
            msg.showinfo("Enrollment", message)
            self.lesson_controller.decrease_lesson_capacity(self.lesson.id)
            self.update_selected_courses_table(self.student.id)
            self.reset_lesson_form()
            self.update_credits_display()
        else:
            msg.showerror("Error",message)

    def delete_enrollment(self):
        status,message=self.enrollment_controller.delete_enrollment(self.my_lesson.id ,self.student.id)
        if status:
            msg.showinfo("Enrollment", message)
            self.lesson_controller.increase_lesson_capacity(self.my_lesson.id)
            self.update_selected_courses_table(self.student.id)
            self.reset_lesson_form()
            self.update_credits_display()

        else:
            msg.showerror("Error", message)



    def __init__(self):
        self.student_controller = StudentController()
        self.lesson_controller = LessonController()
        self.enrollment_controller = EnrollmentController()
        self.student = None
        self.lesson = None


        self.win = Tk()
        self.win.geometry("1366x768")
        self.win.title("Enrollment View")


        Label(self.win, text="Student List").place(x=15, y=20)

        self.student_table = Table(
            self.win,
            ["Id", "Name", "Family"],

            [30, 100, 100],
            15, 40,
            14,
            self.select_student # y=40
        )


        Label(self.win, text="Course List").place(x=265, y=20)
        self.lesson_table = Table(self.win,
                           ["Id", "Title", "StartDate", "EndDate", "Professor", "RoomNumber", "Credit", "Capacity"],
                           [30, 60, 70, 70, 100, 100, 45, 55], 265, 40, 14, self.select_lesson) # y=40


        Label(self.win, text="Selected Courses").place(x=815, y=20)
        self.selected_courses_table = Table(self.win,
                                  ["Id", "Title", "StartDate", "EndDate", "Professor", "RoomNumber", "Credit",
                                   "Capacity"],
                                  [30, 60, 70, 70, 100, 100, 45, 55], 815, 40, 14,self.select_selected_courses)  # y=40




        Button(self.win, text="Enrollment", width=15, command=self.save_enrollment).place(x=465, y=370)
        Button(self.win, text="Delete", width=15, command=self.delete_enrollment).place(x=1030, y=370)

        self.reset_student_form()
        self.reset_lesson_form()


        self.win.mainloop()
