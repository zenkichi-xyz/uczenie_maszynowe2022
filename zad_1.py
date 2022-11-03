class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if sum(self.marks) / len(self.marks) > 50:
            return True
        return False

    
s1 = Student('Szymon', [40, 50, 50, 70, 80])
s2 = Student('Jan', [10, 50, 49, 30, 20])