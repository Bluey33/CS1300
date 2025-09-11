# CS 1300 WEEK 3 LAB 1
# KC luczko
# 9 / 10 / 2025
print("=== Memory Investigation ===")
# Create variables with small integers
a = 100
b = 100
print(f"a = {a}, memory address = {id(a)}")
print(f"b = {b}, memory address = {id(b)}")
print(f"a and b same object? {id(a) == id(b)}")
print()
# Create variables with large integers
c = 1000
d = 1000
print(f"c = {c}, memory address = {id(c)}")
print(f"d = {d}, memory address = {id(d)}")
print(f"c and d same object? {id(c) == id(d)}")
print()
# Create variables with strings
e = "Python"
f = "Python"
print(f"e = '{e}', memory address = {id(e)}")
print(f"f = '{f}', memory address = {id(f)}")
print(f"e and f same object? {id(e) == id(f)}")
# Q1: Why do a and b share the same memory address?
# Your answer: You assign a and b the same value and its small enough so its the samew
# Q2: Why might c and d have different memory addresses?
# Your answer: c and d are assigned 1000 which is outside of the small range so it can have multiple different addresses
# Q3: What happens with string variables e and f?
# Your answer: they get stored once and e and f both call to python 


print("\n=== Variable References ===")
# Create a variable
original = 500
print(f"original = {original}, id = {id(original)}")
# Create a reference to the same object
reference = original
print(f"reference = original")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Same object? {id(original) == id(reference)}")
print()
# Now modify original
original = original + 100
print("After: original = original + 100")
print(f"original = {original}, id = {id(original)}")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Still same object? {id(original) == id(reference)}")
# YOUR TURN: Create your own example with strings
word = "hi"
print(f"word = {word},id = {id(word)}")
word2 = word
print(f"word2 = word")
print(f"word2 = {word2}, id = {id(word2)}")
print(f"Same object? {id(word) == id(word2)}")

word = word + word2
print("After: word = word + word2")
print(f"word = {word}, id = {id(word)}")
print(f"word2 = {word2}, id = {id(word2)}")
print(f"Still same object? {id(word) == id(word2)}")


print("\n=== Memory Changes with Operations ===")
# Track memory changes with different operations
x = 200
print(f"Initial: x = {x}, id = {id(x)}")
# Save the original id
original_id = id(x)
# Try different operations and check if id changes
x = x + 50
print(f"After x = x + 50: x = {x}, id = {id(x)}, did it change? {id(x) != original_id}")
# Test 1: Multiplication
x = 200
original_id = id(x)
x = x * 2
print(f"After x = x * 2: x = {x}, id = {id(x)}, did it change? {id(x) != original_id}")

# Test 2: Subtraction
x = 200
original_id = id(x)
x = x - 100
print(f"After x = x - 100: x = {x}, id = {id(x)}, did it change? {id(x) != original_id}")

# Test 3: Division
x = 200
original_id = id(x)
x = x / 2
print(f"After x = x / 2: x = {x}, id = {id(x)}, did it change? {id(x) != original_id}")

# Test 4: Floor division
x = 200
original_id = id(x)
x = x // 3
print(f"After x = x // 3: x = {x}, id = {id(x)}, did it change? {id(x)!= original_id}")

# Test 5: Modulo
x = 200
original_id = id(x)
x = x % 7
print(f"After x = x % 7: x = {x}, id = {id(x)}, did it change? {id(x) != original_id}")


print("\n=== Compound vs Regular Assignment ===")
# Compare regular and compound assignment
print("Regular assignment:")
a = 10
print(f"Start: a = {a}")
a = a + 5
print(f"After a = a + 5: a = {a}")
a = a * 2
print(f"After a = a * 2: a = {a}")
a = a - 3
print(f"After a = a - 3: a = {a}")
print()
print("Compound assignment:")
b = 10
print(f"Start: b = {b}")
b += 5
print(f"After b += 5: b = {b}")
b *= 2
print(f"After b *= 2: b = {b}")
b -= 3
print(f"After b -= 3: b = {b}")
# YOUR TURN: Complete using compound operators
print("\nYour turn - use compound operators:")
c = 100
print(f"Start: c = {c}")
c += 25
print(f"After adding 25: c = {c}")
# Divide c by 5 using compound operator
c /= 5
print(f"After dividing by 5: c = {c}")
# Get remainder when c is divided by 7 using compound operator
c%= 7
print(f"After modulo 7: c = {c}")

