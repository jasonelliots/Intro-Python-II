from user import User 
import sys
from department import Department 
from products import Product
from store import Store

num_args = len(sys.argv)
if num_args == 1:
    user = User(100)
elif num_args == 2:
    user = User(int(sys.argv[1]))
else:
    print("Usage: store.py [money]")
    sys.exit(1)

departments = {
    23: Department(23, "Groceries", [Product("Bananas", 0.60), Product("Avos", 2.60), Product("Watermelon", 1.60)]), 
    9: Department(9, "Books", [Product("Game of Thrones", 10.60), Product("Working in Public", 12.60), Product("Watermelon Chronicles", 1.60)]),
    13: Department(13, "Electronics", [Product("Samsung 4k TV", 300.60), Product("Iphone SE", 2000.60), Product("Pixel 4a", 1000.60)]),
    7: Department(7, "Clothes", [Product("Shirt", 0.60), Product("Shorts", 2.60), Product("Hat", 1.60)]),
    15: Department(15, "Toys", [Product("RC Car", 100.60), Product("Rattle", 2.60), Product("Poi", 19.60)]),
}

store = Store("Quarantine Store", departments)

print(store)
print(user, '\n')

while True:

    #print departments before you ask which customer wants to vist - duh 

    store.print_departments()

    selection = input("\nWhich department would you like to visit? ")

    if selection == 'quit' or selection == 'q':
        break 

    # expect user to type in a number that is read in as a string 
    # parse it into an int and then check if the int is a valid department number

    dep_num = int(selection)

    if dep_num not in departments:
        print('\n that is not a valid dep')
        continue

    selected_dep = departments[dep_num]

    print(f"\nyou picked department number: {dep_num}, {selected_dep.name}\n")

    selected_dep.print_products()

    product_selection = int(input("What would you like to add to your cart?"))

    possible_products = selected_dep.products

    selected_product = possible_products[product_selection]

    user.add_to_cart(selected_product)






