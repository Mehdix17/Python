from random import shuffle, sample
from art import items_menu

class Game:

    def __init__(self, question_bank, mode, user):
        shuffle(question_bank)
        self.question_bank = question_bank
        self.question_number = 0
        self.mode = mode
        self.user = user
        self.score = 0
        self.right_answers = 0
        self.wrong_answers = 0
        self.shield = 0
        self.stop = False

        if self.mode != "hard": # item not allowed in hard mode
            print("\n💡 Type 'item' to use an item if you have")
            self.lives = 3

        else: # hard mode
            self.lives = 1

        if self.mode != "chill": # no cookies to earn in chill mode
            print("\n💡 You can leave the game at any time by typing 'exit', but you will lose all your cookies")
        
        else:
            print("\n💡 You can leave the game at any time by typing 'exit'")

        print("\n" + "*"*134) # separation


    def next_question(self):
        """ask question and return user answer"""

        question = self.question_bank[self.question_number] # get the i question from the question bank
        self.question_number += 1 # increase i
        tempo_dict = {} # dictionary option_number/option (option = potential answer)     

        while True:

            print(f"\nQ{self.question_number}) {question.text}") # ask the question
            
            if question.points != 3: # display options if it's not an exact question
                answers_num = range(1, len(question.answers)+1)
                
                for i, j in zip(answers_num, question.answers): # display the options
                    print(f"\n{i}) {j.title()}")
                    tempo_dict[i] = j # associate each option number to its option
        
            while True:

                if question.points != 3: # not an exact question
                    user_answer = input("\nType an answer or its associated number : ").lower()

                    if user_answer not in question.answers and user_answer not in ("item", "exit"):
                        
                        try:
                            index = int(user_answer) # check if user typed a number associated to an answer
                            if index not in tempo_dict.keys():
                                print("\nInvalid number ❌")
                            else:
                                user_answer = tempo_dict[index] # get the associated answer
                                break                   
                        except:
                            print("\nInvalid answer ❌")
                    
                    else:
                        break # user typed either a valid answer, 'item' or 'exit'
                    
                else: # exact questions --> just get the answer 
                    user_answer = input("\nYour answer : ").lower()
                    break

            if user_answer == "item": # display items menu if it's not in hard mode
                
                if self.mode == "hard":
                    print("\nNo item allowed in hard mode ❌")
                
                else:
                    self.display_items(question)
            
            elif user_answer == "exit":
                
                if self.mode == "chill": # no cookies to lose in chill mode
                    msg = "\n💡 Are you sure ? (Y|N) : "
                else:
                    msg = "\n💡 Are you sure ? all cookies will be lost ! (Y|N) : "
                
                while True:
                    user_input = input(msg).lower() # get user answer
                    
                    if user_input not in ("yes", "no", "y", "n"):
                        print("\n💡 Answer by 'yes' or 'no'")
                    
                    elif user_input in ("yes", "y"): # reset lives, shield and stop the game
                        self.lives = 0
                        self.shield = 0
                        self.stop = True
                        return 0
                    
                    else: # no --> go back to the question
                        break
            
            else: # user typed a valid answer --> calculate and return points    points = 0 --> wrong answer
                points = self.calcul_points(user_answer, question)             # points in (1, 2, 3) --> right answer
                return points


    def display_items(self, question):
        """display the items menu when user type 'item'"""

        user_items = [str(item).zfill(2) for item in self.user.items.values()] # get user items
        print(items_menu.format(*user_items)) # display items menu
        
        while True:
            item = input("\nWhat item do you want to use ? : ").lower()
            
            if item not in ("joker", "shield", "half", "back"): # invalid input
                print("\n💡 Choose one of these options : 'joker', 'shield', 'half' or 'back'")
            
            else:
                break
        
        if item == "back": # go back to the question
            return
        
        elif self.user.items[item] == 0: # item not available
            print("\nYou don't have this item ❌" + " "*89 + self.display_user_lives())
        
        else: # item available

            if item == "joker":
                print(f"\nThe right answer is : {question.right_answer.title()} ✅")
                self.user.items[item] -= 1
            
            elif item == "shield":
                
                if self.shield == 3: # user can't stack more than 3 shields
                    print("\nYou can't stack more than 3 shields ❌" + " "*77 + self.display_user_lives())
                
                else:
                    self.shield += 1
                    print("\nShield successfully added ✅" + " "*87 + self.display_user_lives())
                    self.user.items[item] -= 1 # update user inventory

            else: # half
                
                if question.points == 2: # it's a 4-option question
                    wrong_answers_list = sample([answer for answer in question.answers if answer != question.right_answer], k=2)
                    question.answers = list(set(question.answers) - set(wrong_answers_list)) # eliminate 2 wrong answers
                    print("\n2 wrong answers have been eliminated ✅" + " "*77 + self.display_user_lives())
                    self.user.items[item] -= 1 # update user inventory
                
                else:
                    print("\n💡 'Half' item only works on 4 options questions"  + " "*69 + self.display_user_lives())            
            

    def calcul_points(self, user_answer, question):
        """return question points based on user answer"""

        if user_answer == question.right_answer:
            self.right_answers += 1 # increment the right_answers counter
            return question.points # return question points (1, 2 or 3)
        
        else:
            self.wrong_answers += 1 # increment the wrong_answers counter
            return 0 

    def still_has_questions(self):
        """check if there are still any questions in the game"""
        return self.question_number != len(self.question_bank)
    
    def display_user_lives(self):
        """display user lives and shield"""
        space = 3 - self.shield
        return "  "*space + "🛡️ "*self.shield + "❤️ "*self.lives