print("\n=== Building a Total ===")
# Calculate a restaurant bill
bill = 0.0
print(f"Starting bill: ${bill:.2f}")
# Add items using compound operators
appetizer = 12.99
bill += appetizer
print(f"Added appetizer (${appetizer}): ${bill:.2f}")
entree = 24.50
bill += entree
print(f"Added entree (${entree}): ${bill:.2f}")
dessert = 8.99
bill += dessert
print(f"Added dessert (${dessert}): ${bill:.2f}")
# YOUR TURN: Complete the bill calculation
# Calculate 20% tip (multiply bill by 0.20)
tip = bill *0.20
print(f"Tip (20%): ${tip:.2f}")
# Add tip to bill using compound operator
bill += tip
print(f"Total with tip: ${bill:.2f}")
# Calculate 8.5% tax on the original bill (before tip)
# Note: You'll need to recalculate the original bill amount
original_bill = appetizer + entree + dessert
tax = original_bill * 0.085
print(f"Tax (8.5%): ${tax:.2f}")
# Add tax to bill using compound operator
bill += tax
print(f"Final total: ${bill:.2f}")


print("\n=== String Building ===")
# Build a message using compound operators
message = "Shopping list"
print(f"1. message = '{message}'")
message += ":"
print(f"2. After += ':' -> '{message}'")
message += " apples"
print(f"3. After += ' apples' -> '{message}'")
# YOUR TURN: Continue building the shopping list
# Add ", bananas" to message
message += ", bananas"
print(f"4. After adding bananas -> '{message}'")
# Add ", milk" to message
message += ", milk"
print(f"5. After adding milk -> '{message}'")
# Add ", bread" to message
message += ", bread"
print(f"6. Final list -> '{message}'")
# Check memory - does += create a new string?
original_message = "Test"
original_id = id(original_message)
original_message += " String"
new_id = id(original_message)
print(f"\nString memory test:")
print(f"Original id: {original_id}")
print(f"After += id: {new_id}")
print(f"Same object? {original_id == new_id}")


print("\n=== Operator Precedence - Predict First! ===")
# For each expression:
# 1. Write your prediction
# 2. Run the code
# 3. Explain why you got that result
# Example:
# Prediction: 14
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")
print("Explanation: Multiplication happens before addition\n")
# YOUR TURN - Predict before running:
# Prediction: 4
result1 = 10 - 2 * 3
print(f"10 - 2 * 3 = {result1}")
# Explanation: multiplication has a higher precendence than subtraction does so 2*3 happens then 10-6
# Prediction: 24
result2 = (10 - 2) * 3
print(f"(10 - 2) * 3 = {result2}")
# Explanation: parentheses force subtraction first then 8*3 happens 
# Prediction: 32
result3 = 2 ** 3 * 4
print(f"2 ** 3 * 4 = {result3}")
# Explanation: it goes 2**3 which is 2*2*2 then 8 *4 = 32
# Prediction: no clue
result4 = 2 ** (3 * 4)
print(f"2 ** (3 * 4) = {result4}")
# Explanation: its 4096 because parentheses make it 3*4 so then its 2 **12 or the twelth power of 2
# Prediction: 50.0
result5 = 100 / 10 * 5
print(f"100 / 10 * 5 = {result5}")
# Explanation:division and multiplication is equal so its left to right reading
# Prediction: 2.0
result6 = 100 / (10 * 5)
print(f"100 / (10 * 5) = {result6}")
# Explanation: parentheses then division


print("\n=== Fix the Expression with Parentheses ===")
# Each calculation is wrong. Add parentheses to fix it.
# Goal: Calculate the average of 10 and 20
wrong_avg = 10 + 20 / 2
print(f"Wrong average: {wrong_avg}")
# YOUR FIX:
fixed_avg = (10 + 20) / 2
print(f"Fixed average: {fixed_avg}")
# Goal: Calculate 5% of 200
wrong_percent = 5 / 100 * 200
print(f"Wrong calculation: {wrong_percent}")
# YOUR FIX:
fixed_percent = 200 * (5 / 100)
print(f"Fixed calculation: {fixed_percent}")
# Goal: Convert 75 minutes to hours (divide by 60)
wrong_hours = 75 / 60 * 60
print(f"Wrong hours: {wrong_hours}")
# YOUR FIX:
fixed_hours = 75 / 60
print(f"Fixed hours: {fixed_hours}")

