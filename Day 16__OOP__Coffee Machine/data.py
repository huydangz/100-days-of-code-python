class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, {"water": 50, "milk": 0, "coffee": 18}),
            MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24}),
            MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f"Sorry your choice is not available.")


class CoffeeMachine:
    COINS_VALUE = {
        "quarters": 25,
        "dimes": 10,
        "nickles": 5,
        "pennies": 1
    }

    def __init__(self, water, milk, coffee):
        self.resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        self.money = 0
        self.money_received = 0

    def report(self):
        for thing in self.resources:
            print(f"{thing}: {self.resources[thing]}")
        print(f"money: ${self.money}")
        print(f"money received: ${self.money_received}")

    def can_serve(self, item):
        for thing in self.resources:
            if self.resources[thing] < item.ingredients[thing]:
                print(f"Sorry not enough {thing}")
                return False
        return True

    def serve(self, item):
        # calc money_received
        print("Please insert coins.")
        for coin in self.COINS_VALUE:
            self.money_received += int(input(f"how many {coin}?: ")) * self.COINS_VALUE[coin] / 100
        if self.money_received < item.cost:
            print(f"Sorry not enough money. You pay ${self.money_received}, price for {item.name} is ${item.cost}.")
        else:
            # output coffee and change
            money_change = self.money_received - item.cost
            print(f"Here is your {item.name} and ${money_change} money change.")
            # update resources
            for thing in self.resources:
                self.resources[thing] -= item.ingredients[thing]
            self.money += item.cost
        self.money_received = 0
