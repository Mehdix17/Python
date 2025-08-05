import constants as cst
from question import Question
from random import sample
import art

def get_user_choice():
    print(art.logo)
    print(art.menu_msg)
    
    while True:
        user_choice = input("\nWhat do you want to do ? : ").lower()
        
        if user_choice not in ('play', 'shop', 'exit'):
            print("\n💡 Choose one of these options : 'play', 'shop' or 'exit'")
        
        else:
            return user_choice

#------------------------------------------------------------ Shop ------------------------------------------------------------

def open_shop(user):
    print(art.shop_menu_msg)
    while True:
        user_items = [str(item).zfill(2) for item in user.items.values()]
        print(art.shop_menu.format(str(user.cookies).zfill(4), *user_items)) # print user inventory and price of items
        
        while True:
            item = input("\nItem : ").lower() # get user input
            if item not in ("half", "shield", "joker", "back"):
                print("\n💡 Choose one of these options : 'half', 'shield', 'joker' or 'back'")
            else:
                break

        if item == "back": # return to main menu
            return
        
        else:

            if user.items[item] == 99: # user can stack up to 99 units per item
                print(f"\nYou can't stack more than 99 {item} ❌")
            
            else:
                item_price = cst.item_prices[item] # get the item price
                
                if user.cookies >= item_price: # enough cookies
                    user.cookies -= item_price
                    user.items[item] += 1
                    print(f"\n 1 {item} has been added to your inventory ✅")
                
                else:
                    print("\nNot enough cookies ❌")

#--------------------------------------------------------- Mode selection ---------------------------------------------------------

def set_mode():
    print(art.modes_msg)
    while True:
        mode = input("\nIn which mode you want to play ? : ").lower()
        
        if mode not in ("chill", "normal", "hard", "back"):
            print("\n💡 Choose one of these options : 'chill', 'normal', 'hard', 'back'")
        
        else:
            cst.user_questions_dict = {key: 0 for key in cst.user_questions_dict} # delete all selected questions
            return mode

#-------------------------------------------------------- Theme selection ----------------------------------------------------------

def set_themes():

    user_questions_dict = cst.user_questions_dict

    def get_theme():
        """get the theme name, random or back"""

        print(art.themes_msg.format(" ", cst.theme_list[0],  cst.theme_list[1],
                                    " ", cst.theme_list[2],  cst.theme_list[3],
                                    " ", cst.theme_list[4],  cst.theme_list[5],
                                    " ", cst.theme_list[6],  cst.theme_list[7],
                                    " ", cst.theme_list[8],  cst.theme_list[9],
                                    " ", cst.theme_list[10], cst.theme_list[11]))
        print(art.themes_menu)
        
        while True:
            theme = input("\nInput : ").lower()
            
            try: # check if the input is a number
                theme = int(theme)
                if theme not in cst.themes_dict.keys():
                    print("\n💡 Type a number between 1 and 12")
                else:
                    return cst.themes_dict[theme]
            
            except: # the input is not a number, check if it's 'random' or 'back'
                if theme not in tuple(cst.themes_dict.values()) and theme not in ("random", "back"):
                    print("\nInvalid theme name ❌")
                else:
                    return theme
                
    def get_questions(theme):
        """get the number of questions user wants to play with """

        while True:
            
            try: # check if the input is a number
                user_questions_num = int(input(f"\n{theme.capitalize()} theme contains {theme_questions_num} questions, how many do you want to play with ? : "))
                
                if user_questions_num > theme_questions_num:
                    print(f"\n{theme.capitalize()} theme only contains {theme_questions_num} ❌")
                
                elif user_questions_num < 0:
                    print(f"\n💡 Type a positive number")
                
                else: # user typed a valid number
                    user_questions_dict[theme] = user_questions_num # save it
                    print(f"\n{user_questions_num} questions added from {theme.capitalize()} theme ✅")
                    break             
            
            except: # input is not a number
                print(f"\n💡 Type a number between 0 and {theme_questions_num}")
                                
    while True: # main loop
        theme = get_theme() # start by getting the theme
        
        if theme == "back": # go back to mode selection
            return "back"
        
        elif theme == "random": # select n questions randomly
            cst.user_questions_dict = {key: 0 for key in cst.user_questions_dict} # delete all selected questions
            quizz_len = len(cst.all_quiz_questions)
            
            while True:
                
                try: # check if input is a number
                    n = int(input(f"\nType the number of questions (between 1 and {quizz_len}) : "))
                    
                    if n not in range(1, quizz_len+1): # invalid number
                        print(f"\n💡 Type a number between 1 and {quizz_len}")
                    
                    else: # valid number
                        print(f"\n{n} questions added ✅")
                        break
                
                except: # input is not a number
                    print("\nInvalid input ❌")
            
            sampled_questions = sample(cst.all_quiz_questions, k=n) # choose randomly n questions from all themes
            
            for _, category in sampled_questions:
                user_questions_dict[category] += 1 # associate each question to its theme

            return user_questions_dict # return the dictionary theme/number_of_questions
        
        else: # user typed one of the 12 themes

            theme_questions_list = cst.quiz_questions_dict[theme] # list of questions of the selected theme
            theme_questions_num = len(theme_questions_list) # number of questions of the selected theme

            if not user_questions_dict[theme]: # user has not yet selected questions from this theme
                get_questions(theme) # get number of questions
            
            else: # user has already selected some questions from this theme
                num = str(user_questions_dict[theme]).zfill(2) # number of selected questions from this theme
                print(art.theme_already_selected_msg.format(num)) # display a different menu when a theme has already selected questions

                while True:
                    edit_or_delete = input("\nWhat do you want to do ? : ").lower() # edit or delete number of questions ?
                    
                    if edit_or_delete not in ("edit", "delete", "back"): # invalid input
                        print("\n💡 Choose one of these options : 'edit', 'delete' or 'back'")
                    
                    else:
                        if edit_or_delete == "back": # go back to theme selection
                            return "back"
                        else:
                            break

                if edit_or_delete == "edit": # update number of questions
                    get_questions(theme) 
                
                else: # delete all selected questions from this theme
                    user_questions_dict[theme] = 0
                    print("\nAll selected questions from this theme have been deleted ✅")

        while True:
            add_questions = input("\nDo you want to add questions from other themes ? (Y|N) : ").lower()
            
            if add_questions not in ("yes", "no", "y", "n"): # ivalid input
                print("\n💡 Answer by 'yes' or 'no'")
            
            elif add_questions in ("no", "n"): # no more questions
                
                if sum(user_questions_dict.values()) > 0: # check if at least one question has been selected
                    return user_questions_dict # return the dictionary theme/number_of_questions
                
                else: # no question selected --> go back to theme selection
                    print("\nNo question selected ❌")
                    print("\n💡 Select at least one to start playing")
                    break

            else: # yes add more questions --> go back to theme selection
                break

