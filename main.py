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
#
# def format_text(cm_resources):
#     """Formats the resources data into a printable format"""
#     global user_money
#     cm_resources_water = cm_resources["water"]
#     cm_resources_milk = cm_resources["milk"]
#     cm_resources_coffee = cm_resources["coffee"]
#     return (f"Water: {cm_resources_water}ml\n"
#             f"Milk: {cm_resources_milk}ml\n"
#             f"Coffee: {cm_resources_coffee}g\n"
#             f"Money: ${user_money}")

# TODO: 4. process coins as inputs from the user and calculate the users value
def coin_process(menu_choice, user_choice):
    """Takes in the menus price of the users choice and sees if the users transaction was successful"""
    global user_money
    print("Please insert coins.")
    quarter = int(input("How many quarters?: ")) * 0.25
    dime = int(input("How many dimes?: ")) * 0.10
    nickle = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    user_total = quarter + dime + nickle + pennies
    # rounded_total = round(user_total, 2)
    print(f"You have ${round(user_total, 2)}")


    # TODO: 5. checking if the transaction was successful
    cost_of_coffee = menu_choice[user_choice]["cost"]

    if cost_of_coffee > user_total:
        print("Sorry that's not enough money. Money refunded.")
    elif cost_of_coffee == user_total:
        user_money += cost_of_coffee
    else:
        user_money += cost_of_coffee
        rounded_total = round(user_total - cost_of_coffee, 2)
        print(f"Here is ${rounded_total} dollars in change")
    # need to fix it so that money goes into
    # print(f"money: {money}")
    return user_money


# TODO: 3. Check if resources are sufficient
def check_resources(users_choice, cm_resources, menu_choice):
    """Takes in users input and checks if there are enough resources available for the order"""
    still_resources = True

    for key in cm_resources:
        if key in menu_choice[users_choice]["ingredients"]:
            if cm_resources[key] < menu_choice[users_choice]["ingredients"][key]:
                print(f"Sorry there is not enough {key}")
                still_resources = False
                break
            else:
                cm_resources[key] -= menu_choice[users_choice]["ingredients"][key]
                still_resources = True

    return still_resources
    # this is for testing purposes to see if the resources are being allocated appropriately
    print(format_text(coffee_resources))


user_money = 0
still_on = True

while still_on:
    # TODO: 1. Ask the user what coffee they would like

    users_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Print report of all coffee machine resources, and turn off the machine.

    if users_drink == "off":
        still_on = False
    elif users_drink == "report":
        # need to update money 0 is being used as a temp
        print(f"Water: {resources['water']}ml\n"
                f"Milk: {resources['milk']}ml\n"
                f"Coffee: {resources['milk']}g\n"
                f"Money: ${user_money}")
        # print(format_text(resources))
    elif users_drink == "off":
        still_on = False
    elif users_drink == "espresso" or users_drink == "latte" or users_drink == "cappuccino":
        if check_resources(users_drink, resources, MENU) and coin_process(MENU, users_drink):
                print(f"Here is your {users_drink} ☕ Enjoy!")
    else:
        print("Please enter either 'off' or 'report'.")


# Problem: 1. Does not check if there is enough coins first
# Problem: 2. Does not restart the while loop when not enough resources or not enough coins
# TODO: 6 adjust the check_resources and coin_process, check resources needs to be adjusted so that it only checks