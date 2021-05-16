from menu import MENU


# TODO: 3. Print report
def res_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"${money}")


# TODO: 4. Check for sufficient resources
def resource_check(coffee_type):
    resource_list = ['water', 'milk', 'coffee']
    resource_attendance = 0
    missing_resource = []

    for objects in resource_list:
        if resources[f'{objects}'] > MENU[coffee_type]['ingredients'][objects]:
            resource_attendance += 1
        else:
            missing_resource.append(objects)

    if resource_attendance == 3:
        return True
    else:
        return missing_resource


# TODO: 5a. Method that asks user to input coins. Returns list with amount of coins.
def coin_input():
    coin_names = ['quarters', 'dimes', 'nickles', 'pennies']
    print("Please insert coins.")
    coin_purse = []
    for coins in coin_names:
        user_val = False
        while user_val == False:
            amount = input(f"How many {coins} will you use? ")
            user_val = amount.isnumeric()
        amount_as_float = float(amount)
        coin_purse.append(amount_as_float)
    return coin_purse


# TODO: 5. Method to add currency.
def add_coins(coin_list):
    money_total = (coin_list[0] * .25) + (coin_list[1] * .1) + (coin_list[2] * .05) + (coin_list[3] * .01)
    money_total = round(money_total, 2)
    return money_total


# TODO: 6. Check for correct amount of currency. Refund money for insufficient funds. Return change to user when
#  transaction is successful.
def currency_check(coffee_type, user_money):
    coffee_price = MENU[coffee_type]['cost']
    if user_money >= coffee_price:
        balance = round(user_money - coffee_price, 2)
        return balance
    else:
        return False


# TODO: 7. Make coffee
def make_coffee(coffee_type):
    resource_list = ['water', 'milk', 'coffee']
    for items in resource_list:
        resources[f'{items}'] -= MENU[coffee_type]['ingredients'][items]
    global money
    money += MENU[coffee_type]['cost']
    print(f"Here is your {coffee_type}. Enjoy!")


####################################################
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# probably where the real code will start
machine_on = True

money = 0
# TODO: 1. User input and user input verification
# TODO: 2. Make the "off" prompt
while machine_on:
    machine_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if machine_input == 'off':
        machine_on = False
    elif machine_input == 'report':
        res_report()
    elif machine_input == 'cappuccino' or machine_input == 'latte' or machine_input == 'espresso':
        check_outcome_1 = resource_check(machine_input)
        if check_outcome_1 == True:
            wallet = coin_input()
            wallet_total = add_coins(wallet)
            check_outcome_2 = currency_check(machine_input, wallet_total)
            # This works, I assume, because check_outcome isn't "False." Check outcome either returns a number or "False"
            if check_outcome_2:
                print(f"Thank you. Here is ${check_outcome_2} back in change.")
                make_coffee(machine_input)
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            for missing_item in check_outcome_1:
                print(f'Sorry, there is not enough {missing_item}.')
    else:
        print("Uh oh! Did you spell something wrong?")
