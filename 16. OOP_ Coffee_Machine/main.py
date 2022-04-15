from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    # TODO: 1. print report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # TODO: 2. after user made an order, check resources sufficient first
    # TODO: 3. Ask for payment, process coins
    # TODO: 4. check if transaction successful
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)  # MenuItem object
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # TODO: 5. make coffee by deducting resources
            coffee_maker.make_coffee(drink)
    else:
        continue