print("\n=== Understanding Division Operations ===")
# Regular division (/)
print("Regular division (/):")
print(f"17 / 5 = {17 / 5}")
print(f"20 / 4 = {20 / 4}")
print(f"Type of 20 / 4: {type(20 / 4)}")
print()
# Floor division (//)
print("Floor division (//):")
print(f"17 // 5 = {17 // 5}")
print(f"20 // 4 = {20 // 4}")
print(f"Type of 20 // 4: {type(20 // 4)}")
print()
# Modulo (%)
print("Modulo (%):")
print(f"17 % 5 = {17 % 5}")
print(f"20 % 4 = {20 % 4}")
print()
# YOUR TURN: Calculate these
numerator = 23
denominator = 7
regular_div = numerator / denominator
floor_div = numerator // denominator
remainder = numerator % denominator
print(f"{numerator} / {denominator} = {regular_div}")
print(f"{numerator} // {denominator} = {floor_div}")
print(f"{numerator} % {denominator} = {remainder}")
# Verify: numerator should equal (floor_div * denominator) + remainder
verification = (floor_div * denominator) + remainder
print(f"Verification: {floor_div} * {denominator} + {remainder} = {verification}")


print("\n=== Time Conversion ===")
# Convert total seconds to hours, minutes, seconds
total_seconds = 7325
print(f"Converting {total_seconds} seconds:")
# Calculate hours
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
print(f"Hours: {hours}")
print(f"Remaining seconds: {remaining_seconds}")
# Calculate minutes from remaining seconds
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print(f"Result: {hours} hours, {minutes} minutes, {seconds} seconds")
# YOUR TURN: Convert 9876 seconds
total_seconds_2 = 9876
print(f"\nConverting {total_seconds_2} seconds:")
# Calculate hours
hours_2 = total_seconds_2 // 3600
remaining_2 = total_seconds_2 % 3600
# Calculate minutes
minutes_2 = remaining_2 // 60
seconds_2 = remaining_2 % 60
print(f"Result: {hours_2} hours, {minutes_2} minutes, {seconds_2} seconds")



print("\n=== Making Change ===")
# Calculate coins needed for given cents
cents = 287
print(f"Making change for {cents} cents:")
# Calculate quarters (25 cents)
quarters = cents // 25
remaining = cents % 25
print(f"Quarters: {quarters}, Remaining: {remaining} cents")
# Calculate dimes (10 cents)
dimes = remaining // 10
remaining = remaining % 10
print(f"Dimes: {dimes}, Remaining: {remaining} cents")
# Calculate nickels (5 cents)
nickels = remaining // 5
pennies = remaining % 5
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")
# YOUR TURN: Calculate change for 193 cents
cents_2 = 193
print(f"\nMaking change for {cents_2} cents:")
quarters_2 = cents_2 // 25
remaining_2 = cents_2 % 25
dimes_2 = cents_2 // 10
remaining_2 = remaining_2 % 10
nickels_2 = remaining_2 // 5 
pennies_2 = remaining_2 % 5
print(f"Quarters: {quarters_2}")
print(f"Dimes: {dimes_2}")
print(f"Nickels: {nickels_2}")
print(f"Pennies: {pennies_2}")
# Verify your answer
total_check = (quarters_2 * 25) + (dimes_2 * 10) + (nickels_2 * 5) + pennies_2
print(f"Verification: {total_check} cents")


