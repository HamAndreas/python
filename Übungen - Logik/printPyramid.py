def printDreieck(i):
    dreieck=""
    while i > 0:
        dreieck += "*"
        print(dreieck)
        i -= 1

i = int(input("What size should the triangle be? "))  # ask for user input for variable i, and convert to integer
printDreieck(i)   # run function createLine