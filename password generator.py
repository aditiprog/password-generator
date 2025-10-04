import random
import string
import tkinter as tk
from tkinter import ttk

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?/"
special_chars = "!@#$%&*?/"

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Password length must be at least 4.")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(special_chars)
    ]

    for _ in range(length - 4):
        password.append(random.choice(chars))

    random.shuffle(password)
    final_password = ''.join(password)
    strength = check_strength(final_password)

    result_label.config(text=f"Password: {final_password}")
    strength_label.config(text=f"Strength: {strength}")

def check_strength(pw):
    score = 0
    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in special_chars for c in pw):
        score += 1

    return "Strong" if score >= 6 else "Moderate" if score >= 4 else "Weak"

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = ttk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Courier", 12))
result_label.grid(row=2, column=0, columnspan=2)

strength_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"))
strength_label.grid(row=3, column=0, columnspan=2)

root.mainloop()