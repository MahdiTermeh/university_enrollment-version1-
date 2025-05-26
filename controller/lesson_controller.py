from model.lesson import Lesson
from service.lesson_service import LessonService
from validation.validator import lesson_validator


class LessonController:
    def __init__(self):
        self.service=LessonService()

    def save(self,title,start_date,end_date,professor,room_number,credit,capacity):
        try:
            lesson=Lesson(None,title,start_date,end_date,professor,room_number,credit,capacity)
            errors=lesson_validator(lesson)
            if errors:
                raise Exception(errors)

            self.service.save(lesson)
            return True,"Lesson Saved"
        except Exception as e:
            return False,f"Error:{e}"

    def edit(self,id,title,start_date,end_date,professor,room_number,credit,capacity):
        try:
            lesson=Lesson(id,title,start_date,end_date,professor,room_number,credit,capacity)
            errors=lesson_validator(lesson)
            if errors:
                raise Exception(errors)

            self.service.edit(lesson)
            return True,"Lesson Edited"
        except Exception as e:
            return False,f"Error:{e}"

    def remove(self,lesson_id):
        try:
            self.service.remove(lesson_id)
            return True,"Lesson Removed"
        except Exception as e:
            return False,f"Error:{e}"

    def find_all(self):
        try:
            return self.service.find_all()
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_id(self,lesson_id):
        try:
            return self.service.find_by_id(lesson_id)
        except Exception as e:
            return False,f"Error:{e}"

    def find_by_title_and_professor(self, title, professor):
        try:
            return self.service.find_by_title_and_professor(title,professor)
        except Exception as e:
            return False,f"Error:{e}"


    def get_lesson_capacity(self, lesson_id):
        try:
            return self.service.get_lesson_capacity(lesson_id)
        except Exception as e:
            return False,f"Error:{e}"


    def decrease_lesson_capacity(self, lesson_id):
        try:
            self.service.decrease_lesson_capacity(lesson_id)
        except Exception as e:
            return False,f"Error:{e}"

    def increase_lesson_capacity(self, lesson_id):
        try:
            self.service.increase_lesson_capacity(lesson_id)
        except Exception as e:
            return False,f"Error:{e}"


