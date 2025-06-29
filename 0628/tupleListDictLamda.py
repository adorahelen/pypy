# 학생 데이터: 리스트 안에 튜플 (이름, 과목별 점수 딕셔너리)
students = [
    ("Alice", {"math": 90, "english": 85, "science": 78}),
    ("Bob", {"math": 70, "english": 65, "science": 72}),
    ("Charlie", {"math": 88, "english": 90, "science": 92}),
    ("Diana", {"math": 60, "english": 75, "science": 70}),
]

# 평균 점수를 구하는 람다 함수
calc_avg = lambda scores: sum(scores.values()) / len(scores)

# 평균이 80 이상인 학생만 필터링
passed_students = list(filter(lambda x: calc_avg(x[1]) >= 80, students))

# 평균 점수를 기준으로 내림차순 정렬
sorted_students = sorted(passed_students, key=lambda x: calc_avg(x[1]), reverse=True)

# 출력
print("🎓 평균 80점 이상 학생 목록 (내림차순 정렬):")
for name, scores in sorted_students:
    avg = calc_avg(scores)
    print(f"{name}: 평균 {avg:.2f}점 - 과목별 점수: {scores}")


print("===================================")


# 예제 데이터: 반마다 리스트, 각 리스트엔 (학생이름, 과목별 점수 딕셔너리) 튜플이 있음
classes = {
    "A": [
        ("Alice", {"math": 90, "english": 85, "science": 78}),
        ("Bob", {"math": 70, "english": 65, "science": 72}),
    ],
    "B": [
        ("Charlie", {"math": 88, "english": 90, "science": 92}),
        ("Diana", {"math": 60, "english": 75, "science": 70}),
    ],
    "C": [
        ("Eve", {"math": 95, "english": 98, "science": 100}),
        ("Frank", {"math": 45, "english": 50, "science": 55}),
    ]
}

# 평균을 계산하는 람다 함수
calc_avg = lambda scores: sum(scores.values()) / len(scores)

# 전체 학생 리스트 생성 (flattened)
all_students = [
    (class_id, name, scores)
    for class_id, student_list in classes.items()
    for name, scores in student_list
]

# 전체 평균 계산
all_avg = sum(map(lambda x: calc_avg(x[2]), all_students)) / len(all_students)

# 반별 평균 점수 계산
class_averages = {
    class_id: sum(map(lambda x: calc_avg(x[1]), students)) / len(students)
    for class_id, students in classes.items()
}

# 평균 80점 이상 학생만 필터링하고 정렬
top_students = sorted(
    filter(lambda x: calc_avg(x[2]) >= 80, all_students),
    key=lambda x: calc_avg(x[2]),
    reverse=True
)

# 출력
print("✅ 전체 평균 점수:", round(all_avg, 2))
print("\n🏫 반별 평균:")
for class_id, avg in class_averages.items():
    print(f" - {class_id}반: {avg:.2f}점")

print("\n🌟 평균 80점 이상 학생 (전체 정렬):")
for class_id, name, scores in top_students:
    print(f" - {name} ({class_id}반): 평균 {calc_avg(scores):.2f}점, 과목: {scores}")