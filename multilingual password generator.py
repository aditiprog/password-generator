import random
import string
import tkinter as tk
from tkinter import ttk

english_chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hindi_chars = "अआइईउऊएऐओऔकखगघचछजझटठडढतथदधनपफबभमयरलवशषसह"
special_chars = "!@#$%&*"

def generate_password():
    try:
        length = int(length_entry.get())
        memorable = memorable_entry.get().strip()
        lang_choice = lang_var.get()

        if length < 4:
            result_label.config(text="Password length must be at least 4", foreground="red")
            return
        if len(memorable) > length - 4:
            result_label.config(text="Memorable detail too long", foreground="red")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.", foreground="red")
        return

    if lang_choice == "English":
        chars = english_chars
    elif lang_choice == "Hindi":
        chars = hindi_chars
    else:
        chars = english_chars + hindi_chars

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(special_chars)
    ]

    insert_pos = random.randint(1, len(password))
    password.insert(insert_pos, memorable)

    while sum(len(p) for p in password) < length:
        password.append(random.choice(chars + special_chars))

    random.shuffle(password)
    final_password = ''.join(password)[:length]

    strength = check_strength(final_password)

    result_label.config(text=f"{final_password}", foreground="#222")
    update_strength_bar(strength)
    copy_button.config(state="normal")

def check_strength(pw):
    score = 0
    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in special_chars for c in pw): score += 1
    return "Strong" if score >= 6 else "Moderate" if score >= 4 else "Weak"

def update_strength_bar(level):
    colors = {"Strong": "#2ecc71", "Moderate": "#f39c12", "Weak": "#e74c3c"}
    strength_bar.config(bg=colors[level])
    strength_label.config(text=f"Strength: {level}", foreground=colors[level])

def copy_to_clipboard():
    pw_text = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(pw_text)
    root.update()
    strength_label.config(text="Copied to clipboard!", foreground="#2980b9")
root = tk.Tk()
root.title("Multilingual Password Generator")
root.state("zoomed")
root.configure(bg="#eaf2f8")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 13), background="#eaf2f8")
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=10, relief="flat", background="#3498db", foreground="white")
style.map("TButton", background=[("active", "#2980b9")])

main_frame = ttk.Frame(root, padding="40 40 40 40", style="TFrame")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(main_frame, text="🔐Password Generator", font=("Segoe UI", 22, "bold"), bg="#eaf2f8", fg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

ttk.Label(main_frame, text="Password length:").grid(row=1, column=0, sticky="w", pady=10)
length_entry = ttk.Entry(main_frame, width=25)
length_entry.grid(row=1, column=1, pady=10)

ttk.Label(main_frame, text="Memorable word (e.g. name, date):").grid(row=2, column=0, sticky="w", pady=10)
memorable_entry = ttk.Entry(main_frame, width=25)
memorable_entry.grid(row=2, column=1, pady=10)

ttk.Label(main_frame, text="Language mode:").grid(row=3, column=0, sticky="w", pady=10)
lang_var = tk.StringVar(value="English")
lang_menu = ttk.Combobox(main_frame, textvariable=lang_var, values=["English", "Hindi", "Mixed"], state="readonly", width=23)
lang_menu.grid(row=3, column=1, pady=10)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = tk.Label(main_frame, text="", font=("Consolas", 20, "bold"), bg="#fdfefe", fg="#2c3e50", relief="solid", padx=15, pady=10)
result_label.grid(row=5, column=0, columnspan=2, pady=15)

strength_bar = tk.Label(main_frame, text="", width=40, height=2, bg="#bdc3c7")
strength_bar.grid(row=6, column=0, columnspan=2, pady=5)

strength_label = ttk.Label(main_frame, text="", font=("Segoe UI", 13, "italic"))
strength_label.grid(row=7, column=0, columnspan=2)

copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.grid(row=8, column=0, columnspan=2, pady=20)

footer = tk.Label(root, text="talk doesn't cook rice- made by aditi", font=("Segoe UI", 11, "italic"), bg="#eaf2f8", fg="#7f8c8d")
footer.pack(side="bottom", pady=10)

root.mainloop()