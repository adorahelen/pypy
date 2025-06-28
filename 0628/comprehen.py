# 원본 리스트
numbers = [1, 2, 3, 4, 5, 6]

# 1. 각 요소의 제곱
squares = [x**2 for x in numbers]

# 2. 짝수만 선택
evens = [x for x in numbers if x % 2 == 0]

# 3. (인덱스, 값) 튜플 리스트 (enumerate 사용)
indexed = [(i, x) for i, x in enumerate(numbers)]

# 4. 짝수는 그대로, 홀수는 '홀수' 문자열로
mixed = [x if x % 2 == 0 else "홀수" for x in numbers]

# 5. 2차원 리스트 생성 (중첩 for)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]

# 6. 2차원 리스트를 1차원으로 펼치기 (flatten)
flattened = [num for row in matrix for num in row]

# 결과 출력
print("원본 리스트:", numbers)
print("제곱:", squares)
print("짝수:", evens)
print("인덱스 포함:", indexed)
print("짝수는 숫자, 홀수는 '홀수' 문자열:", mixed)
print("2차원 리스트:", matrix)
print("펼친 리스트:", flattened)