# lab2_2.py
# Week 2 Session 2 Lab
# KC Luczko
# 8/28/2025
print("=" * 50)
print("WEEK 2 SESSION 2 LAB")
print("=" * 50)
# Problem 1: Age Calculator
print("\n--- Problem 1: Age Calculator ---")
birth_year = int(input("Enter your birth year: "))
age = 2024 - birth_year
print(f"You are {age} years old in 2024.")
# Test with: 2000 → Should output: You are 24 years old in 2024.

# Problem 2: Temperature Converter
print("\n--- Problem 2: Temperature Converter ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
# Test with: 25 → Should output: 25.0°C = 77.0°F

#Problem 3: Rectangle Measurements
print("\n--- Problem 3: Rectangle Measurements ---")
length = float(input("Enter Length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")
# Test with: length=5.5, width=3.2
# Should output: Area: 17.60, Perimeter: 17.40

#Problem 4: Bill Calculator
print("\n--- Problem 4: Bill Calculator ---")
meal = float(input("Enter meal cost:"))
tip_percent = float(input("Enter tip percentage: "))
tip = meal * (tip_percent / 100)
total = meal + tip
print(f"Meal: ${meal:.2f}, Tip: ${tip:.2f}, Total: ${total:.2f}")
# Test with: meal=$50, tip=20%
# Should output: Meal: $50.00, Tip: $10.00, Total: $60.00

#Problem 5: Student Info Display
print("\n--- Problem 5: Student Info Display ---")
name = input("Enter name: ")
age = input("Enter age: ")
major = input("Enter major: ")

print(name, age, major)
print(name, age, major, sep=", ")
print(name, age, major, sep= " | ")
# Test with: Alice, 20, Computer Science
# Should show three different formats

#Problem 6: Progress Indicator
print("\n--- Problem 6: Progress Indicator ---")
print("Processing", end="")
for _ in range(5):
    print(".", end="")
print(" Complete!")
# Should output: Processing..... Complete!

#Problem 7: Data Table Header
print("\n--- Problem 7: Data Table Header ---")
print("=" * 40)
print ("name\tscore\tgrade")
print("=" * 40)
name = input("Enter name: ")
score = input("Enter Score : ")
grade = input ("Enter grade: ") 
print (f"{name}\t{score}\t{grade}")
# Should create a simple table structure

#Problem 8: Message Box
print("\n--- Problem 8: Message Box ---")
message = input(" Enter a short message: ")
print("+"+"-" * 30 + "+")
print(f"| {message:<28} |")
print("+"+"-" * 30 + "+")
# Test with: "Hello World"
# Should create a box around the message

#Problem 9: Price Display
print("\n--- Problem 9: Price Display ---")
item = input("Enter item name: ")
price = float(input("Enter price: "))
print(f"{item} ${price:>.2f}")
# Test with: Apple, 1.5
# Should output: Apple $ 1.50

#Problem 10: Percentage Calculator
print("\n--- Problem 10: Percentage Calculator ---")
earned = float(input("Enter earned points: "))
total = float(input("Enter total points avaliable : "))
percentage = (earned / total) * 100
print(f"Score: {int(earned)}/{int(total)} = {percentage:.1f}%")
# Test with: 85 out of 100
# Should output: Score: 85/100 = 85.0%

#Problem 11: Receipt Line Item
print("\n--- Problem 11: Receipt Line Item ---")
product = input("Enter product: ")
quantity = int(input("Enter quantity: "))
Unit_price = float(input("Enter unit price: "))
total = quantity * Unit_price
print(f"{product:<20}{str(quantity):^10}${total:>10.2f}")
# - Product left-aligned (20 chars)
# - Quantity centered (10 chars)
# - Total right-aligned with $ (10 chars)
# Test with: Notebook, 3, 2.50
# Output: Notebook 3 $ 7.50

#Problem 12: ID Formatter
print("\n--- Problem 12: ID Formatter ---")
number = int(input("Enter a number: "))
print(f"4-digit: {number:04d}")
print(f"6-digit: {number:06d}")
print(f"8-digit: {number:08d}")
# Test with: 42
# Should output:
# 4-digit: 0042
# 6-digit: 000042
# 8-digit: 00000042
# I just wanted to say thank you for putting the steps its really helping learn python. I would be lost where to start most of these without it :)
# git commit -m "Complete week 2 session 2 lab"