from controller.lesson_controller import LessonController
from model.lesson import Lesson
from repository.lesson_repository import LessonRepository
from service.lesson_service import LessonService

repo=LessonController()
lesson1=Lesson(1,"signal_system","2000-02-04",
        "2010-06-02","mesbah","736",3,5)
lesson2=Lesson(2,"python","2000-02-05","2010-06-02","mesbah","736",3,5)

repo.increase_lesson_capacity(1)
# print(repo.get_lesson_capacity(10))
#Test Passed
# print(lesson1)

#Test Passed
# print(repo.get_lesson_capacity(2))

#Test Passed
# repo.connect()
# repo.disconnect()

#Test Passed
# repo.save(lesson1)
# repo.save(lesson2)

#Test Passed
# repo.edit(lesson)

#Test Passed
# repo.remove(1)

#Test Passed
# print(repo.find_all())

#Test Passed
# print(repo.find_by_id(3))


#Test Passed
# print(repo.find_by_title_and_professor("p","m"))




