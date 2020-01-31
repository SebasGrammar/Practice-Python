import random

def generateList():
    return [random.randint(0, random.randint(1, 100)) for number in range(0, 10)]


print(generateList())

def findEnds(lst):
    return [lst[0], lst[- 1]]

"""
def main():
    randomList = generateList()
    print(randomList)
    print(findEnds(randomList))
"""

def main(listGenerator, endsFinder):
    randomList = listGenerator()
    print(randomList)
    print(endsFinder(randomList))
    

main(generateList, findEnds)

## HIGHER ORDER FUNCTIONS - JUST AS IN JAVASCRIPT ##

def doThis(x):
    print(x())

doThis(generateList)

def doThat(x):
    print(x)

doThat(generateList())
