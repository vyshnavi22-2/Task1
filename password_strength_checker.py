import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Score based on failed criteria
    score = sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])
    
    # Feedback
    if score == 0:
        strength = "Strong"
    elif score <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Detailed feedback
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters long.")
    if lowercase_error:
        feedback.append("Add at least one lowercase letter.")
    if uppercase_error:
        feedback.append("Add at least one uppercase letter.")
    if digit_error:
        feedback.append("Include at least one digit.")
    if special_char_error:
        feedback.append("Include at least one special character (!@#$%^&* etc).")

    return strength, feedback

# User input
password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions to improve:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
