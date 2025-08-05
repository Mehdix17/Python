from art import logo
import stuffs as stf

power_switch = True
stf.set_menu()
print(logo)

while power_switch:
    user_input = stf.get_user_input()

    if user_input == "coffee":
        stf.make_coffee()
    
    elif user_input == "manage":
        stf.manage_ressources()

    elif user_input == "money":
        stf.check_password(stf.withdraw_money)
    
    elif user_input == "off":
        print("\nMachine turned off ⛔")
        power_switch = False
