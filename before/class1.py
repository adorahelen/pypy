
# class Kisaa :
#     pass

# kisaa = Kisaa()


# kisaa = [Kisaa(), Kisaa(), Kisaa(), Kisaa(), Kisaa()]


# 클래스 이름과 같은 함수를 생성자라고 부릅니다.
# 클래스 내부에 __init__ 라는 함수를 만들면 객체를 생성할 때 처리할 내용을 작성할 수 있습니다. 

class Security:
    def __init__(self):
        print("보안요원이 생성되었습니다.")

s = Security()  # 이 순간 __init__ 함수가 자동으로 실행됨


# self는 현재 생성되는 객체 자신을 가리킵니다.

# 클래스 안에서 정의한 함수들은 객체가 호출할 것이기 때문에,
# 그 객체 자신에 접근할 수 있도록 첫 번째 매개변수로 self를 꼭 넣어야 합니다.

class Security:
    def __init__(self, name, emotion, oath):  # name은 생성할 때 전달받는 값
        self.name = name  # self.name은 인스턴스 변수
        self.emotion = emotion
        self.oath = oath

s = Security("Alice", "love", "forever")  # name에 "Alice" 전달
print(s.emotion, s.name, s.oath)  # 출력: Alice


