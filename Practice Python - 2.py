number = int(input("Please enter a number: "))

if number % 4 == 0:
    print("{number} is a multiple of 4".format(number = number))
elif number % 2 == 0:
    print(f"{number} is a multiple of 2".format(number = number))
else:
    print(f"{number} is odd".format(number = number))
