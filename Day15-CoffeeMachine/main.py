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


def userPrompt():
    return input("What would you like? (espresso/latte/cappuccino): ")


def printReport(res, money):
    print(f"Water: {res['water']}")
    print(f"Milk: {res['milk']}")
    print(f"Coffee: {res['coffee']}")
    print(f"Money: ${money}")


def countCoins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01


def haveMats(choice, menu, res):
    if menu[choice]["ingredients"]["water"] > res["water"]:
        print("Sorry, not enough water.")
        return False
    elif menu[choice]["ingredients"]["milk"] > res["milk"]:
        print("Sorry, not enough milk.")
        return False
    elif menu[choice]["ingredients"]["coffee"] > res["coffee"]:
        print("Sorry, not enough coffee.")
        return False
    else:
        return True


def haveMoney(choice, menu, money):
    if menu[choice]["cost"] > money:
        print("Sorry, not enough money. Coins refunded.")
        return False
    else:
        return True


def transact(choice, menu, res):
    res["water"] -= menu[choice]["ingredients"]["water"]
    res["milk"] -= menu[choice]["ingredients"]["milk"]
    res["coffee"] -= menu[choice]["ingredients"]["coffee"]


userMoney = 0
machineMoney = 0
userChoice = userPrompt()
while userChoice != "off":
    if userChoice == "report":
        printReport(resources, machineMoney)
    else:
        if haveMats(userChoice, MENU, resources):
            userMoney = countCoins()
            if haveMoney(userChoice, MENU, userMoney):
                transact(userChoice, MENU, resources)
                machineMoney += MENU[userChoice]["cost"]
                if MENU[userChoice]["cost"] < userMoney:
                    change = userMoney - MENU[userChoice]["cost"]
                    print(f"Here is {change:.2f} dollars in change.")
                print(f"Here is your {userChoice}, enjoy!")
    userChoice = userPrompt()


print("Coffee machine shutting down.")
