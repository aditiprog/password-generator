# Password Generator GUI

A beginner-friendly Python application that generates secure, customizable passwords through a graphical interface. Built with a focus on usability, clarity, and teaching secure password practices — ideal for learners, educators, and anyone looking to improve their digital hygiene.

## 📌Project Overview

This project allows users to:
- Generate passwords of custom length
- Include memorable details using *Memorability Mode*
- Ensure strong password composition using lowercase, uppercase, digits, and special characters
- View password strength feedback (Weak / Moderate / Strong)
- Use a simple GUI built with `tkinter`

# What Is Memorability Mode?
*Memorability Mode* is a unique feature that lets users include a personal detail — such as a name, date, or keyword — in the generated password. This helps users remember their passwords more easily while still maintaining strength and randomness.
For example:
- Input: `Fluffy2023`
- Output: `aB3$Fluffy2023`
- Strength: `Strong`

The app ensures that the memorable detail doesn't compromise password length or diversity. If the detail is too long, the app will notify the user.

# 🖥️ Technologies Used

- Python 3.x
- Tkinter – for GUI
- Random – for password generation

# 🚀 Getting Started
Prerequisites
Ensure you have Python installed. You can check by running:
```bash
Running the App:
- Clone or download this repository.
- Run the script:
python password_generator.py

How It Works:
- Enter the desired password length.
- Optionally enter a memorable detail (e.g., "Fluffy2023").
- Click Generate.
- The app displays:
- A secure password
- Its strength rating
Example Output
Password: aB3$Fluffy2023
Strength: Strong


Planned Enhancements
- [ ] Copy-to-clipboard button
- [ ] Save password history to a file
- [ ] Entropy score display
- [ ] Modular refactor for better readability
- [ ] Unit tests for strength checker

👩‍💻 Author
Aditi
First-year CS (Cyber Security) student at VIT Bhopal


screenshot: 
 You're all set to upload this!<img width="617" height="450" alt="Screenshot 2025-08-28 143208" src="https://github.com/user-attachments/assets/e5b44b08-1420-4243-9587-ee433f2691ef" />









 













