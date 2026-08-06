
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
user_money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 3. Check if resources are sufficient
def check_resources(order_ingredients):
    """Takes in users input and checks if there are enough resources available for the order"""

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO: 4. process coins as inputs from the user and calculate the users value
def coin_process():
    """Takes in the menus price of the users choice and sees if the users transaction was successful"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change")
        global user_money
        user_money += money_received
        return True
    else:
        print("Sorry there is not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")

still_on = True

while still_on:
    # TODO: 1. Ask the user what coffee they would like
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Print report of all coffee machine resources, and turn off the machine.
    if choice == "off":
        still_on = False
    elif choice == "report":
        # need to update money 0 is being used as a temp
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['milk']}g")
        print(f"Money: ${round(user_money, 2)}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = coin_process()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
