from model.enrollment import Enrollment
from model.lesson import Lesson
from model.student import Student
from repository.enrollment_repository import EnrollmentRepository
from service.enrollment_service import EnrollmentRepository, EnrollmentService

# for en in repo.find_all():
#     student2=Student(*en[4:10])
#     lesson2=Lesson(*en[10:])
#     enrollment=Enrollment(en[0],lesson2,student2,en[3])
#     print(enrollment)

# repo1=EnrollmentRepository()
#Test Passed
# print(repo1.get_course_enrollment_count(1,10))

#Test Passed
# print(repo.get_remaining_credits(4))

#Test Passed
# print(repo.find_all())

#Test Passed
# print(repo.find_by_lesson_id(1))

#Test Passed
# print(repo.find_by_student_id(4))

#Test Passed
# print(repo.find_by_username_and_title("mohsen","cshrp"))

#Test Passed
# repo.enroll_student_in_course(course_selection)

#Test Passed
# print(course_selection)

#Test Passed
# repo.connect()
# repo.disconnect()

# Test Passed
# print(repo.get_remaining_credits(1))
repo=EnrollmentService()
lesson1=Lesson(4,"cshrp","2025-05-12","2025-05-27","mohseni",123,3,4

)
lesson2=Lesson(6,"parto","2025-05-02","2025-05-15","moghadasi",234,17,2



)




student1=Student(4,"mohsen","akbari","2025-05-12","mohsen","mohsen123"


)
student3=Student(3,"sohrab","sabaii","2000-01-10","mahidh","sdkkh"
)
course_selection=Enrollment(None,lesson1,student1,
        "2000-06-02")
# repo.delete_enrollment(2,1)
# print(repo.find_enrolled_courses_by_student_id(4))


print(repo.get_total_credits(10))
print(repo.get_remaining_credits(10))
