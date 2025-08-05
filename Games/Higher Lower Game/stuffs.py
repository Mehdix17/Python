import art
import random

def get_versus(data):
    new_a = 0
    new_b = 0
    while new_a == new_b:
        new_a, new_b = random.choices(data, k=2)
    return new_a, new_b 

def update_versus(a, b, data):
    new_a = b
    data.remove(a)
    try:
        new_b = random.choice([d for d in data if d != b])
    except:
        print("\n" + "*" * 35 + " Congratulation, you won all the battles 👑 " + "*" * 35)

        new_b = None # the value doesn't matter
        data.clear() # clear the list so data == False in order to exit the while loop
    return new_a, new_b, data 

def display_versus(a, b):
    print(art.versus_msg.format( "", "",
                                "", art.versus_msg_list[0],
                                a['name'], art.versus_msg_list[1], b['name'],
                                "", art.versus_msg_list[2],
                                a['description'], art.versus_msg_list[3], b['description'],
                                "", art.versus_msg_list[4],
                                a['country'], art.versus_msg_list[5], b['country'],
                                ))

def get_answer(a, b):
    print("\nWho has more followers ?")
    while True:
        answer = input("\nType 'A' or 'B' : ").lower()
        if answer not in ("a", "b"):
            print("\n💡 Please answer by 'A' or 'B'")
        else:
            if answer == "a":
                return a["follower_count"] > b["follower_count"]            
            else: # answer == "b"
                return a["follower_count"] < b["follower_count"]            

def play_again():
    print("\nDo you want to play a new game ? (Y|N)")
    while True:
        answer = input("\nYour answer : ").lower()
        if answer not in ("yes", "no", "y", "n"):
            print("\n💡 Please answer by 'yes' or 'no'")
        else:
            if answer in ("yes", "y"):
                print(art.new_game_msg)
                return False
            else:
                print(art.game_over_msg)
                return True
