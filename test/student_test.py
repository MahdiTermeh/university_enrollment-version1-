from datetime import datetime, date

from controller.student_controller import StudentController
from model.student import Student
from repository.student_repository import StudentRepository
from service.student_service import StudentService

# repo=StudentRepository()
# student1=Student(2,"ahmmmmad","mozafari",
#         "1800-02-02","jlsjaj","jfkdl",)
# student2=Student(3,"mohammad","mozafari",
#         "1800-02-02","jlsjaj","jfkdl",)
student_controller=StudentController()
student_service=StudentService()
student_repo=StudentRepository()
# print(student_controller.save("omid","safaii","2000-01-01","om_s","omid123"))


# print(repo.find_by_username_and_password("mohsen","mohsen123"))

student_repo.remove(1)
#Test Passed
# print(student)

#Test Passed
# repo.connect()
# repo.disconnect()

#Test Passed
# repo.save(student1)
# repo.save(student2)

#Test Passed
# repo.edit(student)

#Test Passed
# repo.remove(1)

#Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(22))

# Test Passed
# print(repo.find_by_name_and_family("m","mo"))

# Test Passed

# Test passed
# print(repo.username_checker("jlsjaj"))


# if not type(student1) == Student:
#         print("khata")
# else:
#         print("dorost")

