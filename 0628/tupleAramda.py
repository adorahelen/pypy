# 튜플 리스트
students = [
    ("John", 85),
    ("Alice", 92),
    ("Bob", 78),
    ("Diana", 90)
]

# 점수를 기준으로 정렬 (람다 사용)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    # 	•	sorted(..., key=lambda x: x[1]): 점수(x[1]) 기준으로 정렬


print("점수 기준 정렬 결과:")
for name, score in sorted_students:
    print(f"{name}: {score}")


# (이름, 국어, 영어, 수학)
scores = [
    ("Emma", 80, 90, 85),
    ("Tom", 70, 75, 80),
    ("Jane", 95, 85, 100)
]

# 평균 점수를 계산해서 출력
for student in scores:
    name, *subject_scores = student
    average = (lambda s: sum(s)/len(s))(subject_scores)
    print(f"{name}의 평균 점수는 {average:.2f}점입니다.")