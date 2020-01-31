"""
def getFibonacci(n):
    numbers = [0, 1]
    counter = 0
    while counter + 2 < n:
        numbers.append(numbers[counter] + numbers[counter + 1])
        counter += 1
    

    return numbers

print(getFibonacci(10))
"""

"""
def getFibonacci(n, arr, counter = 0):
    if counter == n:
        return arr
    else:
        #arr = [0, 1]
        arr.append(arr[counter] + arr[counter + 1])
        return getFibonacci(n, arr, counter + 1)
    

print(getFibonacci(10, [0, 1]))
"""


"""
def getFibonacci(n, arr, counter = 0):
    arr = [0, 1]
    if counter + 2 == n:
        return arr
    else:
        arr.append(arr[counter] + arr[counter + 1])
        return getFibonacci(n, arr, counter + 1)
    

print(getFibonacci(10))
"""

def getFibonacci(n, counter = 0, arr = [0, 1]):
    # arr = [0, 1] -> arr = [0, 1] every time this function is executed.
    # That's why it's necessary to pass in the new array as an argument.
    if counter == n:
        return arr
    else:
        arr.append(arr[counter] + arr[counter + 1])

        return getFibonacci(n, counter + 1)

print(getFibonacci(10))
