import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # Start with lowercase letters
    characters = string.ascii_lowercase  

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Main program
print("🔑 Password Generator 🔑")
length = int(input("Enter password length: "))

# Ask user preferences
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and display
password = generate_password(length, use_upper, use_digits, use_symbols)
print("\n✅ Your generated password is:", password)

# (Optional) Save to file
save = input("\nDo you want to save this password to a file? (y/n): ").lower()
if save == 'y':
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
    print("📁 Password saved in 'passwords.txt'")
