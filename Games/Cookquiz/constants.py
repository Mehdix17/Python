from themes import *

# list of theme names
theme_list = ["Algeria ❤️", 
              "Sport ⚽", 
              "History 📜", 
              "Movies 🎬",
              "Geography 🌍", 
              "Cars 🚗", 
              "Islam 💚", 
              "Games 🎮", 
              "Tech ⚡", 
              "Food 🍔", 
              "Medicine 🩺", 
              "Animals 🦁", 
]

# dictionary theme_number_in_the_menu/theme
themes_dict = { 
    1: "algeria",
    7: "sport",
    2: "history",
    8:"movies",
    3: "geography",
    9:"cars",
    4: "islam",
    10: "games",
    5: "tech",
    11: "food",
    6:"medicine",
    12: "animals",
}

# dictionary theme/selected_questions
user_questions_dict = { 
    "algeria": 0,
    "sport": 0,
    "history": 0,
    "movies": 0,
    "geography": 0,
    "cars": 0,
    "islam": 0,
    "games": 0,
    "tech": 0,
    "food": 0,
    "medicine": 0,
    "animals": 0,
}

# dictionary theme/questions
quiz_questions_dict = { 
    "algeria": algeria.questions,
    "sport": sport.questions,
    "history": history.questions,
    "movies": movies.questions,
    "geography": geography.questions,
    "cars": cars.questions,
    "islam": islam.questions,
    "games": games.questions,
    "tech": tech.questions,
    "food": food.questions,
    "medicine": medicine.questions,
    "animals": animals.questions,
}

# the max number of question for each theme
max_number_question_theme_list = [len(question) for question in quiz_questions_dict.values()] 

# list of all questions, usefull to choose randomly n questions from the 12 themes
all_quiz_questions = [] 
for category, questions in quiz_questions_dict.items():
    for question in questions:
        all_quiz_questions.append((question, category))

# item prices in the shop
item_prices = { 
    "joker": 300,
    "shield": 200,
    "half": 100,
}
