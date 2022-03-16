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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO: 1. Keep asking user their choice of drink after every time action has completed
while True:
    user_input = input(" What would you like? (espresso/latte/cappuccino):  ").lower()
    # TODO: 2. If user_input == off, break the while loop. elif user_input == report,
    #  display current resources and continue the loop
    if user_input == 'off':
        break
    # Print report
    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        continue

    # TODO: 3. after user choose their drink, check if each current resources >= each ingredients.
    #  If enough ask user for money. else if any resources not enough, tell user. and continue loop
    if resources["water"] >= MENU[user_input]["ingredients"]["water"] and \
            resources["milk"] >= MENU[user_input]["ingredients"]["milk"] and \
            resources["coffee"] >= MENU[user_input]["ingredients"]["coffee"]:
        # TODO: 4. Process coins; ask user to insert coins and how many quantities for each coins
        # TODO: 5. calculate total payment, multiply the quantities with the coins value, output decimal
        #  Penny: 0.01, Nickel: 0.05, Dime: 0.10, Quarter: 0.25
        print("Please insert coins.")
        total_payment = int(input("how many quarters?: ")) * 0.25
        total_payment += int(input("how many dimes?: ")) * 0.1
        total_payment += int(input("how many nickels?: ")) * 0.05
        total_payment += int(input("how many pennies?: ")) * 0.01
    elif resources["water"] < MENU[user_input]["ingredients"]["water"]:
        print(f"Sorry there is not enough {'water'}.")
        continue
    elif resources["milk"] < MENU[user_input]["ingredients"]["milk"]:
        print(f"Sorry there is not enough {'milk'}.")
        continue
    else:
        print(f"Sorry there is not enough {'coffee'}.")
        continue

    # TODO: 6. create a function to Check transaction. if total payment >= cost, add the cost to the resources[money]
    #  and minus cost to offer change to user. print the change amount
    if total_payment >= MENU[user_input]["cost"]:
        resources['money'] += MENU[user_input]["cost"]
        balance = round(total_payment - MENU[user_input]["cost"], 2)
        print(f"Here is ${balance} in change.")
    else:
        # TODO: 8. if no, refund and tell use it's not enough and continue loop
        print(f"Sorry that's not enough money. Money refunded.")
        continue

    # TODO: 7. Make coffee: Deduct the ingredients from the resources and tell user here is your 'drink'. continue loop
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
    print(f"Here is your {user_input} ☕. Enjoy!")

