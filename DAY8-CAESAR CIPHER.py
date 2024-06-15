alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("""
 ██████  █████  ███████ ███████  █████  ██████       ██████ ██ ██████  ██   ██ ███████ ██████  
██      ██   ██ ██      ██      ██   ██ ██   ██     ██      ██ ██   ██ ██   ██ ██      ██   ██ 
██      ███████ █████   ███████ ███████ ██████      ██      ██ ██████  ███████ █████   ██████  
██      ██   ██ ██           ██ ██   ██ ██   ██     ██      ██ ██      ██   ██ ██      ██   ██ 
██████ ██   ██ ███████ ███████ ██   ██ ██   ██      ██████ ██ ██      ██   ██ ███████ ██   ██ \n
""")
def cryptography():
    print("The Cipher is ON\n")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("INVALID!!")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        def encrypt(plain_text, shift_amount):
            encrypted_text = ""
            for char in plain_text:
                if char in alphabet:
                    position = alphabet.index(char)
                    if shift_amount <= (len(alphabet)/2):
                        new_position = position + shift_amount
                    elif shift_amount > (len(alphabet)/2):
                        new_position = position + (shift_amount % (int(len(alphabet)/2)))
                        new_char = alphabet[new_position]
                    encrypted_text += new_char
                else:
                    encrypted_text += char
            print(f"the encrypted text is {encrypted_text}\n")

        def decrypt(plain_text, shift_amount):
            decrypted_text = ""
            for char in plain_text:
                if char in alphabet:
                    position = alphabet.index(char)
                    if shift_amount <= (len(alphabet)/2):
                        new_position = position - shift_amount
                    elif shift_amount > (len(alphabet)/2):
                        new_position = position + (shift_amount % (int(len(alphabet)/2)))
                        new_char = alphabet[new_position]
                    decrypted_text += new_char
                else:
                    decrypted_text += char
            print(f"the decrypted text is {decrypted_text}\n")


        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)


caesar = True
while caesar:
    cryptography()
    result = input("do you want to continue using the cipher?\n").lower()
    if result == "no":
        print("OK GOODBYE!")
        caesar = False
    elif result != "no" and result != "yes":
        print("INVALID!!")

    