def palindromeChecker():
    # No side effects (?)
    userInput = input("Please enter some text: ")
    string = userInput.replace(" ", "").lower()
    if string == string[::-1]:
        print("'{input}' is a palindrome.".format(input = userInput))
    else:
        print("'{input}' is not a palindrome.".format(input = userInput))
        

palindromeChecker()
