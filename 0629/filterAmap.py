def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]


output_a = map(power, list_input_a) # 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 map()

print(output_a)
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))