#Problem 1: String Processing
#Complete each task below
# Given information (DO NOT MODIFY):
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"
firtstname = full_name[0:5]
middlename = full_name[5:12]
lastname = full_name[13:18]
# Task 1.1 (3 points): Extract and print the first name only
print(f"{firtstname}")

# Task 1.2 (3 points): Extract and print the last name only
print(f"{lastname}")
# Task 1.3 (3 points): Create and print initials (J.M.S.)
print(f"Initials: {firtstname[0:1]}.{middlename[0:1]}.{lastname[0:1]}")
# Task 1.4 (3 points): Check if the email contains "university" (case-insensitive)
university = email[11:21]
print({university})
if "university" in {university}:
    print("Yes")
else:
    print("No")

# Task 1.5 (3 points): Replace all dashes in phone with spaces and print
phone_clean = phone.replace("-", " ")
print(f"{phone_clean}")

#Problem 2: Restaurant Rating Calculator
#Calculate based on percentage rating.
# Task 2.1 (3 points): Get these ratings
atmosphere = 4.5
food = 3.4
service = 2.5
cleanness = 3.0
# Task 2.2 (4 points): Calculate weighted average
# Weights: atmosphere=10%, food=45%, service=20%, cleanness=25%
newat=atmosphere * .1
newfood=food *.45
mewserv=service *.2
newclen=cleanness *.25
# Store result in variable 'average'
average = newat+newfood+newclen+mewserv / 4
print(average)
# Task 2.3 (8 points): Determine restaurant rating
if average >=4.0:
    print("*****")
elif average >=3.0:
    print("****")
elif average >= 2.0:
    print("***")
elif average >=1.0:
    print("**")
else:
    print("*")
# Use these ranges:
# *****: 4.0 and above
# ****: 3.0-4.0
# ***: 2.0-3.0
# **: 1.0-2.0
# *: below 1.0
# Print both the average and star rating


#Problem 3: Movie Review Number Management
#Manage a list of movie review numbers.
# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]
# Task 3.2 (3 points): Add a new review number of 4 to the end
numbers.append(4)
print(numbers)
# Task 3.3 (3 points): The third review number (4) was entered wrong.
numbers4_index= numbers.index(4)
numbers.pop(numbers4_index)
numbers.insert(3,3)
print(numbers)
# Change it to 3
# Task 3.4 (3 points): Remove the review number 1 from the list
numbers.remove(3)
print(numbers)
# Task 3.5 (3 points): Insert a review number of 3 at position 2
numbers.insert(3,2)
print(numbers)
# Task 3.6 (3 points): Create and print a sublist of the first 3 numbers
first3numbers = numbers[0:3]
print(first3numbers)
# Task 3.7 (3 points): Print:
# - How many movie review numbers
print(f"total reviews: {len(numbers)}")
# - The first review number
print(f"First review number: {numbers[0]}")
# - The last review number
print(f"last review number: {numbers[-1]}")

#Problem 4: Shopping Cart System
#Build a basic shopping cart with price checking.

# Initial setup (DO NOT MODIFY):
items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99] # Matching prices for each item
cart = []
cart_total = 0.0
# Task 4.1 (4 points): Add "milk" to cart
if "milk"  in items:
    Index= items.index("milk")
    cart.append("milk")
    cart_total=cart_total + prices[Index]

# Check if "milk" is in items, find its index, and add to cart
# Also add its price to cart_total
# Task 4.2 (4 points): Add "eggs" to cart
if "milk"  in items:
    Index= items.index("eggs")
    cart.append("eggs")
    cart_total=cart_total + prices[Index]
# Same process as above
# Task 4.3 (4 points): Try to add "cookies" to cart
if "cookies"  in items:
    print("Cookies is in items")
else:
    print("cookies not in items")
# Check if it exists first, print appropriate message
# Task 4.4 (4 points): Apply discount
# If cart_total > 6.00, apply 10% discount
if(cart_total > 6.00):
    discount = cart_total * .10
    cart_total2= cart_total - discount
else:
    discount = 0

# Print the original total and discounted total
print(cart_total)
print(cart_total2)

# Task 4.5 (4 points): Final report
# Print:
# - Items in cart
print(f"Number of items in cart: {len(cart)} ")
# - Number of items
print(f"Number of total items: {len(items)} ")
# - Final total (with discount if applicable)
print(f"Final total without discount: ${cart_total}")
print(f"Final total with discount: ${cart_total2}")