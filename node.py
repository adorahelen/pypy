class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def tree(li):
    nodes = [Node(i) for i in li]# 리스트 컴프리헨션 문법
    for i in range(1, len(li)) : 
        nodes [ (i -1) // 2].children.append(nodes[i]) # 실 구현
    return nodes[0]

def calc(node, level =0):
    if node is None:
        return 0 # 재귀적으로 트리 순회 
    return (node.value if level % 2 == 1 else 0) + sum(calc(n, level + 1) for n in node.children)

li = [3, 5, 8, 12, 15, 18, 21]

root = tree(li)

print(calc(root))