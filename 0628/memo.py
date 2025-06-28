dict = { 1:1, 2:1}

def fibonachi(num):
    if num in dict:
        return dict[num]
    else:
        output = fibonachi(num -1) + fibonachi(num -2)
        dict[num] = output
        return output

        