# Name: Garry Singh
# Assignment 8: Git Development With AI

#Imports
import random

# Store All Of The Characters Than Can Exist In Different Lists
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '|', '\\', '~', '`']

# Store All Of The Data From The Hive Systems Password Data Into A Searchable Dictionary
# Link To Table https://www.hivesystems.com/blog/are-your-passwords-in-the-green
hive_systems_2026 = {
    4: {"numbers": "Instantly", "lowercase": "Instantly", "upper_lower": "Instantly", "num_upper_lower": "Instantly", "all_chars": "Instantly"},
    5: {"numbers": "Instantly", "lowercase": "Instantly", "upper_lower": "46 mins", "num_upper_lower": "2 hours", "all_chars": "3 hours"},
    6: {"numbers": "Instantly", "lowercase": "37 mins", "upper_lower": "2 days", "num_upper_lower": "5 days", "all_chars": "1 week"},
    7: {"numbers": "Instantly", "lowercase": "16 hours", "upper_lower": "3 months", "num_upper_lower": "10 months", "all_chars": "2 years"},
    8: {"numbers": "Instantly", "lowercase": "2 weeks", "upper_lower": "12 years", "num_upper_lower": "50 years", "all_chars": "132 years"},
    9: {"numbers": "2 hours", "lowercase": "1 year", "upper_lower": "636 years", "num_upper_lower": "3k years", "all_chars": "9k years"},
    10: {"numbers": "20 hours", "lowercase": "32 years", "upper_lower": "33k years", "num_upper_lower": "191k years", "all_chars": "645k years"},
    11: {"numbers": "1 week", "lowercase": "839 years", "upper_lower": "1m years", "num_upper_lower": "11m years", "all_chars": "45m years"},
    12: {"numbers": "3 months", "lowercase": "21k years", "upper_lower": "89m years", "num_upper_lower": "737m years", "all_chars": "3bn years"},
    13: {"numbers": "2 years", "lowercase": "567k years", "upper_lower": "4bn years", "num_upper_lower": "45bn years", "all_chars": "221bn years"},
    14: {"numbers": "23 years", "lowercase": "14m years", "upper_lower": "241bn years", "num_upper_lower": "2tn years", "all_chars": "15tn years"},
    15: {"numbers": "229 years", "lowercase": "383m years", "upper_lower": "12tn years", "num_upper_lower": "175tn years", "all_chars": "1qd years"},
    16: {"numbers": "2k years", "lowercase": "9bn years", "upper_lower": "653tn years", "num_upper_lower": "10qd years", "all_chars": "75qd years"},
    17: {"numbers": "22k years", "lowercase": "259bn years", "upper_lower": "33qd years", "num_upper_lower": "675qd years", "all_chars": "5qn years"},
    18: {"numbers": "228k years", "lowercase": "6tn years", "upper_lower": "1qn years", "num_upper_lower": "41qn years", "all_chars": "372qn years"}
}


# Get The Length Of Password And Return Length
def len_of_password(user_pass:str)-> int:
    pass_len = len(user_pass)
    return pass_len

# Check If The Password Has Any Uppercase Characters And Returns True Or False
def has_uppercase(user_pass:str)-> bool:
    result = any(char in user_pass for char in uppercase_letters)
    return result

# Check If The Password Has Any Lowercase Characters And Returns True Or False
def has_lowercase(user_pass:str)-> bool:
    result = any(char in user_pass for char in lowercase_letters)
    return result

# Check If The Password Has Any Number Characters And Returns True Or False
def has_numbers(user_pass:str)-> bool:
    result = any(char in user_pass for char in numbers_list)
    return result

# Check If The Password Has Any Symbol Characters And Returns True Or False
def has_symbols(user_pass:str)-> bool:
    result = any(char in user_pass for char in symbols_list)
    return result

# ----------------------------------------------------------------------------------------------------------------------
# AI GENERATED CODE (ASSIGNMENT 8)

# Determine Password Strength Based On Length And Character Types
def password_strength(user_pass: str) -> str:

    # Get Password Length
    pass_len = len_of_password(user_pass)

    # Count How Many Different Character Types The Password Contains
    char_types = 0

    if has_uppercase(user_pass):
        char_types += 1

    if has_lowercase(user_pass):
        char_types += 1

    if has_numbers(user_pass):
        char_types += 1

    if has_symbols(user_pass):
        char_types += 1

    # Determine Password Strength
    if pass_len >= 12 and char_types >= 3:
        return "STRONG"

    elif pass_len >= 8 and char_types >= 2:
        return "MODERATE"

    else:
        return "WEAK"

# AI GENERATED CODE ENDS HERE
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# ASSIGNMENT 9 MANUAL FEATURE

