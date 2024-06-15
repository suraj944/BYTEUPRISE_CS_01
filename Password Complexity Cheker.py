import tkinter as tk
from tkinter import messagebox
import re

# function for the checker complexity
def check_password_complexity(password):
    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    number = any(char.isdigit() for char in password)
    special_char = any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password)

    #condtion met           
    condition_met = { 

        'Length (8+ characters)' : length,
        'Uppercase Letter': uppercase,
        'Lowercase Letter:': lowercase,
        'Digit': number,
        'Special Character': special_char 
    }

    # Checking password stregth

    if all(condition_met.values()):
        Strength = "Strong"
    elif length and (uppercase or lowercase) and (number or special_char):
        Strength = "Medium"
    else:
        Strength = "Weak"
    return Strength, condition_met

def on_check_password():

    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Password cannot be empty. Please enter a password.")
        return
   
    Strength, condition_met = check_password_complexity(password)


    feedback = f"Password Strength: {Strength}\n\n Criteria Met:"
    for con, met in condition_met.items():
        feedback += f"\n- {con}: {'✔' if met else '✘'}"

    messagebox.showinfo("Password Complexity", feedback)


root = tk.Tk()
root.title("Secure Key - Password Complexity Checker")
root.resizable(False, False)

window_width = 360
window_height = 90
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Password", command=on_check_password)
check_button.grid(row=1,column=0,columnspan=2,pady=10)

root.mainloop() 