print("\n=== Unit Conversion Calculator ===")
# Convert miles to various units
miles = 5.5
print(f"Starting with: {miles} miles")
# Convert to feet (1 mile = 5280 feet)
feet = miles * 5280
print(f"In feet: {feet:.1f} feet")
# Convert to yards (1 mile = 1760 yards)
yards = miles * 1760
print(f"In yards: {yards:.1f} yards")
# Convert to kilometers (1 mile = 1.60934 km)
kilometers = miles * 1.60934
print(f"In kilometers: {kilometers:.2f} km")
# Convert to meters (using the km value)
meters = kilometers
meters *= 1000
print(f"In meters: {meters:.2f} meters")
# YOUR TURN: Convert temperature
# Convert 75°F to Celsius and Kelvin
fahrenheit = 75
print(f"\n=== Temperature Conversion ===")
print(f"Starting with: {fahrenheit}°F")
# Convert to Celsius: C = (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9
print(f"In Celsius: {celsius:.1f}°C")
# Convert to Kelvin: K = C + 273.15
kelvin = celsius # Start with celsius value
kelvin += 273.15
print(f"In Kelvin: {kelvin:.1f} K")
# YOUR TURN: Data Storage Units
# Convert 2.5 GB to other units
gigabytes = 2.5
print(f"\n=== Data Storage Conversion ===")
print(f"Starting with: {gigabytes} GB")
# Convert to MB (1 GB = 1024 MB)
megabytes = gigabytes * 1024
print(f"In Megabytes: {megabytes:.0f} MB")
# Convert to KB (use MB value, 1 MB = 1024 KB)
kilobytes = megabytes
# Multiply by 1024 using compound operator
kilobytes *= 1024
print(f"In Kilobytes: {kilobytes:.0f} KB")
# Convert to bytes (use KB value, 1 KB = 1024 bytes)
bytes_total = kilobytes
bytes_total *= 1024
# Multiply by 1024 using compound operator
print(f"In Bytes: {bytes_total:.0f} bytes")
# Convert to bits (1 byte = 8 bits)
bits = bytes_total
# Multiply by 8 using compound operator
bits *= 8
print(f"In Bits: {bits:.0f} bits")



print("\n=== BONUS: Compound Interest with Memory Tracking ===")
# Calculate compound interest and track memory changes
principal = 1000.00
rate = 0.05 # 5% annual
years = 3
print(f"Initial investment: ${principal:.2f}")
print(f"Annual rate: {rate*100}%")
print(f"Investment period: {years} years\n")
# Track the principal's memory address
print(f"Principal memory address: {id(principal)}")
# Year 1
amount = principal
print(f"Year 0: ${amount:.2f}")
amount *= (1 + rate)
print(f"Year 1: ${amount:.2f} (memory: {id(amount)})")
# Year 2
amount *= (1 + rate)
print(f"Year 2: ${amount:.2f} (memory: {id(amount)})")
# Year 3
amount *= (1 + rate)
print(f"Year 3: ${amount:.2f} (memory: {id(amount)})")
# Calculate total interest earned
interest = amount - principal
print(f"\nTotal interest earned: ${interest:.2f}")
print(f"Return on investment: {(interest/principal)*100:.1f}%")
# Memory analysis
print(f"\nOriginal principal still: ${principal:.2f}")
print(f"Principal unchanged at memory: {id(principal)}")
print(f"Final amount at different memory: {id(amount)}")
# YOUR TURN: Calculate monthly compound interest
# $500 initial, 6% annual rate (0.5% monthly), 6 months
monthly_principal = 500.00
monthly_rate = 0.06 / 12 # Convert annual to monthly
months = 6
print(f"\n=== Your Monthly Calculation ===")
print(f"Initial: ${monthly_principal:.2f}")
print(f"Monthly rate: {monthly_rate*100:.1f}%")
# Calculate compound interest for 6 months\
amount = monthly_principal
print(f"Month 0: ${amount:.2f}")

amount *= (1 + monthly_rate)
print(f"Month 1: ${amount:.2f} (memory: {id(amount)})")

amount *= (1 + monthly_rate)
print(f"Month 2: ${amount:.2f} (memory: {id(amount)})")

amount *= (1 + monthly_rate)
print(f"Month 3: ${amount:.2f} (memory: {id(amount)})")

amount *= (1 + monthly_rate)
print(f"Month 4: ${amount:.2f} (memory: {id(amount)})")

amount *= (1 + monthly_rate)
print(f"Month 5: ${amount:.2f} (memory: {id(amount)})")

amount *= (1 + monthly_rate)
print(f"Month 6: ${amount:.2f} (memory: {id(amount)})")

# Remember: each month, multiply by (1 + monthly_rate)
interest = amount - monthly_principal
print(f"\nTotal interest earned: ${interest:.2f}")
print(f"Return on investment: {(interest / monthly_principal) * 100:.1f}%")
