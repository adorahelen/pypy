class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + "가(이) 소리를 낸다.")

# Animal을 상속받은 Dog 클래스
class Dog(Animal):
    def speak(self):  # 메서드 오버라이딩
        print(self.name + "가(이) 멍멍 짖는다.")

# Animal을 상속받은 Cat 클래스
class Cat(Animal):
    def speak(self):  # 메서드 오버라이딩
        print(self.name + "가(이) 야옹 운다.")

# 사용 예
a = Animal("동물")
d = Dog("강아지")
c = Cat("고양이")

a.speak()  # 동물가(이) 소리를 낸다.
d.speak()  # 강아지가(이) 멍멍 짖는다.
c.speak()  # 고양이가(이) 야옹 운다.