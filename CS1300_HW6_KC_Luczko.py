#CS 1300 - Homework #6
#Name: KC Luczko
#Date: 10/13/2025
#Description: Introduction to Lists
# Example shown for you:
# Create a list of three colors
example_colors = ["red", "blue", "green"]
print("Example:", example_colors)
# Now you try:
# 1. Create a list called 'my_classes' with 4 class names (like "English", "Math",)
my_classes = ["English","Math","Science","History"]
# 2. Create a list called 'my_grades' with 5 test scores (use any numbers between)
my_grades = [66,88,90,92,95]
# 3. Create an empty list called 'my_notes'
my_notes = []
# 4. Print all three of your lists
print(my_classes)
print(my_grades)
print(my_notes)


# Lists can hold different types of data!
# 1. Create a list called 'about_me' with:
about_me = ["KC",18,5.11,True]
# - Your first name (string)
# - Your age (integer)
# - Your height in feet (decimal number like 5.5)
# - Whether you like pizza (True or False)
# 2. Create a list called 'mixed_bag' with:
mixed_bag = [42,"Hello",3.14,[1,2,3]]
# - The number 42
# - The word "Hello"
# - The value 3.14
# - Another list containing [1, 2, 3]
# 3. Print both lists
print(about_me)
print(mixed_bag)


# Method 1: Create a list of 10 zeros using multiplication
# Hint: [0] * 10 creates [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros = [0] * 10
# Method 2: Convert a string to a list of characters
# Convert "HELLO" to ['H', 'E', 'L', 'L', 'O']
letters = list("HELLO")
# Method 3: Create a list that repeats [1, 2] three times
# Result should be [1, 2, 1, 2, 1, 2]
pattern = [1,2] *3
# Print all three lists
#Part 2: Accessing List Elements (20 points)
#Problem 2.1: Reading from Lists (7 points)
# Given this list of months:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
"Nov", "Dec"]
# Access and print these elements:
print("The list:", months)
print("List length:", len(months))
# 1. Print the first month (remember: first element is at index 0)
print("First month:", months[0])
# 2. Print the sixth month (careful with the index!)
print("Sixth month:", months[5])
# 3. Print the last month using positive index (hint: use len() - 1)
print("Last month:", months[len(months) - 1])
# 4. Print the last month using negative index (hint: -1)
print("Last month:", months[-1])
# 5. Print December using its positive index
print("December:", months[11])
# 6. Print January using a negative index
print("January:", months[-12])
# 7. Print the month at index 7
print("Month at index 7:", months[7])

# You're tracking daily temperatures for a week
temperatures = [72, 75, 71, 73, 74, 76, 70] # Sunday through Saturday
print("Original temperatures:", temperatures)
# 1. Monday's temperature was recorded wrong. Change index 1 to 77
temperatures [1] = 77 
# 2. Friday's temperature should be 78 (which index is Friday?)
temperatures [4] = 78
# 3. Change Sunday (first day) to 74
temperatures[0] = 74
# 4. Change Saturday (last day) to 72 using negative index
temperatures [-1] = 72
# 5. Wednesday (middle of week) should be 75
temperatures [2] = 75 
print("Corrected temperatures:", temperatures)
# 6. Calculate and print: how many days are in your list?
print("Days in list", len(temperatures))
# 7. What's the index of the last day? (print it)
print("Index of last day", len(temperatures) - 1)

# Given this small list:
colors = ["red", "blue", "green"]
# 1. Check if index 1 exists before accessing it
if 1 < len(colors):
    print("Color at index 1:", colors[1])
else:
    print("Index 1 doesn't exist")
# 2. Now you try: Check if index 5 exists before trying to access it
if 5 < len(colors):
    print("Color at index 5", colors[5])
else:
    print("Index 5 doesn't exist")
# 3. Check if the list is empty before accessing the first element
if len(colors) > 0:
    print("First element", colors[0])
else:
    print("List is empty")
# 4. Safely access the last element (check if list has at least 1 item first)
if len(colors) >= 1:
    print("Last element", colors[-1])
# 5. Try to print the element at index -4 (but check if it's valid first)
if -4 >= -len(colors):
    print("Element at index -4", colors[-4])
else:
    print("Index -4 is invalid")
# Hint: negative indices from -len(list) to -1 are valid
# 6. What's the smallest valid negative index for this list? Print it.
print("Smallest valid", -len(colors))

