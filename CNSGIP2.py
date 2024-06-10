import re

def password_strength(password):

    # Length check
    if len(password) < 8:
        return "Password is too short. Minimum length is 8 characters."

    # Variety of characters
    strength_criteria = {
        'lowercase': re.search(r'[a-z]', password) is not None,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'digit': re.search(r'[0-9]', password) is not None,
        'special': re.search(r'[@#$%^&+=]', password) is not None
    }

    # Count how many criteria are met
    criteria_met = sum(strength_criteria.values())

    # Evaluate strength
    if criteria_met == 4:
        return "Password is strong."
    elif criteria_met == 3:
        return "Password is medium."
    else:
        return "Password is weak."

def main():
    print("Password Strength Checker")
    print("=========================")
    print("This program checks the strength of a given password.")
    print("A strong password should be at least 8 characters long and include a mix of uppercase, lowercase, numbers, and special characters.")
    print()

    user_input = input("Enter a password to check: ")
    
    strength_message = password_strength(user_input)
    print(strength_message)

if __name__ == "__main__":
    main()
