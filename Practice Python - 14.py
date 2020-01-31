lst = [1, 1, 2, 3, 4, 4, 5, 4, 6, "one", "one"]

def removeDuplicates(lst):
    newList = []
    for element in lst:
        if element not in newList:
            newList.append(element)

    return newList


def removeWithSet(lst):
    return list(set(lst))


print(removeDuplicates(lst))
print(removeWithSet(lst))

print(lst)
