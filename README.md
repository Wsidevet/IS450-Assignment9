# IS450-Assignment9

## Assignment 9: Dual Development

### Project Description:

This Project Asks The User For Their Password And Checks How Long It Would Take For The Password To Be Cracked By A Computer Using The Following Hardware

2026 hardware : 16 x RTX 5090 | 2026 password hash: bcrypt set to a work order of 10 (i.e. 1024 iterations of hashing)

Link For The [Hive Systems Table](https://www.hivesystems.com/blog/are-your-passwords-in-the-green)

### Initial Version:

The initial version of the program includes the following features:

1. Allows the user to enter a password.
2. Calculates the length of the password.
3. Checks whether the password contains uppercase letters, lowercase letters, numbers, and symbols.
4. Uses a dictionary containing the Hive Systems 2026 data to estimate how long the password would take to crack.
5. Displays the password length and estimated cracking time.
6. Allows the user to check multiple passwords using a loop.
7. Allows the user to exit the program when finished.


### Manual Feature - ASSIGNMENT 9

Feature name: Password Generator

Purpose: Will generate a secure password that is 12 characters or longer.

Expected behavior: Asks user for length of password (12 or more chars). And then generate a random string from the character lists of that length.

Two test cases:

    Test Case 1
    - Input: 12
    - Expected result: The program generates a random password that is exactly 12 characters long. (Example: "The Generated Password is: 6X!mB6R2GHcr")
    Test Case 2
    - Input: 8
    - Expected result: "Length of password has to be 12 or more characters. Please select new length:"
    
### AI Feature - ASSIGNMENT 9

**Feature name:** Missing Character Suggestions

**Purpose:** Help users improve their passwords by identifying missing character types.

**Expected behavior:** After the user enters a password, the program checks for uppercase letters, lowercase letters, numbers, and symbols. It displays suggestions for any character types that are missing. If all four types are present, the program says no character types are missing.

**Test Case 1**
- Input: `password123`
- Expected result: The program suggests adding uppercase letters and symbols.

**Test Case 2**
- Input: `PASSWORD123!`
- Expected result: The program suggests adding lowercase letters.

**Test Case 3**
- Input: `Password123!`
- Expected result: The program says no character types are missing.

### AI TOOL USED:

ChatGPT (OpenAI)
Version 6

### AI Assistance (ASSIGNMENT 8):

I asked ChatGPT to write code for a password strength rating feature that I could add to my existing program. ChatGPT suggested a new function that uses the password's length and the number of character types it contains.

### New Or Modified Features (ASSIGNMENT 8)

1. Added a password_strength() function that rates passwords as WEAK, MODERATE, or STRONG.
2. The function reuses the existing checks for uppercase letters, lowercase letters, numbers, and symbols.
3. Updated the program's output to show the strength rating alongside the estimated cracking time.
4. Simplified the prompt for checking another password and adjusted the output formatting.

### Evaluation of AI Output (ASSIGNMENT 8)

I accepted ChatGPT's suggested password strength function because it was easy to understand and fit into my original program without replacing it. I added the function to main.py and updated main() to display the result. The ratings are based only on length and character variety, so they are simple guidelines rather than a complete measure of password security.

### How To Run The Program:

1. Make sure Python is installed on your computer.
2. Download the main.py file.
3. Run the program using Python.
4. Enter a password when prompted.
5. The program will display the password length and estimated cracking time.
6. Enter Y to check another password or N to exit.
