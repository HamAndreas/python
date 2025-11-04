def create_array(arr_length):
    my_array = []
    for i in range(arr_length):
        my_line = i*"*"
        my_array.append(my_line)
    return my_array

def print_array(some_array):
    for i in some_array:
        print(i)

print_array(create_array(4))