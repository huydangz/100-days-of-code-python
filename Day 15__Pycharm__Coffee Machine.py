from data import MENU

def report(resources):
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f'Money: ${resources["money"]}')

def serve(q, d, n, p, action):
    money_taken = (q*25 + d*10 + n*5 + p) / 100
    price = MENU[action]["cost"]
    if money_taken < price:
        print(f"Sorry there is not enough money. You pay {money_taken}, meanwhile price for {action} is {price}.")
    else:
        payback = round(money_taken - price, 2)
        print(f"Here is ${payback} in change.")
        print(f"Here is your {action} ☕️. Enjoy!")
        global resources
        resources["money"] += price
        for thing in ["water", "milk", "coffee"]:
            resources[thing] -= MENU[action]["ingredients"][thing]

def is_enough(action, resources):
    checklist = ["water", "milk", "coffee"]
    for thing in checklist:
        if resources[thing] < MENU[action]["ingredients"][thing]:
            print(f"Sorry there is not enough {thing}.")
            return False
    return  True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
keep_using = True
while keep_using:
    action = input("What would you like? (espresso/latte/cappuccino):")
    if action == "off":
        keep_using = False
    elif action == "report":
        report(resources)
    elif is_enough(action, resources):
        print("Please insert coins.")
        q = int(input("how many quarters?: "))
        d = int(input("how many dimes?: "))
        n = int(input("how many nickles?: "))
        p = int(input("how many pennies?: "))
        serve(q, d, n, p, action)

============================data.py==================================
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

