from categories import Categories
from json import JSONDecodeError
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier


def to_categories():
    def add_category():
        category = input("Insert the name of the new category:\n\t")
        Categories.add_category(category)
        if (input("Do you want to continue: 1/0\n\t")):
            cls()
            menu()

    def remove_category():
        category = input(
            "Insert the name for the category you want to remove:\n\t")
        Categories.remove_category(category)
        if (input("Do you want to continue: 1/0\n\t")):
            cls()
            menu()

    def display_categories():
        try:
            categories = Categories.load_categories()
            for cat in categories:
                print(cat.name)
        except JSONDecodeError as e:
            categories = None
        if (input("Do you want to continue: 1/0\n\t")):
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


def to_products():
    def add_product(category):
        if (input("Do you want to continue: 1/0\n\t")):
            cls()
            menu()

    def remove_product(category):
        if (input("Do you want to continue: 1/0\n\t")):
            cls()
            menu()

    def display_products():
        if (input("Do you want to continue: 1/0\n\t")):
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
               3: display_products, 4: menu}

    action = actions.get(option, error_handler)
    action()


def to_orders():

    def place_order():
        if (input("Do you want to continue: 1/0\n\t")):
            cls()
            menu()

    def display_orders():
        if (input("Do you want to continue: 1/0\n\t")):
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


def Exit():
    print("Exit called")


def error_handler():
    print("Action not supported")
    if (input("Do you want to continue: 1/0\n\t")):
        cls()
        menu()


def menu():
    print("""
    1. Categories
    2. Products
    3. Orders
    4. Exit
    """)
    option = int(input("Enter an option between 1 and 4: "))

    actions = {1: to_categories, 2: to_products,
               3: to_orders, 4: Exit}

    action = actions.get(option, error_handler)
    action()


if __name__ == "__main__":
    menu()
