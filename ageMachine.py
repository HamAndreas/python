"""
this function takes integer age as argument and print if the person is old or young
"""

def ageMachine(age: int):
    if age >= 50:
        print("Du bist alt!")
    else:
        print("Du bist jung!")

"""
this function accepts two integer as arguments and adds them
returns result of summation
"""
# mercedes_auto     snake_case can be used for variables
def addTwoNumers(first_num: int , second_num: int)-> int:
    return first_num + second_num

ageMachine(49.999999)

result = addTwoNumers(5, 10)
print(f"It is: {result}")