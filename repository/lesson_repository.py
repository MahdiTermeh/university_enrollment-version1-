import mysql.connector




class LessonRepository:
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

    def save(self,lesson):
        self.connect()
        self.cursor.execute("""insert into university.lessons
         (title,start_date,end_date,professor,room_number,credit,capacity) values (%s,%s,%s,%s,%s,%s,%s) """
        ,[lesson.title,lesson.start_date,lesson.end_date,lesson.professor,lesson.room_number,lesson.credit,lesson.capacity])
        self.connection.commit()
        self.disconnect()
    def edit(self,lesson):
        self.connect()
        self.cursor.execute("""update university.lessons set title=%s,start_date=%s,end_date=%s,
        professor=%s,room_number=%s,credit=%s,capacity=%s where l_id=%s
        """,[lesson.title,lesson.start_date,lesson.end_date,lesson.professor,lesson.room_number,lesson.credit,lesson.capacity,lesson.id] )
        self.connection.commit()
        self.disconnect()
    def remove(self,lesson_id):
        self.connect()
        self.cursor.execute(""" delete from university.lessons where l_id=%s""",
                            [lesson_id])
        self.connection.commit()
        self.disconnect()
    def find_all(self):
        self.connect()
        self.cursor.execute(""" select * from university.lessons order by title""")
        lesson_list=self.cursor.fetchall()
        self.disconnect()
        return lesson_list
    def find_by_id(self,lesson_id):
        self.connect()
        self.cursor.execute(""" select * from university.lessons where l_id=%s""",
                            [lesson_id])
        lesson=self.cursor.fetchone()
        self.disconnect()
        return lesson

    def find_by_title_and_professor(self, title, professor):
        self.connect()
        self.cursor.execute("SELECT * FROM university.lessons WHERE TITLE LIKE %s AND professor LIKE %s", [title + "%", professor + "%"])
        lesson_list = self.cursor.fetchall()
        self.disconnect()
        return lesson_list

    def get_lesson_capacity(self,lesson_id):
        self.connect()
        self.cursor.execute("select capacity from university.lessons where l_id=%s",
                            [ lesson_id])
        capacity = self.cursor.fetchone()[0]
        self.disconnect()
        return capacity

    def decrease_lesson_capacity(self,lesson_id):
        self.connect()
        self.cursor.execute("""update university.lessons set capacity= capacity-1 where l_id=%s
        """ , [lesson_id])
        self.connection.commit()
        self.disconnect()

    def increase_lesson_capacity(self, lesson_id):
        self.connect()
        self.cursor.execute("""update university.lessons set capacity= capacity+1 where l_id=%s
           """, [lesson_id])
        self.connection.commit()
        self.disconnect()