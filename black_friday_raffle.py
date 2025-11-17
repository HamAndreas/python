# Einfacher Black-Friday-Raffle in einer Datei, nutzt Arrays (Listen)

products = [
    "smartphone",
    "notebook",
    "headphones",
    "smartwatch",
    "tablet",
    "bluetooth-speaker",
    "gaming-mouse",
    "gaming-monitor",
    "SSD 1TB storage",
    "USB storage stick 64GB"
]

# amount of storage (index corresponds to product)
inventory = [5, 2, 10, 3, 1, 4, 6, 2, 1, 8]


def list_products():
    print("\navailable products:")
    for idx, name in enumerate(products):
        print(f"{idx}: {name}")
    print()


def choose_product():
    choice = input("Select a product by entering the index number (or type 'q' to exit): ").strip()
    if choice.lower() == "q":
        return None
    if not choice.isdigit():
        print("Please enter a number (index).")
        return -1
    idx = int(choice)
    if idx < 0 or idx >= len(products):
        print("Invalid input.")
        return -1
    return idx


def deliver_product(idx):
    if inventory[idx] > 0:
        inventory[idx] -= 1
        print(f"Hooray! Your selected product '{products[idx]}' will be delivered soon.")
        return True
    else:
        print(f"Unlucky. '{products[idx]}' is not in stock. Better luck next time!")
        return False


def run_raffle(max_attempts=3):
    attempts = 0
    print("Welcome to the great Black Friday Raffle!")
    while attempts < max_attempts:
        list_products()
        sel = choose_product()
        if sel is None:
            print("Aborted by user.")
            break
        if sel == -1:
            # invalid input, attempt will not be counted
            continue
        success = deliver_product(sel)
        attempts += 1
        if success:
            # when item is delivered, the loop will be aborted
            print("Raffle is closed after successful delivery.")
            break
        else:
            print(f"Remaining attempts: {max_attempts - attempts}")
    else:
        print("Unfortunately you don't have any attempts left.")



if __name__ == "__main__":
    run_raffle()