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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Ask the user what coffee they would like
def coffee_machine():
    temp_money = 0
    still_on = True
    while still_on:
        users_drink_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        # TODO: 2. Print report of all coffee machine resources.
        if users_drink_choice == "off":
            still_on = False
        elif users_drink_choice == "report":
            # need to update money 0 is being used as a temp
            print(f"Water: {resources['water']}ml\n"
                  f"Milk: {resources['milk']}ml\n"
                  f"Coffee: {resources['coffee']}g\n"
                  f"Money: ${temp_money}")

coffee_machine()



