from utils import logo, caesar

stop = False
print(logo)

while not stop:

    while True:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt : ").lower()
        if direction in ("encode", "decode"):
            break
        else:
            print("\n💡 Please answer by 'encode' or 'decode'")

    text = input("\nType your message : ").lower()
    shift = int(input("\nType the shift number : "))
    caesar(text, shift, direction)

    while True:
        answer = input("\nDo you want to continue ? (Y|N) : ").lower()
        if answer in ("no", "n"):
            stop = True
            print("\nGoodbye :)")
            break
        elif answer in ("yes", "y"):
            break
        else:
            print("\n💡 Please answer by 'yes' or 'no'")
