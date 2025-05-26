from model.enrollment import Enrollment
from service.enrollment_service import EnrollmentService
from validation.validator import enrollment_validator


class EnrollmentController:
    def __init__(self):
        self.service=EnrollmentService()

    def map_enrollment(self,enrollment_tuple):
        try:
            return self.service.map_enrollment(enrollment_tuple)
        except Exception as e:
            return False,f"Error:{e}"

    def enroll_student_in_course(self, lesson,student):
        try:
            enrollment=Enrollment(None,lesson,student)
            #todo: the validation part was commented because it doesn't work properly

            # errors=enrollment_validator(enrollment)
            # if errors:
            #     raise Exception(errors)

            self.service.enroll_student_in_course(enrollment)

            return True, "Enrollment Saved successfully"
        except Exception as e:
            return False,f"Error:{e}"

    def delete_enrollment(self, lesson_id, student_id):
        try:
            self.service.delete_enrollment(lesson_id, student_id)
            return True, "Enrollment Deleted successfully"
        except Exception as e:
            return False, f"Error:{e}"

    def find_all(self):
        try:
            return self.service.find_all()
        except Exception as e:
            return False, f"Error:{e}"

    def find_by_id(self, book_id):
        try:
            return self.service.find_by_id(book_id)
        except Exception as e:
            return False, f"Error:{e}"

    def find_enrolled_courses_by_student_id(self, student_id):
        try:
            return self.service.find_enrolled_courses_by_student_id(student_id)
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_lesson_id(self, lesson_id):
        try:
            return self.service.find_by_lesson_id(lesson_id)
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_username_and_title(self, username, title):
        try:
            return self.service.find_by_username_and_title(username, title)
        except Exception as e:
            return False,f"Error:{e}"

    def get_total_credits(self, student_id):
        try:
            return self.service.get_total_credits(student_id)
        except Exception as e:
            return False,f"Error:{e}"

    def get_course_enrollment_count(self, student_id, lesson_id):
        try:
            return self.service.get_course_enrollment_count(student_id,lesson_id)
        except Exception as e:
            return False,f"Error:{e}"

    def get_remaining_credits(self, student_id):
        try:
            return self.service.get_remaining_credits(student_id)
        except Exception as e:
            return False,f"Error:{e}"