def getValue(list,targetValue,low,high):
    if high >= low:
        middle = low + (high-low) // 2
        if list[middle] == targetValue:
            return middle
        elif list[middle] < targetValue:
            return getValue(list,targetValue,middle+1,high)
        else:
            return getValue(list,targetValue,low,middle-1)
    else:
        return -1

listOne = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] #31
valueOne = 31
indexOne = getValue(listOne,valueOne,0,len(listOne)-1)

listTwo = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] #77
valueTwo = 77
indexTwo = getValue(listTwo,valueTwo,0,len(listTwo)-1)

listThree = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"] #Delta
valueThree = 'Delta'
indexThree = getValue(listThree,valueThree,0,len(listThree)-1)

def getIndex(index, value):
    if index == -1:
        return 'Item not found on list'
    else:
        return (f"{value} index is {index}")

print(getIndex(indexOne,valueOne))
print(getIndex(indexTwo,valueTwo))
print(getIndex(indexThree,valueThree))
