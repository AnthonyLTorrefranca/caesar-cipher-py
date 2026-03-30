alphabets = "abcdefghijklmnopqrstuvwxyz"
print("Welcome to caesar cipher game where we encrypt or decrypt your message to specific number!")

def caesar_logic():
    def encrypt():
        enc_msg = input("Input the msg you want to encrypt: ")
        while True:
            try:
                num_shift = int(input("Number to shift the message: "))
                break
            except ValueError:
                print("Try again, this time use numeric.")
        for char in enc_msg:
            if char in alphabets:
                new_index = (alphabets.index(char) + num_shift) % 26
                shifted_ltr = alphabets[new_index]
                print(f"{shifted_ltr}", end="")
            else:
                print(char, end="")

    def decrypt():
        dec_msg = input("Input the msg you want to decrypt: ")
        while True:
            try:
                num_shift = int(input("Input how many unshift you want your msg: "))
                break
            except ValueError:
                print("Try again, this time use numeric.")
        for char in dec_msg:
            new_index = (alphabets.index(char) - num_shift) % 26
            shifted_ltr = alphabets[new_index]
            print(f"{shifted_ltr}", end="")


    while True:
        user_choice = input("Choose between enc for encryption and dec for decryption: ").lower()
        match user_choice:
            case "enc":
                encrypt()
                break
            case "dec":
                decrypt()
                break
            case _:
                print(f"{user_choice} is invalid! either enc or dec only.")

caesar_logic()
