from inventory import Inventory

def menu():
    print("\nWelcome to the Inventory System")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Update quantity")
    print("4. Update price")
    print("5. Show inventory")
    print("6. Exit")
    return input("Select an option: ")

if __name__ == "__main__":
    inventory = Inventory()

    while True:
        option = menu()

        if option == "1":
            name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: "))
            inventory.add_article(name, quantity, price)

        elif option == "2":
            name = input("Enter the name of the item to delete: ")
            inventory.del_article(name)

        elif option == "3":
            name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity to add or subtract: "))
            inventory.upd_quantity(name, quantity)

        elif option == "4":
            name = input("Enter the name of the item: ")
            price = float(input("Enter the new price: "))
            inventory.upd_price(name, price)

        elif option == "5":
            inventory.shw_inventory()

        elif option == "6":
            break

        else:
            print("Invalid option. Please select a valid option.")
