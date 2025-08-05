import utils
import art
from user import User
from game import Game

user = User.load_user_data() # load user data (create new user if data doesn't exist)

while True:
    user_choice = utils.get_user_choice() # main menu

    if user_choice == "exit": # exit the game
        print(art.goodbye_msg)
        break

    elif user_choice == "shop": # open the shop
        utils.open_shop(user)
        user.save_user_data() # save data after each shop visit
    
    else: # play a game
        play_again = True # assume that user want to play again after this game

        while True:
            mode = utils.set_mode() # set the game mode and delete selected questions from previous game

            if mode != "back":
                while play_again: # loop to play again
                    questions_dict = utils.set_themes() # user selects n questions from 12 themes

                    if questions_dict != "back":
                        start_game = utils.display_summary(questions_dict) # display a summary of all selected questions

                        if start_game != "back":
                            question_bank = utils.create_question_bank(questions_dict) # put all selected questions in a bank
                            same_questions = True # assume that user want to play a new game with same questions

                            while same_questions: # loop to play a new game with same questions
                                game = Game(question_bank, mode, user)

                                while game.still_has_questions() and game.lives: # game loop
                                    points = game.next_question() # ask question and return question points, 0 if it's a wrong answer

                                    if game.stop: # user typed 'exit' --> stop the game
                                        break

                                    else:

                                        if points: # right answer
                                            if mode != "hard":
                                                game.score += points
                                            else:
                                                game.score += points*2 # double points in hard mode
                                            print("\n" + "*"*51 + f" You got it right, +{points} points ✅ " + "*"*51)
                                        
                                        else: # wrong answer
                                            if mode != "chill":
                                                if game.shield:
                                                    game.shield -= 1 # user loses 1 shield
                                                else:
                                                    game.lives -= 1 # user loses 1 life
                                            print("\n" + "*"*59 + " That's wrong ❌ " + "*"*58)
                                        
                                        if mode != "chill": # display lives if not in chill mode
                                            print("\n" + " "*56 + f"Current cookies : {game.score} 🍪" + " "*38 + game.display_user_lives())
                                        
                                        else:
                                            print("\n" + " "*58 + f"Current score : {game.score}")

                                if not game.lives: # user lost or typed 'exit'
                                    game.score = 0
                                    print(art.game_over_msg)

                                elif not game.still_has_questions(): # no more questions --> user won
                                    user.cookies += game.score # user gets his earned cookies
                                    if user.cookies > 9999:
                                        user.cookies = 9999 # user can stack up to 9999 cookies
                                        print("\nYou reached max cookies : 9999 🍪")
                                    print(art.win_msg)

                                utils.display_stats(game) # display game stats

                                play_again, same_questions = utils.play_again() # ask user if he want to play a new game
                                user.save_user_data() # save data after each game
                             
                        else:
                            continue # go back to theme selection

                    else:
                        break # break the play_again loop (when user doesn't want to play a new game)
            
            if mode == "back": # go back to main menu (when user is in the mode selection menu)
                break

            if questions_dict == "back": # go back to mode selection
                questions_dict = None
                continue 
            
            break # go back to main menu (when user doesn't want to play a new game)
