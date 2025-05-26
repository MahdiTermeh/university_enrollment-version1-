import re
from datetime import date, datetime
from model.lesson import Lesson
from model.student import Student
from repository.student_repository import StudentRepository
repo=StudentRepository()



# Test Passed
# print(student_validator(student1))
def student_validator(student):
    errors = []
    if not type(student.name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", student.name):
        errors.append({"field": "name", "message": "invalid name"})

    if not type(student.family)== str or not re.match(r"^[a-zA-Z\s]{3,30}$", student.family):
        errors.append({"field": "family", "message": "invalid family"})

    # todo : unexpected error(when the input is not in YYYY-MM-DD format and is of type date)
    if not type(student.birth_date) == date or type(student.birth_date) == str:
        try:
            student.birth_date = datetime.strptime(student.birth_date, "%Y-%m-%d")
        except:
            errors.append({"field": "birth_date", "message": "invalid birth date"})
    else:
        errors.append({"field": "birth_date", "message": "invalid birth_date"})

    if  not re.match(r"^[a-zA-Z_\s\d]{3,30}$", student.username):
        errors.append({"field": "username", "message": "invalid username"})
    # todo:user has to change username everytime decides to edit a student
    if  repo.find_duplicate_usernames(student.username):
        errors.append({"field": "username", "message": "Username already exists"})

    if not re.match(r"^.{3,20}$", student.password):
        errors.append({"field": "password", "message": "invalid password"})



    return errors


def lesson_validator(lesson):
    errors = []
    if not type(lesson.title) == str or  not re.match(r"^[a-zA-Z\s\d]{3,30}$", lesson.title):
        errors.append({"field": "title", "message": "invalid title"})

    if not type(lesson.start_date) == date or type(lesson.start_date) == str:
        try:
            lesson.start_date = datetime.strptime(lesson.start_date, "%Y-%m-%d")
        except:
            errors.append({"field": "start_date", "message": "invalid start_date"})
    else:
        errors.append({"field": "start_date", "message": "invalid start date"})


    if not type(lesson.end_date) == date or type(lesson.end_date) == str:
        try:
            lesson.end_date = datetime.strptime(lesson.end_date, "%Y-%m-%d")
        except:
            errors.append({"field": "end_date", "message": "invalid end_date"})
    else:
        errors.append({"field": "end_date", "message": "invalid end_date"})


    if not type(lesson.professor) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", lesson.professor):
        errors.append({"field": "professor", "message": "invalid professor"})

    #todo the lines that have been commented don't work out properly

    # if not type (lesson.room_number) == int:
    #     errors.append({"field": "room_number", "message": "invalid room_number"})
    # if lesson.credit not in range(1,5):
    #     errors.append({"field": "credit", "message": "invalid credit"})
    #
    # if not type (lesson.capacity) == int:
    #     errors.append({"field": "capacity", "message": "invalid capacity"})



    return errors


def enrollment_validator(enrollment):
    errors=[]
    if not type(enrollment.student) == Student:
        errors.append({"field": "student", "message": "invalid student"})

    if not type(enrollment.lesson) == Lesson:
        errors.append({"field": "lesson", "message": "invalid lesson"})

    #todo:has error: enrollment_date validator doesn't work

    if not type(enrollment.enrollment_date) == date or type(enrollment.enrollment_date) == str:
        try:
            enrollment.enrollment_date = datetime.strptime(enrollment.enrollment_date, "%Y-%m-%d")
        except:
            errors.append({"field": "enrollment_date", "message": "invalid enrollment_date"})
    else:
        errors.append({"field": "enrollment_date", "message": "invalid enrollment_date"})
    return errors




