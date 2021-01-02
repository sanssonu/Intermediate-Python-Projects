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

pennies = 0
nickles = 0
dimes = 0
quarters = 0
flag = "n"


# TODO: Print a report of all coffee machine resources.
def print_resources(money):
    """A report that shows the current resource values."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Profit: ${money}")


# TODO: Check resources available for the coffee.
def check_resources(coffee_ingredients):
    """Check if there are enough resources available to make the coffee."""
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: Insert coins.
def insert_coins():
    """To insert the coins from user."""
    global pennies
    global nickles
    global dimes
    global quarters

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))


# TODO: Process the coins.
def do_transaction(coffee_cost):
    """Calculate the monetary value of the coins inserted.
    If user entered money more than coffee's price, return them the change.
    If user didn't enter enough money, refund it."""

    users_money = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)

    if users_money > coffee_cost:
        change = round(users_money - coffee_cost, 2)
        print(f"Here is ${change} in change.")
    if users_money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")


# TODO: Deduct resources.
def deduct(coffee_ingredients):
    """Deduct resources from the list."""
    global resources
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]


profit = 0
should_stop = False
while not should_stop:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "off":
        should_stop = True
    elif coffee == "report":
        print_resources(profit)
    else:
        enough_resources = check_resources(MENU[coffee]["ingredients"])

        if enough_resources:
            insert_coins()
            do_transaction(MENU[coffee]["cost"])
            profit += MENU[coffee]["cost"]
            deduct(MENU[coffee]["ingredients"])
            print(f"Here is your {coffee} ☕ Enjoy!")
