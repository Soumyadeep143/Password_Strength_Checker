Password Manager (Python)

This is a simple Password Manager application implemented in Python. The program allows users to check the strength of their passwords, save passwords associated with websites and usernames, and retrieve saved passwords. The saved passwords are stored in a text file for simplicity.

Features

1. Password Strength Checker: 
   - Checks whether a password meets the following criteria:
     - At least 8 characters.
     - Contains both uppercase and lowercase letters.
     - Contains at least one digit.
     - Contains at least one special symbol (@$!%*?&).
  
2. Save Password:
   - Saves passwords sec
   - No external libraries are required beyond the standard library (re for regular expressions).

How It Works

1. Password Strength Check:  
   - The user can input a password, and the program checks if it meets the predefined strength requirements using a regular expression. It will output whether the password is strong or provide feedback on how to improve it.
   
2. Save Password:  
   - The program allows users to save passwords for specific websites and usernames. These passwords are appended to a file (passwords.txt). If the file doesn't exist, it is automatically created.
   
3. View Saved Passwords:  
   - The program can display all previously saved passwords by reading the contents of the passwords.txt file.

4. Error Handling:  
   - The program includes basic error handling to ensure passwords are saved correctly and any file access issues are reported.

Usage

1. Check Password Strength
To check the strength of a password, the user can input the password, and the program will return whether it’s a strong password or provide feedback on how to improve it.

Example:


Enter password to check: MyPassword123!
Strong password


2. Save a Password
To save a password, the user must input:
- Website
- Username
- Password
