# BRUTE FORCE APPROACH
"""
def findDivisors():

    userInput = int(input("Please enter a number: "))

    counter = 2
    divisors = [1]

    while counter < userInput:
        if userInput % counter == 0:
            divisors.append(counter)
        counter += 1

    divisors.append(userInput)
    return divisors
    

print(findDivisors())
"""
# 
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math  
  
# Method to print the divisors 
def printDivisors() :
    userInput = int(input("Please enter a number: "))
    divisors = []
    below = []
    check = range(1, int(math.sqrt(userInput) + 1))
    for number in check: 
          
        if (userInput % number == 0) : 

            if (userInput / number == number) : 

                divisors.append(number)
            else : 

                below.append(number)
                divisors.append(int(userInput / number)) 
                  

    for number in below + divisors[::-1] : 
        print (number, end=" ") 
          

print ("The divisors of 100 are: ") 
printDivisors() 

  

