from repository.student_repository import StudentRepository



class StudentService:
    def __init__(self):
        self.repo=StudentRepository()

    def save(self, student):
       self.repo.save(student)

    def edit(self, student):
       self.repo.edit(student)

    def remove(self, student_id):
        self.repo.remove(student_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, student_id):
        return self.repo.find_by_id(student_id)

    def find_by_name_and_family(self, name, family):
        return self.repo.find_by_name_and_family(name,family)

    def find_by_username_and_password(self, username, password):
        return self.repo.find_by_username_and_password(username, password)

    def find_duplicate_usernames(self, username):
        return self.repo.find_duplicate_usernames(username)



