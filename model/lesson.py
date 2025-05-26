
class Lesson:
    def __init__(self,id,title,start_date,end_date,professor,room_number,credit,capacity):
        self.id=id
        self.title=title
        self.start_date=start_date
        self.end_date=end_date
        self.professor=professor
        self.room_number=room_number
        self.credit=credit
        self.capacity=capacity

    def __repr__(self):
        return f"{self.__dict__}"