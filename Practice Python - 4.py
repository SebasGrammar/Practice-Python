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

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://math.stackexchange.com/questions/1039519/finding-prime-factors-by-taking-the-square-root/1039525

import math  
  

def findDivisors() :
    userInput = int(input("Please enter a number: "))
    divisors = []
    below = []
    check = range(1, int(math.sqrt(userInput) + 1)) # (inclusive, exclusive)
    for number in check: 
          
        if (userInput % number == 0) : 
            if (userInput / number == number) : 
                divisors.append(number)
            else : 
                below.append(number)
                divisors.append(int(userInput / number))   

    return below + divisors
          
print(findDivisors()) 

  

