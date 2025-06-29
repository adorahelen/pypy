# def flatten(data):
#     output = []
#     for item in data:
#         if type(item) == list:
#             output += item

#         else:
#             output.append(item)
#     return output

# example = [[1,2,3], [4, [5,6]], 7, [8,9]]
# print(" origin : ", example)
# print(" changed : ", flatten(example))

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1,2,3], [4, [5,6]], 7, [8,9]]
print(" origin : ", example)
print(" changed : ", flatten(example))

