import json
import os
import sys

class User:
    def __init__(self):
        self.cookies = 500
        self.items = {
            "joker": 1,
            "shield": 1,
            "half": 1,
        }

    def get_save_path(self):
        """Return the path where user data should be saved"""
        
        # Get the folder where the user_data.json will be stored
        if getattr(sys, 'frozen', False):  # if running as a bundle
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        data_folder = os.path.join(base_path, 'data')

        # Ensure the directory exists
        os.makedirs(data_folder, exist_ok=True)

        return os.path.join(data_folder, 'user_data.json')

    def save_user_data(self):
        """Save user data to a json file"""

        user_data = {
            "cookies": self.cookies,
            "items": self.items
        }
        save_path = self.get_save_path()  # Get the correct save path
        with open(save_path, "w") as file:
            json.dump(user_data, file)

    @classmethod
    def load_user_data(cls):
        """Load user data from the json file. If the file doesn't exist, create a new user"""

        user = cls() # new instance
        save_path = user.get_save_path()  # Get the correct load path
        
        if os.path.exists(save_path):
            with open(save_path, "r") as file:
                data = json.load(file)
                user.cookies = data["cookies"]
                user.items = data["items"]
        
        return user
