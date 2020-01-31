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

"""
doThat(generateList) (1)
vs
doThat(generateList()) (2)

In (1), we are just passing in the reference to a function, while in (2)
we are actually calling the function and using whatever value it returns
as an argument for the outer function.

This is different from what happens with the doThis function, in which the
function passed in as an argument is being called from the body of doThis.
The problem with this is that if we wanted to pass in any arguments to the inner function,
we would have to make that clear by passing them in the function call. If we decided that's not what we want,
we would have to change the body of the function. = not so flexible.
"""


