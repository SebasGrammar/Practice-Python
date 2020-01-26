"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
belowFive = []

for number in a:
    if number < 5:
        print(number)
        belowFive.append(number)


print(belowFive)
"""

inputNumber = int(input("Please enter a number: ")) 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
belowFive = list(filter(lambda x: x < inputNumber, a))
print(belowFive)
