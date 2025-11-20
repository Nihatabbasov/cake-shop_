class Shop:
    def __init__(self, name, location):
        self.name = name 
        self.location = location
class Cakes:
    def __init__(self, name, ingriedents, price, stocks):
        self.name = name
        self.ingridients = ingriedents
        self.price = price
        self.stocks = stocks
    def __str__(self):
        return f"{self.name} {self.ingridients}"
    def __repr__(self):
        return f"Name : {self.name}\n" 
    def info_stocks(self):
        """
        this functions remind the seller that bring new one
        returns:
              str
        """
        if self.stocks < 10:
            return f"Restock {self.name} cake"
        return f"We have enough"


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.customer_basket = []
    def buy_cake(self, cake: Cakes):
        """
        this function give information about cakes in stocks.
        if cake in stocks lesser than 1 you cannot buy otherwise
        you can buy and divise from stocks
        returns:
                 str
        """
        if cake.stocks > 0:
            self.customer_basket.append(cake)
            cake.stocks -= 1
            print(f"you bought {cake.name}")
        else:
            print(f"Sorry we have not {cake.name}")
    def calculate_price(self):
        """
        This function calculate total price all cakes in the customer's backet
        returns:
                float   
        """
        total = sum(x.price for x in self.customer_basket)
        return total
    def check_balance(self):
        """
        This function checking the customers balance
        """
        total_price = self.calculate_price()
        if customer.balance < total_price:
            print("Insufficient balance!")
        else:
            print("Balance is sufficient.")


shop = Shop("Azza", "Baku 12A street")
customer = Customer("john", 30)
cake_bluberry = Cakes("Bluberry", "[fresh Blueberry, Vanilla]", 15.99, 18)
cake_troufel = Cakes("Troufel", "[dark schocolate, vanilla]", 19.99, 3)
customer.buy_cake(cake_troufel)
customer.buy_cake(cake_troufel)
customer.buy_cake(cake_troufel)
print(customer.calculate_price())
customer.check_balance()