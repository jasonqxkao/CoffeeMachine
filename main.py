MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

should_continue = True
money = 0


def check_resources(coffee_type):
    if coffee_type == "espresso":
        if resources["water"] < 50:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < 18:
            print("Sorry, there is not enough coffee.")
            return False
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
    if coffee_type == "latte":
        if resources["water"] < 200:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < 24:
            print("Sorry, there is not enough coffee.")
            return False
        if resources["milk"] < 150:
            print("Sorry, there is not enough milk.")
            return False
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            return True
    if coffee_type == "cappuccino":
        if resources["water"] < 250:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < 24:
            print("Sorry, there is not enough coffee.")
            return False
        if resources["milk"] < 100:
            print("Sorry, there is not enough milk.")
            return False
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            return True


def process_coins():
    if c:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        total = round(total, 2)
        return total
    else:
        return "should_stop"


def transaction_successful(coffee_type):
    if d == "should_stop":
        return resources
    if d < MENU[coffee_type]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    elif d >= MENU[coffee_type]["cost"]:
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["money"] += MENU[coffee_type]["cost"]
        if d > MENU[coffee_type]["cost"]:
            change = d - MENU[coffee_type]["cost"]
            change = round(change, 2)
            print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type}, Enjoy!")
        return resources


while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        should_continue = False
    elif user_input == "report":
        print(f"Water: " + str(resources["water"]) + "mL")
        print(f"Milk: " + str(resources["milk"]) + "mL")
        print(f"Coffee: " + str(resources["coffee"]) + "mL")
        print(f"Money: $" + str(resources["money"]))
    else:
        c = check_resources(user_input)
        d = process_coins()
        e = transaction_successful(user_input)









