#CS1300_HW3_Luczko_KC.py
"""
CS1300 - Homework 3: String Manipulation
Name: KC Luczko 
Date: 9/15/2025
Description: Programs that work with text and string operations
"""

print("=== Business Card Generator ===")
# Get user information
name = input("Enter your full name: ")
title = input("Enter your job title: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
# Create the business card
border = "*" * 40 # This creates a line of 40 asterisks
# YOUR CODE HERE
print(border)
print(name.center(40))
print(title.center(40))
print(email.center(40))
print(phone.center(40))
print(border)
# Hint: You can center text using:
# text.center(40) # Centers text in 40 characters

print("=== Username Generator ===")
# Get user's name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# Generate usernames
username_1 = (first_name [0:3] + last_name[0:3]).lower()
username_2 = (first_name [0] + last_name).lower()
username_3 = (first_name [0] + str(len(last_name))).lower()

# Remember:
# - Use .lower() to make lowercase
# - Use [0:3] to get first 3 characters
# - Use [0] to get first character
# - Use str() to convert numbers to strings
print("\nYour username options:")
print("1:",username_1)
print("2:",username_2)
print("3:",username_3)

print("=== Text Message Formatter ===")
# Get the message
message = input("Enter your message: ")
# Calculate length
length = len(message)
# YOUR CODE HERE
print(f"(shouting): {message.upper()}")
print(f"(whispering): {message.lower()}")
print(f"Snake_case: {message.replace(' ', '_')}")
print(f"First half: {message[0:length//2]}")
print(f"Last half: {message[length//2:]}")
print(f"Reversed: {message[::-1]}")
print(f"\nOriginal: {message}")
print(f"Length: {length} characters")
# Continue with other transformations...


print("=== Password Validator ===")
# Get password
password = input("Create a password: ")
# Check length
length = len(password)
has_minimum_length = length >= 8
# Check for uppercase and lowercase
has_uppercase = password != password.lower()
has_lowercase = password != password.upper()
# YOUR CODE HERE
if length > 1:
    masked = password[0] + ("*" * (length - 2)) + password[-1]
else:
    masked = password
    #Im not sure if im supposed to use if and else statements in the class yet but thats how i learned to do this type of an operation
requirements = sum([has_minimum_length, has_uppercase, has_lowercase])

print(f"Masked password : {masked}")
print(f"length: {length}")

if requirements == 3:
    print("Strength: Strong password!")
elif requirements == 2:
    print("Strength: Decent password")
else:
    print("Strength: Weak password")
 
print("Password analysis: ")
print("Minimum length 8+:", "Pass" if has_minimum_length else "Fail")
print("Contains uppercase:", "Pass" if has_uppercase else "Fail")
print("Contains lowercase:", "Pass" if has_lowercase else "Fail")
# Example: "password" becomes "p******d"
# 2. Count how many requirements are met
# 3. Display results
# For masking:
# First character: password[0]
# Last character: password[-1]
# Middle asterisks: "*" * (length - 2)


print("=== Mad Libs Story Generator ===")
print("I need some words to create your story!\n")
# Collect inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
adjective1 = input("Enter an adjective (describing word): ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb ending in -ing: ")
verb2 = input("Enter another verb ending in -ing: ")
number = input("Enter a number: ")
color = input("Enter a color: ")
# YOUR CODE HERE
# Create your story using the inputs
# You can use + to concatenate or use f-strings
# Make the user inputs uppercase for highlighting
name_upper = name.upper()
place_upper = place.upper()
animal_upper = animal.upper()
food_upper = food.upper()
adjective1_upper = adjective1.upper()
adjective2_upper = adjective2.upper()
verb1_upper = verb1.upper()
verb2_upper = verb2.upper()
number_upper = number.upper()
color_upper = color.upper()

# Create the story
story = f"""
Once upon a time, {name_upper} was {verb1.upper()} through {place_upper}
when they discovered a {adjective1.upper()} {animal.upper()}.
The {animal.upper()} was eating {number} pieces of {food.upper()}
and wearing a {color.upper()} hat.
"How {adjective2.upper()}!" exclaimed {name_upper}.
They spent the rest of the day {verb2.upper()} together.
THE END
"""
# Count words (split by spaces and count)
word_count = len(story.split())
print("\n" + "="*50)
print("YOUR STORY")
print("="*50)
print(story)
print(f"\nYour story has {word_count} words!")

# Get name and print each letter on a separate line
print("AscII Art style name")
name = input("Enter your name: ")
print("\n".join(name.upper())) # This prints each letter on its own line

print("Find and replace tool")
text = input("Enter text here: ")
find_word = input("Word to find: ")
replace_wword = input("Replace with")
new_text = text.replace(find_word, replace_wword)

print(f"Result: {new_text}")