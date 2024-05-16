# Preliminary code 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        new_letter_index = letter_index + shift_amount
        encoded_text += alphabet[new_letter_index]
    return encoded_text
def decrypt(encrypted_text, encryption_shift):
    decrypted_text = ""
    for letter in encrypted_text:
        letter_index = alphabet.index(letter)
        original_index = letter_index - encryption_shift
        decrypted_text += alphabet[original_index]
    print(f"The decrypted text is {decrypted_text}.")

if direction == 'encode':
    encodedText = encrypt(text, shift)
    print(f"The encoded text is {encodedText}")
else:
    encodedText = text
    decrypt(encodedText, shift)
