import re

def check_password_strength(password):
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*()]', password):
        return "Strong ✅"
    elif re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()