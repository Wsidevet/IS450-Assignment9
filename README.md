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

### AI TOOL USED:

ChatGPT (OpenAI)
Version 6

### AI Assistance:

I asked ChatGPT to write code for a password strength rating feature that I could add to my existing program. ChatGPT suggested a new function that uses the password's length and the number of character types it contains.

### New Or Modified Features

1. Added a password_strength() function that rates passwords as WEAK, MODERATE, or STRONG.
2. The function reuses the existing checks for uppercase letters, lowercase letters, numbers, and symbols.
3. Updated the program's output to show the strength rating alongside the estimated cracking time.
4. Simplified the prompt for checking another password and adjusted the output formatting.

### Evaluation of AI Output

I accepted ChatGPT's suggested password strength function because it was easy to understand and fit into my original program without replacing it. I added the function to main.py and updated main() to display the result. The ratings are based only on length and character variety, so they are simple guidelines rather than a complete measure of password security.

### How To Run The Program:

1. Make sure Python is installed on your computer.
2. Download the main.py file.
3. Run the program using Python.
4. Enter a password when prompted.
5. The program will display the password length and estimated cracking time.
6. Enter Y to check another password or N to exit.
