def print_n_times(*values):
    n = 2
    sumList = []

    for i in range(n):
        for value in values:
            # print(value)
            # sumList += value
            sumList.append(value)
    print(sumList)


print_n_times("You", "Can", "become", "A HERO")