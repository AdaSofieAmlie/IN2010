
import sys

class Teque:
    def __init__(self):
        self.teque = []

    #O(1)
    def push_back(self, x):
        self.teque = self.teque + [x]
    
    #O(1)
    def push_front(self, x):
        self.teque = [x] + self.teque

    #O(n)
    def push_middle(self, x):
        size = 0
        for i in self.teque:
            size += 1
        middle = (size+1)/2
        self.teque = self.teque[0:middle] + [x] + self.teque[middle:]

    #0(1)
    def get(self, i):
        print(self.teque[i])


#lese stdin
tequeObject = Teque()
file = sys.stdin
commandCount = int(file.readline().strip())
i = 0

while i < commandCount:
    c = file.readline().strip()
    data = c.split(" ")
    function = data[0]

    if len(data) == 2:
        element = int(data[1])

    if function == 'push_back':
        tequeObject.push_back(element)
    elif function == 'push_front':
        tequeObject.push_front(element)
    elif function == 'push_middle':
        tequeObject.push_middle(element)
    elif function == 'get':
        tequeObject.get(element)
    i = i+1

