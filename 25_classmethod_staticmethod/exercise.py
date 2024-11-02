# @classmethod and @staticmethod
## This coding exercise requires you to complete an implementation of two class methods two method implementations:
### 1. The franchise method, which takes in store as argument. It should return a new Store object, with name set to store.name + " - franchise".
### 2. The store_details method, which also takes in a store as argument. It should return a string representing the argument.


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        return sum(item["price"] for item in self.items)

    @classmethod
    def franchise(cls, store):
        return cls(f"{store.name} - franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(Store.franchise(store).name)  # Test - franchise
print(Store.franchise(store2).name)  # Amazon - franchise
print(Store.store_details(store))  # Test, total stock price: 0
print(Store.store_details(store2))  # Amazon, total stock price: 160
