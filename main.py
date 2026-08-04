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
    return (f"Water: {cm_resources_water}ml\n"
            f"Milk: {cm_resources_milk}ml\n"
            f"Coffee: {cm_resources_coffee}g\n"
            f"Money: ${temp_money}")

# TODO: 3. Check if resources are sufficient
def check_resources(users_choice, coffee_resources, menu_choice):
    """Takes in users input and checks if there are enough resources available for the order"""
    for key in coffee_resources:
        if key in menu_choice[users_choice]["ingredients"]:
            if coffee_resources[key] < menu_choice[users_choice]["ingredients"][key]:
                print(f"Sorry there is not enough {key}")
                break
            coffee_resources[key] -= menu_choice[users_choice]["ingredients"][key]

    # this is for testing purposes to see if the resources are being allocated appropriately
    print(format_text(coffee_resources))


still_on = True

while still_on:
    # TODO: 1. Ask the user what coffee they would like
    users_drink = input("What would you like? (espresso/latte/cappuccino):").lower()

    # TODO: 2. Print report of all coffee machine resources, and turn off the machine.
    if users_drink == "off":
        still_on = False
    elif users_drink == "report":
        # need to update money 0 is being used as a temp
        format_text(resources)
    elif users_drink == "espresso":
        check_resources(users_drink, resources, MENU)
    elif users_drink == "latte":
        check_resources(users_drink, resources, MENU)
    elif users_drink == "cappuccino":
        check_resources(users_drink, resources, MENU)
        print("Please enter either 'off' or 'report'.")





