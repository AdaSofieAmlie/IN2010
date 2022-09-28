
import sys
import math

inputList = []

def makeBalanceSearchTree(inList, inBalanceList):
    #Hvis arrayet er stort nok til at det trenger å bli kalt på rekursivt
    if (len(inList) >= 3):
        #finner elementet i midten og sorterer det i den nye listen
        middle = math.floor((len(inList) -1 ) / 2)
        inBalanceList.append(inList[middle])

        #kaller rekursivt på høre og venstres siden av listen for å sortere videre
        firstHalf = inList[:middle]
        makeBalanceSearchTree(firstHalf, inBalanceList)

        secondHalf = inList[middle+1:]
        makeBalanceSearchTree(secondHalf, inBalanceList)

    #Hvis arrayet er så lite at det ikke kan bli kalt på rekursivt igjen
    else:
        if (len(inList) == 1):
            inBalanceList.append(inList[0])
        elif (inList[0] > inList[1]):
            inBalanceList.append(inList[0])
            inBalanceList.append(inList[1])
        else:
            inBalanceList.append(inList[1])
            inBalanceList.append(inList[0])
    return inBalanceList

#Print out balanced array
def printOut(inBL):
    for element in inBL:
        print(element)

#put input into a input list
for line in sys.stdin:
    element = int(line.strip())
    inputList.append(element)

balanceList = []
balanceArray = makeBalanceSearchTree(inputList, balanceList)
printOut(balanceArray)