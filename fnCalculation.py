def fnCalculation(x, y):
    result = 0
    for i in range(len(x)):
        temp = x[i:i + len(y)]  # x에서 길이 len(y)만큼 부분 문자열 잘라냄
        if temp == y:           # 부분 문자열이 y와 같다면
            result += 1
    return result               # 들여쓰기 주의!

a = "abdcabcabca"
p1 = "ab"
p2 = "ca"

out = fnCalculation(a, p1) + fnCalculation(a, p2)
print(out)