# Slicing lets us get multiple elements at once!
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list:", numbers)
print("Remember: list[start:end] gives elements from start up to (but not including) end")
# Example:
print("Example - numbers[0:3]:", numbers[0:3]) # Gets indices 0, 1, 2
# Now you try:
# 1. Get the first 4 numbers
print("First 4 numbers", numbers[0:4])
# 2. Get the last 3 numbers (use negative indices)
print("Last 3 numbers", numbers[-3:])
# 3. Get numbers from index 2 to index 6 (30, 40, 50, 60)
print("Index 2 to 6", numbers[2:7])
# 4. Get all numbers from index 5 to the end
print("Index 5 to end", numbers[5:])
# 5. Get all numbers from start up to index 4
print("Start to index 4", numbers[:5])
# 6. Make a complete copy of the list using [:]
print("copy", numbers[:])
# 7. Get an empty slice (like numbers[3:3]) and see what happens
print("Empty slice", numbers[3:3])

# We can use a step value: list[start:end:step]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print("Alphabet:", alphabet)
# Example:
print("Every other letter:", alphabet[::2]) # Start to end, step by 2
# Now you try:
# 1. Get every third letter starting from 'a' (indices 0, 3, 6, 9, 12)
print("Every third letter", alphabet[::3])
# 2. Get every other letter starting from 'b' (indices 1, 3, 5, 7, ...)
print("Every other starting from 'b'", alphabet[1::2])
# 3. Reverse the entire list using slicing (hint: use step of -1)
print("Reversed", alphabet[::-1])
# 4. Get the first half of the alphabet
mid = len(alphabet) // 2
print("First half", alphabet[:mid])
# Hint: Calculate middle index using len() // 2
# 5. Get the second half of the alphabet
print("Second half:", alphabet[mid:])
# 6. Get letters from index 2 to 8, but only every other one
print("Index 2 to 8, every other:", alphabet[2:9:2])
# 7. Reverse just the first 5 letters (get them, then reverse)
print("First 5 letters reversed:", alphabet[:5][::-1])

# You have hourly temperature readings for a day (24 hours)
hourly_temps = [55, 54, 53, 52, 52, 54, 58, 62, 66, 70, 73, 75,76, 77, 77, 76, 74, 71, 68, 65, 62, 59, 57, 55]
print(f"24-hour temperature data ({len(hourly_temps)} readings)")
# 1. Get morning temperatures (first 6 hours, 12am-5am)
print("Morning:", hourly_temps[:6])
# 2. Get afternoon temperatures (12pm-5pm, which is indices 12-17)
print("Afternoon:", hourly_temps[12:18])
# 3. Get evening temperatures (last 6 hours, 6pm-11pm)
print("Evening:", hourly_temps[-6:])
# 4. Get every other hour's temperature for the whole day
print("Every other hour", hourly_temps[::2])
# 5. Get the middle 4 hours of the day (hours 10-13, so indices 10-14)
print("Middle 4 hours", hourly_temps[10:14])
# 6. What were the temperatures for hours 6-9am? (indices 6-9)'
print("6-9am", hourly_temps[6:10])

# append() adds ONE item to the end of a list
shopping_list = []
print("Starting with empty list:", shopping_list)
# Add these items one at a time using append():
# 1. Add "milk"
shopping_list.append("milk")
# 2. Add "bread"
shopping_list.append("bread")
# 3. Add "eggs"
shopping_list.append("eggs")
# 4. Add "cheese"
shopping_list.append("cheese")
# 5. Add "apples"
shopping_list.append("apples")

print("Final shopping list:", shopping_list)
# 6. What happens if you try to append two items at once?
# Try: shopping_list.append("butter", "yogurt")
# Comment out the line after you see the error!
# 7. Create a list with your 3 favorite foods using append()
favorites = []
favorites.append("Pizza")
favorites.append("Ice_cream")
favorites.append("Tacos")
# Add your three favorites here
print("My favorites:", favorites)

# insert() adds an item at a specific position
line = ["Alice", "Bob", "Charlie"]
print("Original line:", line)
# 1. David cuts to the front! Insert "David" at index 0
line.insert(0, "David")
print("After David cuts:", line)
# 2. Eve joins between Alice and Bob (what index?)
line.insert(2, "Eve")
print("After Eve joins:", line)
# 3. Frank joins at the end (what index? Use len())
line.insert(len(line), "Frank")
print("Final line:", line)
# Now create a schedule:
schedule = ["Math", "History", "Science"]
print("\nOriginal schedule:", schedule)
# 4. Add "Lunch" between History and Science
schedule.insert(2,"Lunch")
# 5. Add "Homeroom" at the beginning
schedule.insert(0,"Homeroom")
print("Updated schedule:", schedule)

