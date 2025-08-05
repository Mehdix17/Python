# if you want to add a question to a specific theme follow this format :

#----------------------------------------- adding an exact questions -----------------------------------------

# {"text": "your question ...", 
# "answers": [],
# "right_answer": right_answer
# points: 3,
# },

#----------------------------------------- adding a two options questions -----------------------------------------

# {"text": "your question ...", 
# "answers": [right_answer, wrong_asnwer],
# "right_answer": right_answer
# points: 1,
# },

#----------------------------------------- adding a four options questions -----------------------------------------

# {"text": "your question ...", 
# "answers": [right_answer, wrong_asnwer1, wrong_asnwer2, wrong_asnwer3],
# "right_answer": right_answer
# points: 2,
# },

# you can also delete a question by deleting its dictionary

# all answers must be in lowercase

# to create a .exe file :
# install pyinstaller : pip install pyinstaller
# then type this command :pyinstaller --onefile --icon=data\icon.ico --add-data "data;data" --add-data "themes;themes" main.py
