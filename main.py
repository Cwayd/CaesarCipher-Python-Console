import random

# Function to encrypt the message
def encrypt(message, key):
    encrypted_message = ""
    key_str = str(key)  # Convert the key to a string to loop through it
    key_len = len(key_str)  # Get the length of the key
    for i, char in enumerate(message):
        if char.isalpha():
            key_digit = int(key_str[i % key_len])  # Loop through the key if it’s longer than the message
            if char.isupper():
                shift = (ord(char) + key_digit - 65) % 26 + 65
            else:
                shift = (ord(char) + key_digit - 97) % 26 + 97
            encrypted_message += chr(shift)
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, key):
    decrypted_message = ""
    key_str = str(key)  # Convert the key to a string
    key_len = len(key_str)
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            key_digit = int(key_str[i % key_len])  # Use the digit at position i % len(key_str)
            if char.isupper():
                shift = (ord(char) - key_digit - 65) % 26 + 65
            else:
                shift = (ord(char) - key_digit - 97) % 26 + 97
            decrypted_message += chr(shift)
        else:
            decrypted_message += char
    return decrypted_message

# Function to generate a random "scrambled" message when the key is incorrect
def generate_random_message(length):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

# Main program logic with menu
if __name__ == "__main__":  # Corrected line
    # Dictionary to store encrypted messages with their associated keys
    encrypted_messages = {}

    while True:
        # Display menu options
        print("\nOptions:")
        print("E - Encrypt a message")
        print("D - Decrypt a message")
        print("Q - Quit the program")
        
        # Get user's choice
        choice = input("Please select an option (E/D/Q): ").strip().upper()

        if choice == "E":
            # Encryption option
            message = input("Enter a word or phrase to encrypt: ")
            try:
                key = int(input("Enter the encryption key (number): "))
            except ValueError:
                print("Invalid key! Please enter a numeric key.")
                continue

            # Encrypt the message and store it with the key
            encrypted_message = encrypt(message, key)
            encrypted_messages[encrypted_message] = key
            print("\nEncrypted Message:", encrypted_message)

        elif choice == "D":
            # Decryption option
            if not encrypted_messages:
                print("No messages have been encrypted yet. Please encrypt a message first.")
            else:
                # Ask for the encrypted message and the decryption key
                encrypted_message = input("Enter the encrypted message you want to decrypt: ")
                
                # Check if the encrypted message exists
                if encrypted_message in encrypted_messages:
                    try:
                        decryption_key = int(input("Enter the encryption key to decrypt the message: "))
                    except ValueError:
                        print("Invalid key! Please enter a numeric key.")
                        continue

                    # Verify if the entered key matches the stored key
                    if decryption_key == encrypted_messages[encrypted_message]:
                        decrypted_message = decrypt(encrypted_message, decryption_key)
                        print("\nDecrypted Message:", decrypted_message)
                    else:
                        print("Incorrect key! Here's a scrambled message instead:")
                        print(generate_random_message(len(encrypted_message)))
                else:
                    print("The entered encrypted message was not found.")

        elif choice == "Q":
            # Quit option
            print("Exiting program.")
            break

        else:
            print("Invalid option! Please select E, D, or Q.")
