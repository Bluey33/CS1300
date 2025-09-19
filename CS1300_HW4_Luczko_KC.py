#CS1300 - Homework 4: Decision Structures I
#Name: KC Luczko
#Date: 9/19/2025
#Description: Programs using conditional statements for decision-making

print("=== Temperature Converter & Weather Advisor ===")
# Get temperature from user
temp = float(input("Enter temperature: "))
# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()
# YOUR CODE HERE
if scale == "C":
    far_temp = (temp *9/5) + 32
    cel_temp = temp
elif scale == "F":
    cel_temp = (temp - 32 ) * 5/9
    far_temp = temp
else: 
    print("Bad input not a weather scale.")

print(f"temperature in celsius: {cel_temp:.1f}")
print(f"temperature in fahrenheit: {far_temp:.1f}")

if far_temp <= 32:
    print(" Freezing, bundle up warmly!")
elif far_temp <= 50:
    print("Cold, wear a warm jacket")
elif far_temp <= 70:
    print(" cool, a light jacket would be nice")
elif far_temp <= 85:
    print("Pleasent, Enojoy the weather")
else:
    print("Hot, Stay hydrated")
# 2. Convert to the other scale
# 3. Display both temperatures
# 4. Give weather advice based on Fahrenheit


print("=== Movie Theater Ticket System ===")


age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()

if day == "tuesday":
    print("Your ticket price: $7.00 - Tuesday Special!!!")
else:
    showtime = int(input("Enter show time (in 24hr format): "))

    if age <= 12:
        price = 8.00
    elif age > 65:
        price = 10.00
    else:
        price = 15.00

    if showtime < 17:
        price -= 3.00
    print("Matinee discount applied: -$3.00")

    print(f"Your ticket price: ${price:.2f}")



print("=== Grade Calculator ===")
# Get three test scores
test1 = float(input("Enter Test 1 score (0-100): "))
test2 = float(input("Enter Test 2 score (0-100): "))
test3 = float(input("Enter Test 3 score (0-100): "))
# YOUR CODE HERE
if not (0 <= test1 <= 100 and 0 <= test2 <= 100 and 0 <= test3 <= 100):
    print("Error all test scores have to be within 0 and 100: ")
average = (test1 + test2 +test3) / 3

if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"
if letter!= "F" and (test1 >= 60 or test2 >= 60 or test3 >= 60):
    grade = "PASS"
else:
    grade = "FAIL"

print(f"Average score: {average:.2f}")
print(f"Letter grade: {letter}")
print(f"PASS OR FAIL: {grade}")

print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
criteria_met = 0
feedback = []
common_passwords = ["password", "12345678", "qwerty"]
if len(password) > 8:
    criteria_met += 1
else:
    feedback.append("Password should be at least 8 characters long: ")

if password.lower() != password:
    criteria_met += 1
else:
    feedback.append("Include at least one uppercase letter:")

if password.upper() != password:
    criteria_met += 1
else:
    feedback.append("Include at least one lowercase letter: ")

if any(char.isdigit() for char in password):
    criteria_met += 1
else:
    feedback.append("Include at least one digit: ")

if password.lower() not in common_passwords:
    criteria_met += 1
else:
    feedback.append("Avoid using common passwords: ")

if criteria_met <= 2:
    strength = "Weak"
elif criteria_met == 3:
    strength = "Fair"
elif criteria_met == 4:
    strength = "Good"
else:
    strength = "Strong"


print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for item in feedback:
        print(item)
else:
    print("Great job Your password meets all criteria.")


print("=== Restaurant Bill Calculator ===")
original_food_total = float(input("Enter food total: $"))
food_total = original_food_total
is_holiday = input("Is today a holiday? yes or no : ").lower()
party_size = int(input("How many people in your party? "))

holiday_charge = 0
if is_holiday == "yes":
    holiday_charge = food_total * 0.15
    food_total += holiday_charge

has_membership = input("Are you a member? yes or no: ").lower()
member_discount = 0
if has_membership == "yes":
    member_discount = food_total * 0.10
    food_total -= member_discount

day_of_week = input("What day is it? ").lower()
senior_discount = 0
if day_of_week == "wednesday":
    has_seniors = input("Do you have seniors in your party yes or no : ").lower()
    if has_seniors == "yes":
        senior_discount = food_total * 0.10
        food_total -= senior_discount

tax = food_total * 0.085
food_totalwithtax = food_total + tax

gratuity = 0
if party_size >= 6:
    gratuity = (food_total / (1 + 0.085)) * 0.18

final_total = food_totalwithtax + gratuity

print("Bill Breakdown")
print(f"Food Total: ${original_food_total:.2f}")
if holiday_charge > 0:
    print(f"Holiday Surcharge 15%: +${holiday_charge:.2f}")
if member_discount > 0:
    print(f"Member Discount 10%: -${member_discount:.2f}")
if senior_discount > 0:
    print(f"Senior Discount 10%: -${senior_discount:.2f}")
print(f"Subtotal: ${food_total:.2f}")
print(f"Tax (8.5%): ${tax:.2f}")
if gratuity > 0:
    print(f"Gratuity (18%): ${gratuity:.2f}")
print(f"Total: ${final_total:.2f}")
if final_total > 120:
    print("You are big back haha: ")
print("Thank you for dining with us: ")
