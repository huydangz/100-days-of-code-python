from data import Menu, CoffeeMachine

coffee_machine = CoffeeMachine(300, 200, 100)
menu = Menu()

off = False
while not off:
    choice = input(f"What would you like? ({menu.get_items()}):")
    if choice == "off":
        off = True
    elif choice == "report":
        coffee_machine.report()
    else:
        item = menu.find_drink(choice)
        if item is not None and coffee_machine.can_serve(item):
            coffee_machine.serve(item)
