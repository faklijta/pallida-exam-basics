# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.

# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"

class CandyShop(object):
    def __init__(self, sugar_amount):
        self.sugar_amount = 0
        self.income = 0
        self.storage = []
        self.type_of_sweet = ['lollipops', 'candies']
        if self.type_of_sweet == "lollipops":
            self.price = 10
            self.sugar = 5
        if self.type_of_sweet == "candies":
            self.price = 20
            self.sugar = 10
    

    def raise_prices(self, percent):
        return self.price * (percent / 100)


    def create_sweets(self, type_of_sweet):
        if self.type_of_sweet == 'lolipops':
            self.sugar -= self.sugar_amount
        if self.type_of_sweet == 'candies':
            self.sugar -= self.sugar_amount
        return self.storage.append(self.type_of_sweet)


    def sell(self, type_of_sweet, number):
        if self.type_of_sweet == 'lolipops':
            self.income += self.price * number
        if self.type_of_sweet == 'candies':
            self.income += self.price * number
        return self.storage.remove(self.type_of_sweet * number)


    def buy_sugar(self, number):
        self.sugar_price = 100/1000
        self.sugar += number
        self.income -= self.sugar_price * number


    def status(self):
        return "\nInventory: ({}) lollipops, ({}) candies, Income: ({}), Sugar: ({})gr ".format(self.storage, self.storage, self.income, self.sugar )

candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop.status)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop.status)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
# candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop.status)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop.status)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"
