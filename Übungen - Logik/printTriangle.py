# Exercise: print a triangle 

def printTriangle(i):
    triangle=""
    while i > 0:
        triangle += "*"
        print(triangle)
        i -= 1

i = int(input("What size should the triangle be? "))
printTriangle(i)