#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0 , ):
        self.discount = discount
        self.total = 0
        self.items = []
        self.items_with_prices = []
    

    def add_item(self,title, price, quantity = 1):
        self.total += (price * quantity)
        for _ in range(quantity):
            self.items.append(title)
            self.items_with_prices.append({"item":title, "quantity": quantity, "price": price})

    def apply_discount(self):
        if self.discount > 0 :
            self.total = int(self.total - (self.total * (self.discount)/100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.items_with_prices:
            return "There are no transactions to void."
        self.total -= (
            self.items_with_prices[-1]["price"]
            * self.items_with_prices[-1]["quantity"]
        )
        for _ in range(self.items_with_prices[-1]["quantity"]):
            self.items.pop()
        self.items_with_prices.pop()

        

