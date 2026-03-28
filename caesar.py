alphabets = "abcdefghijklmnopqrstuvwxyz"
print("Welcome to caesar cipher game where we encrypt or decrypt your message to specific number!")

def caesar_logic():
    def encrypt():
        enc_msg = input("Input the msg you want to encrypt: ")
        print(f"Encrypting the message...")

    def decrypt():
        dec_msg = input("Input the msg you want to decrypt: ")
        print(f"Decrypting the message...")
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

        # if user_choice not in ["enc", "dec"]:
        #     print(f"The {user_choice!r} is not in the choices!")
        #
        # if user_choice == "enc":
        #     print("Good! You chose to encrypt a msg.")
        #     shifted_number = input("Provide number for the msg to shift: ")
        #     while not shifted_number.isdigit():
        #         print("Numerical only!")
        #     if shifted_number.isdigit():
        #         print(f"shifted number is {shifted_number}")
        #
        # if user_choice == "dec":
        #     print("Good! You chose to decrypt a msg.\n")
        #     unshifted_number = input("Input a number for the unshift method: ")
        #     while not unshifted_number.isdigit():
        #         print("Pls enter a valid unshift number: \n")
        #         unshifted_number = input("Input a number for the unshift method: ")

    else:
        dec_message = input("Input the message you want to decrypt: ")
        while True:
            if dec_message.isdigit():
                print("Digit isn't allowed! ")
                dec_message = input("Input the message you want to decrypt: ")
            else:
                break
caesar_logic()