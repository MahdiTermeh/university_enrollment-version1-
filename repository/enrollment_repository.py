import mysql.connector

from model.enrollment import Enrollment
from model.lesson import Lesson
from model.student import Student



class EnrollmentRepository:
    def connect(self):
        self.connection=mysql.connector.connect(
            user="root",
            password="root123",
            port=3306,
            database="university",
            host="localhost"

        )
        self.cursor=self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        self.cursor.close()

    def map_enrollment(self,enrollment_tuple):
        student = Student(*enrollment_tuple[4:10])
        lesson = Lesson(*enrollment_tuple[10:])
        enrollment = Enrollment(enrollment_tuple[0], lesson, student, enrollment_tuple[3])
        return enrollment


    def enroll_student_in_course(self, enrollment):
        self.connect()
        self.cursor.execute("insert into university.enrollment (student_id, lesson_id, enrollment_date) VALUES (%s, %s, %s)",
                            [enrollment.student.id, enrollment.lesson.id, enrollment.enrollment_date])
        self.connection.commit()
        self.disconnect()


    def find_all(self):
        self.connect()
        self.cursor.execute("select * from enrollment_report")
        enrollment_list = list(map(self.map_enrollment,self.cursor.fetchall()))

        self.disconnect()
        return enrollment_list

    def find_by_id(self, book_id):
        self.connect()
        self.cursor.execute()
        enrollment = self.cursor.fetchone()
        self.disconnect()
        return enrollment

    def find_enrolled_courses_by_student_id(self,student_id):
        self.connect()
        self.cursor.execute("""select l_id, title, start_date, end_date,
         professor, room_number, credit, capacity
         from enrollment_report
         where s_id =%s;""",
        [student_id])
        lesson_list = self.cursor.fetchall()
        self.disconnect()
        return lesson_list

    def find_by_lesson_id(self, lesson_id):
        self.connect()
        self.cursor.execute("select * from university.enrollment_report where lesson_id = %s",[lesson_id])
        enrollment_list = list(map(self.map_enrollment,self.cursor.fetchall()))
        self.disconnect()
        return enrollment_list

    def find_by_username_and_title (self,username, title):
        self.connect()
        self.cursor.execute("select * from enrollment_report where username=%s and title=%s",
                            [username,title])
        enrollment=self.map_enrollment(self.cursor.fetchone())
        self.disconnect()
        return enrollment

    def get_total_credits(self,student_id):
        self.connect()
        self.cursor.execute("select sum(credit) from enrollment_report where s_id =%s",
                            [student_id])
        total_credit = self.cursor.fetchone()[0]
        self.disconnect()
        return total_credit if total_credit is not None else 0

    def get_course_enrollment_count(self,student_id,lesson_id):
        self.connect()
        self.cursor.execute("select count(*) from enrollment_report where s_id=%s and l_id=%s",
                            [student_id,lesson_id])
        total_count = self.cursor.fetchone()[0]
        self.disconnect()
        return total_count


    def get_remaining_credits(self,student_id):
        return 17 - self.get_total_credits(student_id)

    def delete_enrollment(self,lesson_id,student_id):
        self.connect()
        self.cursor.execute("""delete from enrollment where lesson_id=%s and student_id=%s""",
                            [lesson_id,student_id])
        self.connection.commit()
        self.disconnect()


    # def find_non_returned (self):
    #     self.connect()
    #     self.cursor.execute()
    #     enrollment_list = self.cursor.fetchall()
    #     self.disconnect()
    #     return enrollment_list