def display_summary(questions_dict):
    """display a summary of all questions selected from the 12 themes"""

    selected = list(questions_dict.values()) # list of questions selected from the 12 themes
    max = cst.max_number_question_theme_list # list of the max number of questions for each theme
    print(art.summary_msg.format(cst.theme_list[0],  selected[0], max[0], cst.theme_list[1], selected[1], max[1],
                                 cst.theme_list[2],  selected[2], max[2], cst.theme_list[3], selected[3], max[3],
                                 cst.theme_list[4],  selected[4], max[4], cst.theme_list[5], selected[5], max[5],
                                 cst.theme_list[6],  selected[6], max[6], cst.theme_list[7], selected[7], max[7],
                                 cst.theme_list[8],  selected[8], max[8], cst.theme_list[9], selected[9], max[9],
                                 cst.theme_list[10], selected[10], max[10], cst.theme_list[11], selected[11],max[11],))
    while True:
        user_choice = input("\nWhat do you want to do ? : ").lower() # start the game or go back ?
        if user_choice not in ("start", "back"):
            print("\n💡 Choose one of these options : 'start' or 'back'")
        else:
            return user_choice

#------------------------------------------------ Create question bank ------------------------------------------------------------

def create_question_bank(questions_dict):
    question_bank = [] # list of all questions in the game
    
    for theme, questions_num in questions_dict.items(): # iterate over the theme/number_of_questions dict
        
        if questions_num: # if there is at least one question selected from this theme
            questions = sample(cst.quiz_questions_dict[theme], k=questions_num) # a list of k questions randomly selected
            
            for question in questions: # create an object for each question
                new_question = Question(question["text"], 
                                        question["answers"], 
                                        question["right_answer"], 
                                        question["points"])
                question_bank.append(new_question) # append the object to the question bank

    return question_bank

#------------------------------------------------------ Display statistics ------------------------------------------------------------

def display_stats(game):
    """display game statistics at the end of the game"""

    answered_questions = game.right_answers + game.wrong_answers # get number of answered questions
    
    try:
        win_rate = round(game.right_answers/answered_questions*100, 2) # calculate the win rate
    
    except:
        win_rate = 0 # the special case where user typed 'exit' before answering the first question 
    
    if game.mode == "chill": # don't show earned cookies in chill mode
        print(art.chill_stats_msg.format(game.right_answers, game.wrong_answers, win_rate))
    
    else: # show all stats
        print(art.stats_msg.format(game.right_answers, game.wrong_answers, win_rate, game.score))

#--------------------------------------------------------- Play again ? ------------------------------------------------------------

def play_again():
    print("\nDo you want to play a new game ? (Y|N)") # yes or no ?
    while True:
        answer = input("\nYour answer : ").lower()
        
        if answer not in ("yes", "no", "y", "n"): # invalid answer
            print("\n💡 Please answer by 'yes' or 'no'")
        
        else:
            
            if answer in ("yes", "y"): # user wants to play a new game, asks if he wants to play with the same questions or not
                
                while True:
                    same_question = input("\nWith same questions ? (Y|N) : ").lower()
                    
                    if same_question not in ("yes", "no", "y", "n"): # invalid answer
                        print("\n💡 Please answer by 'yes' or 'no'")                
                    
                    else:
                        break

                print(art.new_game_msg) # new game !
                
                if same_question in ("yes", "y"):
                    return True, True # play again, with same questions
                
                else:
                    cst.user_questions_dict = {key: 0 for key in cst.user_questions_dict} # delete all selected questions
                    return True, False # play again, not with the same questions
            
            else: # user doesn't want to play a new game --> go back to main menu
                return False, False
