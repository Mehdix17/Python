from ressources import machine_resources, machine_password
from art import welcome_msg, menu_msg, ressources_msg, add_ressource_msg
from ressources import *

def set_menu():
    global menu_msg
    coffee_names = list(MENU.keys())
    coffee_prices = [MENU[coffee]['cost'] for coffee in coffee_names]

    menu_msg = menu_msg.format(
        coffee_names[0].capitalize(), coffee_prices[0],
        coffee_names[1].capitalize(), coffee_prices[1],
        coffee_names[2].capitalize(), coffee_prices[2],
        coffee_names[3].capitalize(), coffee_prices[3],
        coffee_names[4].capitalize(), coffee_prices[4],
        coffee_names[5].capitalize(), coffee_prices[5],)

def get_user_input():
    print(welcome_msg)
    while True:
        user_input = input("\nWhat would you like to do ? : ").lower()
        if user_input not in ("coffee", "manage", "money", "off"):
            print("\nInvalid input ❌")
        else:
            return user_input

#--------------------------------------------------------- Make coffee ---------------------------------------------------------

def make_coffee():
    print(menu_msg)
    print("What kind of coffee would you like ?")
    
    while True:
        code = input("\nType the coffee name or the corresponding code : ").lower()
        try:
            code = int(code)
            if code not in range(1,7):
                print("\nInvalid code ❌")
            else:
                break
        except:
            if code in coffee_codes.values():
                code = [key for key, value in coffee_codes.items() if value == code][0]
                break
            else:
                print("\nInvalid name ❌")

    coffee = coffee_codes[code]
    enough_ressources = check_ressources(coffee)

    if enough_ressources:
        coffee_cost = MENU[coffee]["cost"]
        user_money = insert_money()
        enough_money = check_money(user_money, coffee_cost)

        if enough_money:
            print(f"\nHere is your {coffee} ☕ Enjoy!")
            update_ressources(coffee, coffee_cost)

def check_ressources(coffee):
    coffee_ingredients = MENU[coffee]["ingredients"].items()
    for (ingredient, quantity), machine_quantity in zip(coffee_ingredients, machine_resources.values()):
        if machine_quantity < quantity:
            print(f"\nSorry there is not enough {ingredient} ⚠️")
            return False
    return True

def insert_money():

    def get_coin_value(coin):
        while True:
            try:
                value = int(input(f"\nHow many {coin} DZD coins : "))
                if value < 0:
                    print("\nInvalid input ❌")
                else:
                    return value
            except:
                print("\nInvalid input ❌")
    
    def calcul_coins_sum():
        total_sum = 0
        for coin, value in coins_dict.items():
            total_sum += coin * value
        return total_sum
    
    for coin in coins_dict.keys():
        coins_dict[coin] = get_coin_value(coin)

    return calcul_coins_sum()

def check_money(user_money, coffee_cost):
    print(f"\nYou inserted : {user_money} DZD 🪙")
    if user_money < coffee_cost:
        print(f"\n{coffee_cost - user_money} DZD are missing, Money refunded ⚠️")
        return False
    else:
        if user_money > coffee_cost:
            print(f"\nHere is {user_money - coffee_cost} DZD in change ✅")
        return True

def update_ressources(coffee, cost):
    coffee_ingredients = MENU[coffee]["ingredients"].values()
    for quantity, machine_ingredient in zip(coffee_ingredients, machine_resources.keys()):
        machine_resources[machine_ingredient] -= quantity
    machine_resources["money"] += cost

#----------------------------------------------------------- Manage -----------------------------------------------------------

def manage_ressources():

    def add_ressources():
        while True:
            print(add_ressource_msg)
            user_input = input("\nInput : ").lower()
            
            if user_input == "back":
                return

            else:
                try:
                    user_input = int(user_input)
                    
                    if user_input not in range(1,5):
                        print("\nInvalid input ❌")
                        print("\n💡 Type '1', '2', '3', '4' or 'back'")
                    
                    else:
                        machine_resources_keys = list(machine_resources.keys())
                        ressource = machine_resources_keys[user_input - 1]

                        if machine_resources[ressource] == 1000:
                            print(f"\n{ressource} stock is already full ⚠️")
                        else:
                            print(f"\nCurrent {ressource} stock : {machine_resources[ressource]}")
                        
                            while True:
                                try:
                                    added_value = int(input("\nInput : ").lower())
                                    
                                    if added_value < 0:
                                        print("\n💡 Add a positive number")
                                    
                                    else:
                                        machine_resources[ressource] += added_value
                                        
                                        if machine_resources[ressource] >= 1000:
                                            machine_resources[ressource] = 1000
                                            print(f"\n{ressource} stock is now full ⚠️")

                                        print(f"\nUpdated {ressource} stock : {machine_resources[ressource]} ✅")
                                        break
                                
                                except:
                                    if added_value == "back":
                                        break
                                    else:
                                        print("\nInvalid input ❌")        
                except:
                    print("\nInvalid input ❌")
                    print("\n💡 Type '1', '2', '3', '4' or 'back'")
    
    while True:

        print(ressources_msg.format(" ", machine_resources["water"],
                                    " ", machine_resources["coffee"],
                                    " ", machine_resources["milk"],
                                    " ", machine_resources["chocolate"], " "))
        
        print("\nType 'back' to go back or 'add' to add ressources")
        user_input = input("\nInput : ").lower()
        
        if user_input not in ('back', 'add'):
            print("\nInvalid input ❌")
        
        else:
            if user_input == "add":
                check_password(add_ressources)
            else: # go back
                break

def check_password(function):
    while True:
        user_password = input("\nPassword : ")
        
        if user_password not in (machine_password, 'back'):
                print("\nInvalid password ❌")
                print("\n💡 You can type 'back' to go back")
        else:
            if user_password == machine_password:
                    function()
            break # break the loop in both cases

def withdraw_money():
    current_balance = machine_resources["money"]
    print(f"\nCurrent balance : {current_balance} DZD 💰")
    while True:
        try:
            withdrawal = int(input("\nHow much do you want to withdraw : "))
            if withdrawal < 0:
                print("\n💡 Type a positive number")
            elif withdrawal > current_balance:
                print("\nImpossible, insufficient balance ❌")
            else:
                break
        except:
            print("\nInvalid input ❌")
    machine_resources["money"] -= withdrawal
    new_balance = machine_resources["money"]
    print(f"\nNew balance : {new_balance} DZD 💰")
