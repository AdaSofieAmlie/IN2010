import sys

def findWayOut(treeInn, fromX):
    print(fromX)
    for key in tree.keys():
        if key == fromX:
            newStep = treeInn[fromX]
            findWayOut(treeInn, newStep)

            
#lese stdin
file = sys.stdin
tree = {}
kittenLocation = int(file.readline().strip())
c = file.readline().strip()

while c != "-1":
    children = c.split(" ")
    parent = children[0]
    parent = int(parent)

    #sette nodene i en dict
    for child in children[1:]:
        child = int(child)
        tree[child] = parent

    c = file.readline().strip()

#finn veien ut
findWayOut(tree, kittenLocation)
