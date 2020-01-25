import datetime

print("Hello, world!")

userName = input("Please enter your name: ")

print(userName)

age = int(input("How old are you?: "))

year = datetime.datetime.now().year
willTurn100 = 100 - age

message = "You will be 100 years old in " + str(willTurn100) + " years... that is, in " + str(year + willTurn100)




print(message)

xTimes = int(input("Let me show you another trick!... enter a number: "))

print(xTimes * (message + "\n"))
