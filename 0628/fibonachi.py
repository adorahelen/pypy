# def fibonachi(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonachi(n-1) + fibonachi(n-2)
    
counter = 0

def fibonachi(n):
    global counter
    counter += 1

    if n==1:
        return 1
    if n ==2:
        return 2
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    
fibonachi(5)
print("=====")
print(counter)