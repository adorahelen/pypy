# 문자열 생성
s1 = "Hello"
s2 = 'World'
s3 = """여러 줄
문자열입니다."""

# 문자열 연결 및 반복
joined = s1 + " " + s2
repeated = "Hi" * 3

# 문자열 인덱싱 & 슬라이싱
sample = "Python Programming"

# 인덱싱
first_char = sample[0]     # 'P'
last_char = sample[-1]     # 'g'

# 슬라이싱 (다양한 예시)
slice1 = sample[0:6]       # 'Python'
slice2 = sample[7:18]      # 'Programming'
slice3 = sample[:6]        # 'Python'
slice4 = sample[7:]        # 'Programming'
slice5 = sample[-11:-4]    # 'ogramm'
slice6 = sample[::-1]      # 역순 'gnimmargorP nohtyP'
slice7 = sample[::2]       # 홀수 인덱스 문자 추출 'Pto rgamn'

# 문자열 메서드
trimmed = " hello python ".strip()     # 'hello python'
uppered = sample.upper()               # 'PYTHON PROGRAMMING'
lowered = sample.lower()               # 'python programming'
capitalized = sample.capitalize()      # 'Python programming'
replaced = sample.replace("Python", "Java")  # 'Java Programming'
splitted = sample.split()              # ['Python', 'Programming'] //사용하면 문자열을 리스트로 만들어 버리네;
joined_with_dash = "-".join(["a", "b", "c"])  # 'a-b-c' //이렇게 위 아래는 파괴적 함수인거 같음 

# 문자열 검색
contains_love = "love" in "I love Python"         # True
find_python = sample.find("Python")               # 0
count_o = sample.count("o")                       # 2

# 문자열 포매팅
name = "Alice"
age = 25
formatted1 = f"My name is {name}, and I am {age} years old."
formatted2 = "My name is {}, and I am {} years old.".format(name, age)
formatted3 = "My name is %s, and I am %d years old." % (name, age)

# 이스케이프 문자
escaped = "줄 바꿈\n탭\t따옴표\"표현"

# 출력
print("▶ 문자열 생성:\n", s1, s2, s3)
print("\n▶ 연결과 반복:\n", joined, repeated)
print("\n▶ 인덱싱:\n", first_char, last_char)
print("\n▶ 슬라이싱:")
print("  - sample[0:6]:", slice1)
print("  - sample[7:18]:", slice2)
print("  - sample[:6]:", slice3)
print("  - sample[7:]:", slice4)
print("  - sample[-11:-4]:", slice5)
print("  - sample[::-1]:", slice6)
print("  - sample[::2]:", slice7)
print("\n▶ 문자열 메서드:")
print(trimmed, uppered, lowered, capitalized, replaced, splitted, joined_with_dash, sep="\n")
print("\n▶ 문자열 검색:")
print(contains_love, find_python, count_o)
print("\n▶ 문자열 포매팅:")
print(formatted1)
print(formatted2)
print(formatted3)
print("\n▶ 이스케이프 문자:")
print(escaped)

# 파괴적 함수 (원본 자체를 건드림) / 비파괴적 함수(원본은 그대로)


# import java.util.*;

# public class Main {
#     public static void main(String[] args) {
#         List<String> fruits = Arrays.asList("apple", "banana", "cherry");

#         for (String fruit : fruits) {
#             System.out.println(fruit);
#         }
#     }
# }

# =============================================================================

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)