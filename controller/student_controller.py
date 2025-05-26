from model.student import Student
from service.student_service import StudentService
from validation.validator import student_validator


class StudentController:
    def __init__(self):
        self.service=StudentService()

    def save(self,name,family,birth_date,username,password):
        try:
            student=Student(None,name,family,birth_date,username, password)
            errors=student_validator(student)
            if errors:
                raise Exception(errors)

            self.service.save(student)
            return True,"Student Saved"
        except Exception as e:
            return False,f"Error:{e}"

    def edit(self,id,name,family,birth_date,username,password):
        try:
            student=Student(id,name,family,birth_date,username, password)
            errors=student_validator(student)
            if errors:
                raise Exception(errors)

            self.service.edit(student)
            return True,"Student Edited"
        except Exception as e:
            return False,f"Error:{e}"

    def remove(self,student_id):
        try:
            self.service.remove(student_id)
            return True,"Student Removed"
        except Exception as e:
            return False,f"Error:{e}"

    def find_all(self):
        try:
            return self.service.find_all()
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_id(self,student_id):
        try:
            return self.service.find_by_id(student_id)
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_name_and_family(self, name, family):
        try:
            return self.service.find_by_name_and_family(name,family)
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_username_and_password(self, username, password):
        try:
            return self.service.find_by_username_and_password(username,password)
        except Exception as e:
            return False,f"Error:{e}"


    def find_duplicate_usernames(self, username):
        try:
            return self.service.find_duplicate_usernames(username)
        except Exception as e:
            return False,f"Error:{e}"


