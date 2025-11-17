# define function "transport_selection"
def transport_selection():
    # initialise list "list_items" with elements
    list_items = ["car", "motorbike", "bicycle", "skateboard", "jetski"]

    # for-loop to print each element in list_items with associated number of position
    for i in range(len(list_items)):
        print(f"For {list_items[i]} enter {i}")

    # ask for user input and convert to int
    user_input = input("Which transport would you like to get? Please enter item number: ")
    item_number = int(user_input)

    # delete item from list_items and save as selected_item
    selected_item = list_items.pop(item_number)

    # print Thank You message
    print(f"Thank you for ordering a {selected_item}. Your order is on its way.")

# start program
if __name__ == "__main__":
    transport_selection()