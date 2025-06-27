class Student:
    def __init__(self, name, score):
        self._name = name        # _name: 관례적으로 private 속성
        self._score = score      # _score도 마찬가지

    @property
    def score(self):
        print("게터 호출됨")
        return self._score

    @score.setter
    def score(self, value):
        print("세터 호출됨")
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("점수는 0에서 100 사이여야 합니다.")

# 사용 예
s = Student("철수", 85)
print(s.score)     # 게터 호출됨 → 85 출력
s.score = 95       # 세터 호출됨 → 값 변경
print(s.score)

s.score = 150      # 오류 발생!