# Exercise: Print a line of stars. Number of stars must be given by the user
def createLine(i):  # define function createLine with i
    s = ""          # declare variable s as empty string
    while i > 0:    # do while i > 0
        s += "*"    # define str "*"
        i -= 1      # lower i by 1
    print(s)        # print variable s

i = int(input("How many stars would you like to print? "))  # ask for user input for variable i, and convert to integer
createLine(i)   # run function createLine