# extend() adds ALL items from another list
primary_colors = ["red", "blue", "yellow"]
print("Primary colors:", primary_colors)
# 1. Create a list of secondary colors
secondary_colors = ["green", "orange", "purple"]
# 2. Add all secondary colors to primary_colors using extend()
primary_colors.extend(secondary_colors)
print("All colors:", primary_colors)

# Compare append vs extend:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# 3. Append [4, 5] to list1 (this adds the list as one item!)
list1.append([4, 5])
print("After append([4, 5]):", list1)
# 4. Extend list2 with [4, 5] (this adds each item separately)
list2.extend([4, 5])
print("After extend([4, 5]):", list2)
# 5. Create your own example showing the difference
my_list = ["a", "b"]
my_list.append(["c", "d"])
print("After append", my_list)
my_list = ["a", "b"]
my_list.extend(["c", "d"])
print("After extend:", my_list)
# Try both append and extend with ["c", "d"] and print results

# remove() deletes the FIRST occurrence of a value
pets = ["dog", "cat", "bird", "cat", "fish", "cat"]
print("Original pets:", pets)
# 1. Remove "bird"
pets.remove("bird")
print("After removing bird:", pets)
# 2. Remove "cat" (notice it only removes the first one!)
pets.remove("cat")
print("After removing one cat:", pets)
# 3. Check if "hamster" is in the list before trying to remove it
if "hamster" in pets:
    pets.remove("hamster")
else:
    print("hamster not found in list")
    # 4. Create a list with duplicate values
numbers = [5, 3, 8, 3, 9, 3, 2]
print("\nNumbers:", numbers)
# 5. Remove all 3's (one at a time, checking each time)
if 3 in numbers:
    numbers.remove(3)
if 3 in numbers:
    numbers.remove(3) 
print("Removed first 3:", numbers)
# Remove the remaining 3's (you'll need more if statements)

# pop() removes AND RETURNS an item by index
stack = [10, 20, 30, 40, 50]
print("Original stack:", stack)
# 1. Remove and save the last item
last_item = stack.pop()
print(f"Popped {last_item}, stack is now: {stack}")
# 2. Remove and save the first item (index 0)
first_item = stack.pop(0)
print(f"Popped({first_item}),stack {stack}")
# 3. Remove the item at index 1
stack.pop(1)
print("Current stack:", stack)
# Working with a queue:
queue = ["Person1", "Person2", "Person3", "Person4"]
print("\nQueue:", queue)
# 4. Serve (remove) the first person in line and print who was served
served = queue.pop(0)
print(f"Served: {served}")
# 5. The last person gives up and leaves (remove but don't save)
queue.pop()
print("Remaining queue:", queue)

# del can remove items by index or slice
data = [100, 200, 300, 400, 500, 600, 700]
print("Original data:", data)
# 1. Delete the first element using del
del data[0]
print("After deleting first:", data)
# 2. Delete the element at index 2
del data[2]
print("After deleting index 2:", data)
del data[1:3]
# 3. Delete a slice from index 1 to 3 (not including 3)
print("After deleting slice:", data)
# Working with unwanted data:
readings = [0, 5, -999, 10, 15, -999, 20] # -999 represents bad data
print("\nReadings with errors:", readings)
# 4. Find and remove the first -999 using remove()
readings.remove(-999)
if -999 in readings:
    readings.remove(-999)
# 5. Check if there are more -999 values and remove them
print("Clean readings:", readings)

# Check if items are in a list
valid_grades = ['A', 'B', 'C', 'D', 'F']
print("Valid grades:", valid_grades)
# 1. Check if 'B' is a valid grade
print("'B' is valid?", 'B' in valid_grades)
# 2. Check if 'E' is NOT a valid grade
print("'E' is NOT valid?", 'E' not in valid_grades)
# 3. Ask user for a grade and check if it's valid
user_grade = 'C' # Pretend user entered this
# Check if user_grade is in valid_grades
print("User grade valid?", user_grade in valid_grades)
# Working with a menu:
menu_options = [1, 2, 3, 4, 5]
print("\nMenu options:", menu_options)
# 4. Check if option 3 is available
print("Option 3 available?", 3 in menu_options)
# 5. Check if option 9 is NOT available
print("Option 9 not available?", 9 not in menu_options)
# Student roster:
enrolled = ["Alice", "Bob", "Charlie", "Diana"]
print("\nEnrolled students:", enrolled)
# 6. Check if "Eve" needs to be added (not in list)
if "Eve" not in enrolled:
    print("Eve needs to be added.")
