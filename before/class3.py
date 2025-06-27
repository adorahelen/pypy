class Today:
    @classmethod
    def DAY250625(cls, self2):
        pass


# •	클래스 내부에서 인스턴스에 작용하는 동작이면 → self
# •	클래스 자체에 작용하거나 클래스 변수 변경이면 → @classmethod, cls
# •	클래스와 아무 관련 없는 독립 기능이면 → 그냥 def


class Student:
    count = 0
    students = []

    @classmethod
    def print(self):
        print("----- student list -----")
        print("name\t total\t average")
        for student in self.students:
            print(str(student))
        print("==============================")    
        

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t {}\t {}".format(self.name, self.get_sum(), self.get_average())
    
