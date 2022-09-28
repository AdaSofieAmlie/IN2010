from re import I
import sys

inputList = []

def makeBalanceSearchTree(inList, inBalanceList):
    if (len(inList) > 3):
        middle = (len(inList)) / 2
        inBalanceList.append(inList[middle])
        firstHalf = inList[:middle]
        makeBalanceSearchTree(firstHalf, inBalanceList)
        secondHalf = inList[middle+1:]
        makeBalanceSearchTree(secondHalf, inBalanceList)
    else:
        if (inList[0] > inList[1]):
            inBalanceList.append(inList[0])
            inBalanceList.append(inList[1])
        else:
            inBalanceList.append(inList[1])
            inBalanceList.append(inList[0])
    print(inBalanceList)



for line in sys.stdin:
    line = int(line)
    inputList.append(line)

print(inputList)
balanceList = []
makeBalanceSearchTree(inputList, balanceList)