# Generate a random password that is 12 or more characters long
def password_generator()->None:

    gen_pass = ""
    pass_len = int(input("\nHow Long Would You Like The New Password To Be? (!MUST BE 12 Characters or More): "))
    while pass_len < 12:
       pass_len = int(input("\nLength of password has to be 12 or more characters. Please select new length: "))
    
    # Takes all the lists of characters and puts them into one so that they can chosen from randomly

    char_lists = [uppercase_letters,lowercase_letters,numbers_list,symbols_list]
    
    # Generate the random password
    for i in range(0,pass_len):
        x = random.choice(char_lists)
        gen_pass += random.choice(x)

    # Print the password
    print(f"\nThe Generated Password is: {gen_pass}")

# MANUAL FEATURE ENDS HERE
# ----------------------------------------------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------------------------------------------
# ASSIGNMENT 9 AI FEATURE

# Suggest Character Types The User Can Add To Their Password
def missing_character_suggestions(user_pass: str) -> None:
    suggestions = []

    if not has_uppercase(user_pass):
        suggestions.append("Add uppercase letters.")

    if not has_lowercase(user_pass):
        suggestions.append("Add lowercase letters.")

    if not has_numbers(user_pass):
        suggestions.append("Add numbers.")

    if not has_symbols(user_pass):
        suggestions.append("Add symbols.")

    print("\nPassword Improvement Suggestions:")
    if suggestions:
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("No character types are missing from your password.")

# ASSIGNMENT 9 AI FEATURE ENDS HERE
# ----------------------------------------------------------------------------------------------------------------------


# Function That Contains The Code To Check The Password
def check_password(user_pass: str)-> str:
    # Calls Functions To Get Lenght And Check Characters For Type
    pass_len = len_of_password(user_pass=user_pass)
    contains_upper = has_uppercase(user_pass=user_pass)
    contains_lower = has_lowercase(user_pass=user_pass)
    contains_number = has_numbers(user_pass=user_pass)
    contains_symbol = has_symbols(user_pass=user_pass)
    
    pass_contains = ""

    # Checks What Category The Password Falls Under To Select The Correct Dictionary Definition
    if contains_number == True and contains_lower == False and contains_upper == False and contains_symbol == False:
        pass_contains = "numbers"
    elif contains_number == False and contains_lower == True and contains_upper == False and contains_symbol == False:
        pass_contains = "lowercase"
    elif contains_number == False and contains_lower == True and contains_upper == True and contains_symbol == False:
        pass_contains = "upper_lower"
    elif contains_number == True and contains_lower == True and contains_upper == True and contains_symbol == False:
        pass_contains = "num_upper_lower"
    elif contains_number == True and contains_lower == True and contains_upper == True and contains_symbol == True:
        pass_contains = "all_chars"
    else:
        pass_contains = "other"


    # Returns This Output If The Combination Is Not In The Hive Systems Dictionary Table (Example : Only Numbers and Symbols)
    if pass_contains == "other":
        return "Sorry Your Password Combination Was Not Tested For By Hive Systems And We Do Not Have Any Data To Determine The Length It Will Take To Crack In 2026"

    # Returns Output For Edge Cases If The Lenght Of Password is Under 4 Characters and Over 18 Characters 
    if pass_len < 4:
        return "Instantly"
    elif pass_len > 18:
        return "Passwords with 19 Characters Or More Take A Very Long Time, Atleast More Than 228k Years"
    else:
        # Get Output From Hive Table According To Len Of Password and Definition
        return hive_systems_2026[pass_len][pass_contains]
    
# Main Function That Controls The Program
def main()-> None:
    print("\nHow Long Will It Take For Modern Hardware To Crack Your Password In 2026?")
    keep_running = True
    

    while keep_running:
        
        
        # Get User Password
        user_pass = input("\nEnter Password To Check: ")

        # Call The Check Password Function And Store The Output
        time_to_crack = check_password(user_pass=user_pass)

        # Call The Password Strength Function
        strength = password_strength(user_pass=user_pass)

        print("-----------------------------------------------------------------------------------")
        # Print The Length Of Password And Output (Time To Crack The Password)
        print(f"\nYour Password Is {len(user_pass)} Characters Long")
        print(f"The Time It Will Take To Crack Your Password In 2026 is: {time_to_crack}")
        print(f"Your Password Strength Is: {strength}")

        # Show Suggestions For Missing Character Types (Assignment 9 AI Feature)
        missing_character_suggestions(user_pass=user_pass)
        print("-----------------------------------------------------------------------------------")

        cont = input("\nWould You Like To Check Another Password?(Y/N): ")

        if cont.strip().lower() not in ["y", "yes"]:
            keep_running = False

    # ----------------------------------
    # ASSIGNMENT 9 MANUAL FEATURE
    gen_pass_question = input("\nWould You Like To Generate A Secure Password(Y/N): ")

    if gen_pass_question.strip().lower() in ["y", "yes"]:    
        password_generator()
    # ----------------------------------


    print("\nThank You For Using This Program\n")
    


if __name__ == "__main__":
    main()
    