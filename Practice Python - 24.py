"""
def drawRow(n):
	row = ["[]" for number in range(0, n)]
	print(row)

def drawBoard(n, fn):
    for number in range(0, n):
        fn(n)

drawBoard(4, drawRow)	
"""

def drawRow(n):
    row = ""
    for number in range(0, n):
        row += "[]"
    print(row)

def drawBoard(n, fn):
    for number in range(0, n):
        fn(n)

drawBoard(4, drawRow)
