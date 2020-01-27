import random

def listsOverlap(listA, listB):
    return list(set([number for number in listA if number in listB]))

a = [1, 1, 2, 3, 837, 5, 8, 13, 21, 34, 55, 89, 800]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 200, 15, 800, 837]

listA = [random.randint(0, 100) for number in range(random.randint(5, 20))]
listB = [random.randint(0, 100) for number in range(random.randint(5, 20))]

print(listsOverlap(a, b))

print(listsOverlap(listA, listB))

