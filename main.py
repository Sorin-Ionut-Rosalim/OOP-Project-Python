from categories import Categories
from category import Category
from json import JSONDecodeError


# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier
def to_categories():
    def add_category(category):
        pass

    def remove_category(category):
        pass

    def display_categories():
        try:
            categories = Categories.load_categories()
            for cat in categories:
                print(cat.name)
        except JSONDecodeError as e:
            categories = None

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
        pass

    def remove_product(category):
        pass

    def display_products():
        pass

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
        pass

    def display_orders():
        pass

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
    # below some usage examples

    # create some categories
    cat_1 = Category("Amplifiers")
    cat_2 = Category("Receivers")
    cat_3 = Category("Speakers")

    # add them inside the Categories collection, and also save them
    # on the disk
    Categories.add_category(cat_1)
    Categories.add_category(cat_2)
    Categories.add_category(cat_3)

    # display the existing categories

    # # remove one category from the Categories collection
    # Categories.remove_category(cat_3)

    # display again the existing categories
    # for cat in categories:
    #     print(cat.name)

    menu()
