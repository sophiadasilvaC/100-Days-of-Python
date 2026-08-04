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

def format_text(cm_resources):
    """Formats the resources data into a printable format"""
    cm_resources_water = cm_resources["water"]
    cm_resources_milk = cm_resources["milk"]
    cm_resources_coffee = cm_resources["coffee"]
    temp_money = 0
    return (f"Water: {cm_resources_water}ml\n "
            f"Milk: {cm_resources_milk}ml\n "
            f"Coffee: {cm_resources_coffee}g"
            f"Money: ${temp_money}")

# TODO: 3. Check if resources are sufficient
def check_resources():
    return


# TODO: 1. Ask the user what coffee they would like
def coffee_machine():
    still_on = True
    while still_on:
        users_drink_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        # TODO: 2. Print report of all coffee machine resources.
        if users_drink_choice == "off":
            still_on = False
        elif users_drink_choice == "report":
            # need to update money 0 is being used as a temp
            format_text(resources)


coffee_machine()



