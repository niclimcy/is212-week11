class Items:
    def __init__(self, name, price, discount, tax_rate):
        self.name = name
        self.price = price
        self.discount = discount
        self.tax_rate = tax_rate

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount)
        print(f"Discounted price for {self.name} ({type(self).__name__}): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name} ({type(self).__name__}): {tax}")
        return tax

class Electronics(Items):
    def __init__(self, name, price):
        super().__init__(name, price, 0.10, 0.15)

class Clothing(Items):
    def __init__(self, name, price):
        super().__init__(name, price, 0.20, 0.08)

class Grocery(Items):
    def __init__(self, name, price):
        super().__init__(name, price, 0.05, 0.02)
        self.name = name
        self.price = price
