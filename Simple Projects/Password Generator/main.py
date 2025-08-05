import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")
nr_letters = int(input("\nHow many letters would you like in your password ? : "))
nr_symbols = int(input(f"\nHow many symbols would you like ? : "))
nr_numbers = int(input(f"\nHow many numbers would you like ? : "))

pwd_letters = random.choices(letters, k=nr_letters)
pwd_numbers = random.choices(numbers, k=nr_numbers)
pwd_symbols = random.choices(symbols, k=nr_symbols)

pwd_list = pwd_letters + pwd_numbers + pwd_symbols
random.shuffle(pwd_list)

pwd = "".join(pwd_list)

print(f"\nYour password is : {pwd}")
