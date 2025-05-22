# secret_message.py
# This script lets a user encode or decode a secret message using a Caesar Cipher.

def encode_message(message, shift):
    """
    Encodes the message by shifting each letter by a given number (shift).
    """
    encoded = ""  # This will store the final encoded message

    for char in message:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Set base depending on case
            # Shift the character within the alphabet range
            encoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            encoded += char  # Non-letters (like spaces or punctuation) stay the same

    return encoded

def decode_message(encoded_message, shift):
    """
    Decodes the message by shifting letters in the opposite direction.
    """
    return encode_message(encoded_message, -shift)  # Just reverse the shift

# --- User Interaction Starts Here ---

# Ask the user if they want to encode or decode
choice = input("Type 'e' to encode or 'd' to decode: ").lower()

# Handle encoding
if choice == 'e':
    message = input("Enter your message to encode: ")
    try:
        shift = int(input("Enter a number to shift by (this is your secret key): "))
        encoded = encode_message(message, shift)
        print("✅ Encoded message:", encoded)
    except ValueError:
        print("❌ Please enter a valid number for the shift.")

# Handle decoding
elif choice == 'd':
    message = input("Enter the message to decode: ")
    try:
        shift = int(input("Enter the shift key used to encode the message: "))
        decoded = decode_message(message, shift)
        print("✅ Decoded message:", decoded)
    except ValueError:
        print("❌ Please enter a valid number for the shift.")

# Handle invalid choices
else:
    print("❌ Invalid choice. Please type 'e' to encode or 'd' to decode.")

