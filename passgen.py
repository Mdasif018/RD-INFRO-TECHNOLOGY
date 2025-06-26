import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_special)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
