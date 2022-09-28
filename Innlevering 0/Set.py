import sys

#Contains sjekker om settet har x i seg eller ikke
def contains(set, x):
    for i in set:
        if i == x:
            return True
    return False

#Insert setter inn element x i set
def insert(set, x):
    set = set | {x}
    return set

#Remove tar vekk x fra set
def remove(set, x):
    set = set - {x}
    return set

#size returnerer str til set        
def size(set):
    size = 0
    for i in set:
        size += 1
    return size

#Hovedprogram
s1 = set()

#lese stdin
file = sys.stdin
commandCount = int(file.readline().strip())
i = 0

while i < commandCount:
    c = file.readline().strip()
    data = c.split(" ")
    function = data[0]

    if len(data) == 2:
        element = int(data[1])

    if function == 'contains':
        con = contains(s1, element)
        print(con)
    elif function == 'insert':
        s1 = insert(s1, element)
    elif function == 'remove':
        s1 = remove(s1, element)
    elif function == 'size':
        sizeSet = size(s1)
        print(sizeSet)
    i = i+1
