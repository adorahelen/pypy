class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science 
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    

    # 학생 객체들을 리스트에 담기
students = [
    Student("Alice", 90, 85, 88, 92),
    Student("Bob", 78, 80, 75, 70),
    Student("Charlie", 95, 100, 98, 97),
    Student("David", 60, 65, 58, 62),
    Student("Eve", 85, 89, 90, 87)
]

print("name", "total", "avg", sep="\t")
for i in students:
    print(i.to_string())
    
