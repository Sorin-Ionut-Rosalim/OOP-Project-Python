from categories import Categories
from amplifier import Amplifier
from receiver import Receiver
from speaker import Speaker
from turntable import Turntable
from json import loads
from order import Order
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier


def display_products():
    categories = Categories.load_categories()
    for cat in categories:
        with open(f"{(cat.name).lower()}s.txt", "r") as file:
            print(
                f"You have the following products in the {cat.name} category:")
            for i, line in enumerate(file):
                data = loads(line)
                print(f"%d. %s" % (i, data))
        print("\n\n")


def display_products_pm():
    display_products()
    if (input("Do you want to continue: 1/0\n\t") == "1"):
        cls()
        to_products()
    else:
        cls()
        menu()


def create_options() -> dict:
    categories = Categories.load_categories()
    options_menu = {}
    for index, cat in enumerate(categories):
        print(f'{index + 1}. {cat.name}')
        options_menu[index + 1] = cat.name

    return options_menu


def to_categories():
    def add_category():
        category = input("Insert the name of the new category:\n\t")
        Categories.add_category(category)
        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_categories()
        else:
            cls()
            menu()

    def remove_category():
        category = input(
            "Insert the name for the category you want to remove:\n\t")
        Categories.remove_category(category)
        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_categories()
        else:
            cls()
            menu()

    def display_categories():
        categories = Categories.load_categories()
        if categories != []:
            for cat in categories:
                print(cat.name)
        else:
            print("No categories found")

        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_categories()
        else:
            cls()
            menu()

    print("""
    1. Add a category
    2. Remove a category
    3. Display all the categories called
    4. Back to the main menu
    """)
    option = int(input("Enter an option between 1 and 4: "))

    actions = {1: add_category, 2: remove_category,
               3: display_categories, 4: menu}

    action = actions.get(option, error_handler)
    action()


def collect_data(category: str) -> Amplifier | Receiver | Turntable | Speaker:
    if category == "Amplifier":
        name = input("Name: ")
        power = int(input("Power: "))
        channels = int(input("NO. channels: "))
        size = int(input("Size: "))
        return Amplifier(name, power, channels, size)

    elif category == "Receiver":
        name = input("Name: ")
        color = input("Color: ")
        channels = input("NO. channels: ")
        size = int(input("Size: "))
        return Receiver(name, color, channels, size)

    elif category == "Turntable":
        name = input("Name: ")
        speed = int(input("Speed: "))
        conn = int(input("Wired/Bluetooth (0/1): "))
        size = int(input("Size: "))
        return Turntable(name, speed, conn, size)

    elif category == "Speaker":
        name = input("Name: ")
        power = int(input("Power: "))
        wheight = int(input("Wheight: "))
        size = int(input("Size: "))
        return Speaker(name, power, wheight, size)


def to_products():
    def add_product():
        options_menu = create_options()
        category = int(input("Enter the category of the product: "))
        obj = collect_data(options_menu.get(category, error_handler))
        Amplifier.add_amplifier(obj)
        Receiver.add_receiver(obj)
        Turntable.add_turntable(obj)
        Speaker.add_speaker(obj)
        print("Product added")
        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_products()
        else:
            cls()
            menu()

    def remove_product():
        options_menu = create_options()
        category = int(input("Enter the category of the product: "))
        with open(f"{(menu.get(category, error_handler)).lower()}s.txt", "r") as file:
            print("You have the following products in this category:")
            for i, line in enumerate(file):
                data = loads(line)
                print(f"%d. %s" % (i, data))
        obj = collect_data(options_menu.get(category, error_handler))
        print(obj)
        Amplifier.remove_amplifier(obj)
        Receiver.remove_receiver(obj)
        Turntable.remove_turntable(obj)
        Speaker.remove_speaker(obj)
        print("Product removed")
        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_products()
        else:
            cls()
            menu()

    print("""
    1. Add a product
    2. Remove a product
    3. Display all the products
    4. Back to the main menu
    """)
    option = int(input("Enter an option between 1 and 4: "))

    actions = {1: add_product, 2: remove_product,
               3: display_products_pm, 4: menu}

    action = actions.get(option, error_handler)
    action()


def to_orders():

    def place_order():
        name = input("Full Name: ")
        address = input("Address: ")
        c_order = Order(name, address)
        while True:
            print("""
                    Available products:
                    """)
            display_products()
            oprions = create_options()
            option = int(input("Choose a category: "))
            obj = collect_data(oprions.get(option, error_handler))
            if obj in Amplifier.load_amplifiers():
                c_order.add_product_to_order(obj)
            elif obj in Receiver.load_receivers():
                c_order.add_product_to_order(obj)
            elif obj in Speaker.load_speakers():
                c_order.add_product_to_order(obj)
            elif obj in Turntable.load_turntables():
                c_order.add_product_to_order(obj)
            else:
                print("Product is not available.")
            print("""
                    Current order:
                """)
            c_order.load_products_from_order()
            for obj in c_order.products:
                print(obj)
            if (input("Do you want to add another product?: 1/0\n\t") == "1"):
                pass
            else:
                break

        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_orders()
        else:
            cls()
            menu()

    def display_orders():
        files = [f for f in os.listdir('orders')]
        if files == []:
            print("You have no orders")
            if (input("Do you want to continue: 1/0\n\t") == "1"):
                cls()
                to_orders()
            else:
                cls()
                menu()
        print("You have the following orders:")
        for file in files:
            n_order = Order.load_order(file)
            print(n_order, '\n')
        if (input("Do you want to continue: 1/0\n\t") == "1"):
            cls()
            to_orders()
        else:
            cls()
            menu()

    print("""
    1. Place a new order
    2. Display all orders
    3. Back to the main menu
    """)
    option = int(input("Enter an option between 1 and 4: "))

    actions = {1: place_order, 2: display_orders,
               3: menu}

    action = actions.get(option, error_handler)
    action()


def exit():
    print("Exit called")


def error_handler():
    print("Action not supported")
    if (input("Do you want to continue: 1/0\n\t") == "1"):
        cls()
        menu()
    else:
        cls()
        exit()


def menu():
    print("""
    1. Categories
    2. Products
    3. Orders
    4. Exit
    """)
    option = int(input("Enter an option between 1 and 4: "))

    actions = {1: to_categories, 2: to_products,
               3: to_orders, 4: exit}

    action = actions.get(option, error_handler)
    action()


if __name__ == "__main__":
    menu()
