# A)

import sys

class Node:
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None

#Oppslag
def contains(v, x):
    if v is None:
        return False
    if v.element == x:
        return True
    if x < v.element:
        return contains(v.left, x)
    if x > v.element:
        return contains(v.right, x)

#innsetting
def insert(v, x):
    if v is None:
        v = Node(x)
    elif x < v.element:
        v.left = insert(v.left, x)
    elif x > v.element:
        v.right = insert(v.right, x)
    return v

#Sletting
def remove(v, x):
    if v is None:
        return None
    if x < v.element:
        v.left = remove(v.left, x)
        return v
    if x > v.element:
        v.right = remove(v.right, x)
        return v
    if v.left is None:
        return v.right
    if v.right is None:
        return v.left
    
    u = findMin(v.right)
    v.element = u.element
    v.right = remove(v.right, u.element)
    return v

#Finn minste
def findMin(v):
    if v is None:
        return None
    node = v
    while node.left != None:
        node = node.left
    return node


#size returnerer str til set        
def size(v):
    if v is None:
        return 0
    return (1 + size(v.left) + size(v.right))

#lese stdin
file = sys.stdin
commandCount = int(file.readline().strip())
i = 0

#start noden
root = None

while i < commandCount:
    c = file.readline().strip()
    data = c.split(" ")
    function = data[0]

    if len(data) == 2:
        element = int(data[1])

    if function == 'contains':
        con = contains(root, element)
        print(con)
    elif function == 'insert':
        root = insert(root, element)
    elif function == 'remove':
        root = remove(root, element)
    elif function == 'size':
        sizeSet = size(root)
        print(sizeSet)
    i = i+1
