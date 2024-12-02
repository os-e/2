def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Taking input from the user
text = input("Enter the text to be encrypted/decrypted: ")
shift = int(input("Enter the shift value: "))
action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

# Encrypt or Decrypt based on user input
if action == 'encrypt':
    result = caesar_cipher(text, shift, encrypt=True)
elif action == 'decrypt':
    result = caesar_cipher(text, shift, encrypt=False)
else:
    result = "Invalid action. Please type 'encrypt' or 'decrypt'."

print(f"Result: {result}")

import itertools
import string

def brute_force_attack(target_password, max_length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(combination)
            if guess == target_password:
                return guess, attempts

    return None, attempts

if __name__ == "__main__":
    target_password = input("Enter the password to brute force: ")
    max_length = int(input("Enter the maximum length of the password: "))
    found_password, attempts = brute_force_attack(target_password, max_length)
    
    if found_password:
        print(f"Password found: {found_password} in {attempts} attempts.")
    else:
        print(f"Password not found within length {max_length}. Total attempts: {attempts}")
import hashlib
import requests

def read_credentials(file_path="up.txt"):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    credentials = [line.strip().split(',') for line in lines]
    return credentials

def check_password_leak(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True
    return False

def main():
    credentials = read_credentials()
    for username, password in credentials:
        if check_password_leak(password):
            print(f"Password for user {username} has been leaked.")
        else:
            print(f"Password for user {username} is safe.")

if __name__ == "__main__":
    main()
import random

def generate_password(desired_length, dictionary_file="dict.txt"):
    try:
        with open(dictionary_file, "r") as file:
            words = file.read().splitlines()
        
        if not words:
            print("Error: Dictionary file is empty.")
            return None

        password = ""
        while len(password) < desired_length:
            word = random.choice(words)
            password += word

        return password[:desired_length]
    except FileNotFoundError:
        print("Error: Dictionary file not found. Please check the file path.")
        return None

def main():
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

    password = generate_password(desired_length)
    if password:
        print(f"Generated Password: {password}")
        print(f"Password Length: {len(password)}")

if __name__ == "__main__":
    main()

def get_rail_positions(text_length, num_rails):
    pos = [[] for _ in range(num_rails)]
    step = 2 * (num_rails - 1)
    
    for i in range(text_length):
        rail = i % step
        if rail >= num_rails:
            rail = step - rail
        pos[rail].append(i)

    print(pos)
    return pos

def rail_fence_cipher(text, num_rails, encrypt=True):
    if num_rails == 1:
        return text
    
    text_length = len(text)
    pos = get_rail_positions(text_length, num_rails)
    
    if encrypt:
        return ''.join(text[i] for rail in pos for i in rail)
    else:
        index = 0
        original_text = [''] * text_length
        for rail in pos:
            for i in rail:
                original_text[i] = text[index]
                index += 1
        return ''.join(original_text)

def main():
    while True:
        print("\nRail Fence Cipher Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text = input("Enter the text to encrypt: ")
            num_rails = int(input("Enter the number of rails: "))
            ciphered_text = rail_fence_cipher(text, num_rails, encrypt=True)
            print("Ciphered Text:", ciphered_text)
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            num_rails = int(input("Enter the number of rails: "))
            decrypted_text = rail_fence_cipher(text, num_rails, encrypt=False)
            print("Decrypted Text:", decrypted_text)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import hashlib

def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

# Example usage
password = input("Enter a password to hash: ")
hashed_password = hash_password(password)
print(f"SHA-256 hashed password: {hashed_password}")