# 7. Only add "Frank" if not already enrolled
if "Frank" not in enrolled:
    enrolled.append("Frank")
# 8. Create a list of students to check
to_check = ["Alice", "Eve", "Bob", "George"]
# For each student, print whether they're enrolled or not
print("Alice enrolled", "Alice" in enrolled)
print("Eve enrolled", "Eve" in enrolled)
print("Bob enrolled", "Bob" in enrolled)
print("George enrolled", "George" in enrolled)
# (Do this without loops - check each one individually)


# len() tells us how many items are in a list
tasks = ["homework", "dishes", "laundry", "shopping", "exercise"]
print("Tasks:", tasks)
# 1. How many tasks are there?
print("Number of tasks", len(tasks))
# 2. What's the index of the last task? (remember: len() - 1)
print("Index of last task", len(tasks) - 1)
# 3. Check if list has more than 3 tasks
if len(tasks) > 3:
    print("More than 3 tasks")
# 4. Calculate the middle index
middle_index = len(tasks) // 2
print("Middle index", middle_index)
# 5. Access the middle task safely
print("Middle task", tasks[middle_index])
# Empty list checks:
inbox = []
print("\nInbox:", inbox)
# 6. Check if inbox is empty (two ways)
# Way 1: Check if len() == 0
if len(inbox) == 0:
    print("Inbox is empty (using len check)")
# Way 2: Empty lists are "falsy"
if not inbox:
    print("Inbox is empty (using 'not inbox')")
# 7. Create a waiting list with max capacity of 4
waiting = ["P1", "P2"]
max_capacity = 4
print(f"\nWaiting list ({len(waiting)}/{max_capacity}):", waiting)
# How many more can join?
spaces_available = max_capacity - len(waiting)
print(f"Spaces available: {spaces_available}")
# Add two more if there's room
if len(waiting) < max_capacity:
    waiting.append("P3")
if len(waiting) < max_capacity:
    waiting.append("P4")
print(f"Updated waiting list ({len(waiting)}/{max_capacity}):", waiting)

# Starting inventory
inventory = ["apples", "bananas", "milk", "bread", "eggs"]
quantities = [10, 15, 5, 8, 24] # Matching quantities for each item
print("== Store Inventory System ==")
print("Items:", inventory)
print("Quantities:", quantities)
print()
# Print each item with its quantity (use indexing, not loops)
# Task 1: Display the inventory nicely
print("Current Inventory:")
# Print first item and quantity
print(inventory[0], "-", quantities[0])
# Print second item and quantity
print(inventory[1], "-", quantities[1])
print(inventory[2], "-", quantities[2])
print(inventory[3], "-", quantities[3])
print(inventory[4], "-", quantities[4])
# ... continue for all items
# Task 2: A customer buys 3 apples
quantities[0] -= 3
# Find apples (index 0) and reduce quantity by 3
# Task 3: Restock milk
quantities[2] += 10
# Milk is at index 2, add 10 more
# Task 4: Add a new item
inventory.append("cheese")
quantities.append(12)
# Add "cheese" to inventory with quantity 12
# Task 5: Remove items with 0 quantity
if quantities[0] <= 0:
    del inventory[0]
    del quantities[0]


if quantities[1] <= 0:
    del inventory[1]
    del quantities[1]


if quantities[2] <= 0:
    del inventory[2]
    del quantities[2]


if quantities[3] <= 0:
    del inventory[3]
    del quantities[3]


if quantities[4] <= 0:
    del inventory[4]
    del quantities[4]


# If any quantity is 0 or less, remove both the item and quantity
# (Check each one individually since we can't use loops)
# Task 6: Report
print("\nInventory:")
print("Total different items ", len(inventory))
# Print total number of different items (use len())
if quantities[0] < 5:
    print(inventory[0], "needs restock!")
if quantities[1] < 5:
    print(inventory[1], "needs restock!")
if quantities[2] < 5:
    print(inventory[2], "needs restock!")
if quantities[3] < 5:
    print(inventory[3], "needs restock!")
if quantities[4] < 5:
    print(inventory[4], "needs restock!")
# Print items that need restocking (quantity < 5)
# Check each item individually
print("\nFinal Inventory:")
print("Items:", inventory)
print("Quantities:", quantities)
# Print the updated inventory and quantities