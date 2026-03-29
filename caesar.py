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

    else:
        dec_message = input("Input the message you want to decrypt: ")
        while True:
            if dec_message.isdigit():
                print("Digit isn't allowed! ")
                dec_message = input("Input the message you want to decrypt: ")
            else:
                break
caesar_logic()