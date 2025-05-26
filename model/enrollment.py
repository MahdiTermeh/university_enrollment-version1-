from datetime import date
class Enrollment:
    def __init__(self,id,lesson,student,enrollment_date=date.today()):
        self.id=id
        self.lesson=lesson
        self.student=student
        self.enrollment_date=enrollment_date

    def __repr__(self):
        return f"{self.__dict__}"