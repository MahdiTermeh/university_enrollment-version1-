import mysql.connector

from model.student import Student


class StudentRepository:
    def connect(self):
        self.connection=mysql.connector.connect(
            user="root",
            password="root123",
            port=3306,
            database="university",
            host="localhost"

        )
        self.cursor=self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        self.cursor.close()

    def save(self,student):
        self.connect()
        self.cursor.execute("""insert into university.students
         (name,family,birth_date,username,password) values (%s,%s,%s,%s,%s) """
        ,[student.name,student.family,student.birth_date,student.username,student.password])
        self.connection.commit()
        self.disconnect()
    def edit(self,student):
        self.connect()
        self.cursor.execute("""
        update university.students set name=%s,family=%s,birth_date=%s,
        username=%s,password=%s where s_id=%s
        """,[student.name,student.family,student.birth_date,student.username,student.password,student.id])
        self.connection.commit()
        self.disconnect()
    def remove(self,student_id):
        self.connect()
        self.cursor.execute(""" delete from university.students where s_id=%s""",
                            [student_id])
        self.connection.commit()
        self.disconnect()
    def find_all(self):
        self.connect()
        self.cursor.execute("""select * from university.students order by name,family""")
        student_list=self.cursor.fetchall()
        self.disconnect()
        return student_list
    def find_by_id(self,student_id):
        self.connect()
        self.cursor.execute(""" select * from university.students where s_id=%s
        """,[student_id])
        student=self.cursor.fetchone()
        self.disconnect()
        return student


    def find_by_name_and_family(self,name,family):
        self.connect()
        self.cursor.execute(""" select * from university.students 
        where name like %s and family like %s""",
            [name+"%",family+"%"])
        student_list=self.cursor.fetchall()
        self.disconnect()
        return student_list
    def find_by_username_and_password(self,username,password):
        self.connect()
        self.cursor.execute(""" select * from university.students 
                where username =%s and password = %s""",
                            [username, password])
        student = self.cursor.fetchall()
        self.disconnect()
        return student

    def find_duplicate_usernames(self,username):
        self.connect()
        self.cursor.execute("""select * from university.students
                where username=%s""",[username])
        result=self.cursor.fetchall()
        self.disconnect()
        return result