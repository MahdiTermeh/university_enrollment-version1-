from repository.enrollment_repository import EnrollmentRepository
from repository.lesson_repository import LessonRepository


class EnrollmentService:
    def __init__(self):
        self.repo=EnrollmentRepository()
        self.lesson_repo=LessonRepository()

    def map_enrollment(self, enrollment_tuple):
        return self.repo.map_enrollment(enrollment_tuple)

    def enroll_student_in_course(self, enrollment):
        course_enrollment_count=self.repo.get_course_enrollment_count(enrollment.student.id, enrollment.lesson.id)
        if course_enrollment_count > 0:
            raise Exception("The lesson has already been taken")
        capacity_count=self.lesson_repo.get_lesson_capacity(enrollment.lesson.id)
        if capacity_count==0:
            raise Exception("Cannot enroll:lesson capacity has been reached")

        if self.repo.get_remaining_credits(enrollment.student.id) < enrollment.lesson.credit:
            raise Exception("Cannot enroll:credit limit of 17 has been exceeded")

        self.repo.enroll_student_in_course(enrollment)

    def delete_enrollment(self, lesson_id, student_id):
        course_enrollment_count=self.repo.get_course_enrollment_count(student_id,lesson_id)
        if course_enrollment_count > 1:
            raise Exception("Unexpected error:duplicate course enrollments found")
        if course_enrollment_count == 0:
            raise Exception("Student has not enrolled in this course")


        self.repo.delete_enrollment(lesson_id, student_id)



    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, book_id):
        return self.find_by_id(book_id)

    def find_enrolled_courses_by_student_id(self, student_id):
        return self.repo.find_enrolled_courses_by_student_id(student_id)

    def find_by_lesson_id(self, lesson_id):
        return self.repo.find_by_lesson_id(lesson_id)

    def find_by_username_and_title(self, username, title):
        return self.repo.find_by_username_and_title(username, title)

    def get_total_credits(self, student_id):
        return self.repo.get_total_credits(student_id)

    def get_course_enrollment_count(self, student_id, lesson_id):
        return self.repo.get_course_enrollment_count(student_id, lesson_id)

    def get_remaining_credits(self, student_id):
        return self.repo.get_remaining_credits(student_id)






