import random
import string
FILE = "passwords.txt"
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password
def save_password(password):
    with open(FILE, "a") as f:
        f.write(password + "\n")
def show_passwords():
    try:
        with open(FILE, "r") as f:
            passwords = f.readlines()
        if not passwords:
            print("No passwords saved.")
            return
        for i, p in enumerate(passwords, 1):
            print(f"{i}) {p.strip()}")
    except FileNotFoundError:
        print("No passwords saved yet.")
def delete_password(index):
    try:
        with open(FILE, "r") as f:
            passwords = f.readlines()
        if index < 1 or index > len(passwords):
            print("Invalid number.")
            return
        passwords.pop(index - 1)
        with open(FILE, "w") as f:
            f.writelines(passwords)
        print("Password deleted.")
    except FileNotFoundError:
        print("No passwords to delete.")
while True:
    print("\nPassword Manager")
    print("1) Generate password")
    print("2) Show passwords")
    print("3) Delete password")
    print("4) Exit")
    choice = input("Choose option: ")
    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print("Generated password:", password)
            save_password(password)
        except ValueError:
            print("Length must be a number.")
    elif choice == "2":
        show_passwords()
    elif choice == "3":
        show_passwords()
        try:
            num = int(input("Enter password number to delete: "))
            delete_password(num)
        except ValueError:
            print("Invalid number.")
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")
        
