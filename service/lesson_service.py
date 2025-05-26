import mysql.connector

from repository.lesson_repository import LessonRepository


class LessonService:
    def __init__(self):
        self.repo=LessonRepository()

    def save(self,lesson):
        self.repo.save(lesson)
    def edit(self,lesson):
        self.repo.edit(lesson)
    def remove(self,lesson_id):
        self.repo.remove(lesson_id)
    def find_all(self):
        return self.repo.find_all()
    def find_by_id(self,lesson_id):
        return self.repo.find_by_id(lesson_id)

    def find_by_title_and_professor(self, title, professor):
        return self.repo.find_by_title_and_professor(title, professor)

    def get_lesson_capacity(self,lesson_id):
        return self.repo.get_lesson_capacity(lesson_id)

    def decrease_lesson_capacity(self, lesson_id):
        #todo:(optional) we can check if capacity is greater than 0 to prevent negative values
        self.repo.decrease_lesson_capacity(lesson_id)

    def increase_lesson_capacity(self, lesson_id):
        self.repo.increase_lesson_capacity(lesson_id)
