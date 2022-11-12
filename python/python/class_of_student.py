from re import M


class Student:
    def __init__(self, name,major,gpa):
        self.name = name
        self.gpa = gpa
        self.major = major
        
        

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False






