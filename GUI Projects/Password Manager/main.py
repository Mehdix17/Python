import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_random_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    random_password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save(*event):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Empty fields")

    else:
        is_ok = messagebox.askokcancel(title="Title", message="These are the details entered :\n"+
                            f"Website : {website}\n"+
                            f"Email : {email}\n"+
                            f"Password : {password}\n")
        if is_ok:
            
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            
            else:
                data.update(new_data)  
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            
            finally:
                website_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                website_entry.focus()

# ------------------------- SEARCH WEBSITE ---------------------------- #

def search_website():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Label
website_label = tk.Label(text="Website :")
email_label = tk.Label(text="Email / Username :")
password_label = tk.Label(text="Password :")

# Entries
website_entry = tk.Entry(width=55)
website_entry.focus()
email_entry = tk.Entry(width=80)
email_entry.insert(0, "example@gmail.com")
password_entry = tk.Entry(width=55)

# Buttons
generate_password_button = tk.Button(text="Generate Password",  width=20, command=generate_random_password)
search_button = tk.Button(text="Search", width=20, command=search_website)
add_button = tk.Button(text="Add", width=44, command=save)

# Packing
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, pady=2, padx=2)
search_button.grid(row=1, column=2, pady=12, padx=2)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2, pady=2, padx=2)

password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, pady=2, padx=2)
generate_password_button.grid(row=3, column=2, pady=12, padx=2)

add_button.grid(row=4, column=1, columnspan=2, pady=2)

# Bidings
window.bind('<Return>', save)

window.mainloop()
