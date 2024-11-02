# Classes and Objects Exercise
## This coding exercise requires you to complete an implementation of three methods of a class:
### 1. The __init__ method, which should take in a name and an age. It should initialize self.name.
### 2. The add_item method, which should append a dictionary representing an item to store's items property.
### The dictionary should have keys name and price.
### 3. The stock_price method, which should add up each item price inside self.items to come up with a total price and return that.

# -- Your code here --
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        return sum(item["price"] for item in self.items)
