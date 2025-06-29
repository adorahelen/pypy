# 예외 처리 예제 - 파일 읽기, 사용자 입력, 계산, 사용자 정의 예외

class InvalidInputError(Exception):
    """사용자 정의 예외"""
    pass


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print("[파일 내용]")
            print(content)
    except FileNotFoundError:
        print(f"[오류] 파일이 존재하지 않습니다: {file_path}")
    except PermissionError:
        print(f"[오류] 파일에 접근 권한이 없습니다: {file_path}")
    except Exception as e:
        print(f"[알 수 없는 오류] {e}")
    else:
        print("[파일 읽기 성공]")
    finally:
        print("[read_file 종료]\n")


def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"[쓰기 실패] {e}")
    else:
        print("[파일 저장 성공]")
    finally:
        print("[write_file 종료]\n")


def calculate(a, b, op):
    try:
        a = float(a)
        b = float(b)

        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("0으로 나눌 수 없습니다.")
            return a / b
        else:
            raise InvalidInputError("지원하지 않는 연산자입니다.")
    except ValueError:
        raise InvalidInputError("숫자로 변환할 수 없는 값입니다.")
    except ZeroDivisionError as e:
        raise e


def user_input_loop():
    while True:
        try:
            a = input("첫 번째 숫자 입력 (또는 'exit'): ")
            if a.lower() == 'exit':
                break
            b = input("두 번째 숫자 입력: ")
            op = input("연산자 입력 (+, -, *, /): ")

            result = calculate(a, b, op)
            print(f"[결과] {a} {op} {b} = {result}\n")

        except InvalidInputError as e:
            print(f"[입력 오류] {e}\n")
        except ZeroDivisionError as e:
            print(f"[연산 오류] {e}\n")
        except Exception as e:
            print(f"[예기치 못한 오류] {e}\n")
        finally:
            print("-" * 40)


def main():
    print("=== 예외 처리 실습 프로그램 ===\n")

    # 1. 파일 읽기 시도
    read_file("input.txt")

    # 2. 파일 쓰기
    content = "예외 처리를 배워봅시다.\n파일에 텍스트를 저장합니다."
    write_file("output.txt", content)

    # 3. 사용자 계산기 실행
    user_input_loop()

    print("\n[프로그램 종료]")


# 프로그램 시작
if __name__ == "__main__":
    main()