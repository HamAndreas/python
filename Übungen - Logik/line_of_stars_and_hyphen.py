def createLine(n):
    symbol = ""
    i = 0
    while i < n:
        if i % 2 == 0:
            symbol += "*" 
        else:
            symbol += "-"
        i += 1
    print(symbol)

i = int(input("How many characters would you like to print? "))
createLine(i)