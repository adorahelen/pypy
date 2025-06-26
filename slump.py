def func (lst):
    for i in range (len(lst) // 2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
        # 동시할당을 통한 tuple unpacking change 

lst = [1,2,3,4,5,6]

func(lst)      
print(sum(lst[::2]) - sum(lst[1::2]))