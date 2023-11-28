class Inventory:
    """ Initializes the articles dictionary"""
    def __init__(self):
        self.articles = {}

    """ Adds an article to the inventory """
    def add_article(self, name, quantity, price):
        if name in self.articles:
            print("The item already exists in inventory.")
        else:
            self.articles[name] = {'quantity': quantity, 'price': price}
            print(f"Item '{name}' added to inventory.")

    """ Deletes an article from the inventory """
    def del_article(self, name):
        if name in self.articles:
            del self.articles[name]
            print(f"Item '{name}' deleted from inventory.")
        else:
            print("The item does not exist in inventory.")

    """ Updates the quantity of an existing article """
    def upd_quantity(self, name, quantity):
        if name in self.articles:
            self.articles[name]['quantity'] += quantity
            print(f"Updated quantity for '{name}'.")
        else:
            print("The item does not exist in inventory.")

    """ Updates the price of an existing article """
    def upd_price(self, name, price):
        if name in self.articles:
            self.articles[name]['price'] = price
            print(f"Updated price for '{name}'.")

    """ Displays all articles present in the inventory """
    def shw_inventory(self):
        if not self.articles:
            print("Inventory is empty.")
        else:
            print("\nInventory:")
            for name, info in self.articles.items():
                print(f"name: {name}, quantity: {info['quantity']}, price: {info['price']}")
