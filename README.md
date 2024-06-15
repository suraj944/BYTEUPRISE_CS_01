# Secure Key - Password Complexity Checker

This is a simple password complexity checker application built with Python's Tkinter library. It allows users to input a password and checks the password's complexity based on several criteria, providing feedback on the password's strength.

## Features

- **Length Check:** Ensures the password is at least 8 characters long.
- **Uppercase Check:** Ensures the password contains at least one uppercase letter.
- **Lowercase Check:** Ensures the password contains at least one lowercase letter.
- **Digit Check:** Ensures the password contains at least one digit.
- **Special Character Check:** Ensures the password contains at least one special character (e.g., `!@#$%^&*()-_=+[{]}\|;:'",<.>/?~`).

## Password Strength

The application categorizes the password strength into three levels:

- **Strong:** Meets all criteria.
- **Medium:** Meets the length criterion and at least two of the other criteria (uppercase, lowercase, digit, special character).
- **Weak:** Does not meet the criteria for a strong or medium password.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/suraj944/BYTEUPRISE_CS_01.git
    cd BYTEUPRISE_CS_01-main
    ```

## Usage

1. Navigate to the project directory.

2. Run the application:

    ```bash
    python Password Complexity Cheker.py
    ```

3. Enter a password in the input field and click the "Check Password" button.

4. A message box will display the strength of the password and the criteria met.

## Code Explanation

- **`check_password_complexity(password):`** A function that checks if the password meets the defined criteria and returns the strength and conditions met.
- **`on_check_password():`** A function that retrieves the password from the input field, checks its complexity, and displays the results in a message box.
- **Tkinter GUI Setup:** Sets up the Tkinter window with input fields and buttons.
