# Exercise: print a triangle based on "*" and "-"

def printTriangle(i):
    for i in range(i):
        if i%2==0:
            print("-"*i)
        else:
            print("*"*i)

i = int(input("What size should the triangle be? "))
printTriangle(i)