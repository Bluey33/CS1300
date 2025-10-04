#CS1300- Homework #5: advanced control structures
#name KC Luczko
#date 10/4/2025
#description advanced conditional logic and validation

print("=== SMART THERMOSTAT SYSTEM ===")
# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()
# YOUR CODE HERE
# 1. Check if current temp is in comfortable range using chained comparison
if 68 <= current_temp <= 76:
    print("Current temperature is within the comfortable range! : ")
else:
    print("Current temperature is not withing comfortable range : ")
# 2. Determine if it's night time (22-6)
night_time = hour >= 22 or hour <= 6
# 3. Apply seasonal restrictions
ideal_temp = desired_temp
# 4. Calculate actual target temperature after adjustments
if night_time:
    ideal_temp -= 3
# 5. Calculate time to reach target
if season == "summer" and ideal_temp < 72:
    ideal_temp = 72
if season == "winter" and ideal_temp > 70:
    ideal_temp = 70
adjustment = ideal_temp - current_temp

if adjustment <0:
    change = adjustment * -1
else:
    change = adjustment

if change <= 2:
    efficency = "Excellent"
elif change <= 4:
    efficency = "Good"
elif change <=6:
    efficency = "Fair"
else:
    efficency = "poor"

# 7. Display status and adjustments
print("\nCurrent Status:")
if current_temp < 68:
    print(f"Current temp: {current_temp}F (Too cold)")
elif current_temp > 76:
    print(f"Current temp: {current_temp}F (Too hot)")
else:
    print(f"Current temp: {current_temp}F (Comfortable)")

if night_time:
    print("Night mode: ACTIVE (reducing target by 3F)")
else:
    print("Night mode: INACTIVE")

print(f"Season: {season.lower()} ", end='')
if season == "summer" and desired_temp < 72:
    print("(min 72F allowed)")
elif season == "winter" and desired_temp > 70:
    print("(max 70F allowed)")
else:
    print()

print("Adjustments to the temp:")
print(f"Desired: {desired_temp}F")
night_adjusted_temp = desired_temp - 3 if night_time else desired_temp
print(f"Night adjustment: {night_adjusted_temp}F")
print(f"Seasonal limit applied: {ideal_temp}F")
print(f"Final target: {ideal_temp}F")
if adjustment > 0:
    print(f"Heating required: {adjustment:.0f}F")
else:
    print(f"Cooling required: {(adjustment):.0f}F")

print(f"Estimated time: {change / 2:.1f} hours")
print(f"Efficency {efficency}")

# 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
# Hint: Use chained comparisons like: 68 <= current_temp <= 76
# Hint: Night check needs: hour >= 22 or hour <= 6

print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")
# Initialize score
score = 0
# YOUR CODE HERE
# Use conditional expressions for each check
# Example: length_points = 30 if len(password) >= 16 else 20 if len(password) >=12 else 10 if len(password) >= 8 else 0
# Check length (use conditional expression)
length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
score += length_points
# Check for uppercase (use conditional expression)
has_upper = password != password.lower()
upper_points = 15 if has_upper else 0
score += upper_points
# Check for lowercase
has_lower = password != password.upper()
lower_points = 15 if has_lower else 0
score += lower_points
# Check for number
has_digit = any(c.isdigit() for c in password)
digit_points = 15 if has_digit else 0
score += digit_points

# Check for special characters
has_special = not password.isalnum()
special_points = 15 if has_special else 0
score += special_points

# Check for common patterns
common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
pattern_points = 0 if has_pattern else 10
if not has_pattern:
    score += pattern_points
else: 
    score -= 10
# Calculate total score and determine strength level
if score >= 90:
    strength = "EXCELLENT"
elif score >= 70:
    strength = "GOOD"
elif score >= 50:
    strength = "decent"
else:
    strength ="weak"
# Display detailed analysis
print("Security analysis: ")

print(f"Length: {len(password)} characters ({length_points}/30 points)")
print(f" Uppercase letters: {'yes' if has_upper else 'no'}({upper_points}/15 points)")
print(f" Lowercase letters: {'yes' if has_lower else 'no'}({lower_points}/15 points)")
print(f"Numbers: {'Yes' if has_digit else 'no'}({digit_points}/15 points)")
print(f"Special characters:{"yes" if has_special else "no"}({special_points}/15 points)")
if has_pattern:
    for pattern in common_patterns:
        if pattern in password.lower():
            print(f"Common password found: {pattern} (-10 points)")
            break
else:
    print("No common patterns found (+10 points!)")


print(f"Total score: {score}/100 \n")
print(f"Strength level: {strength}")


print("=== GRADE VALIDATION SYSTEM ===")
# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))
# YOUR CODE HERE
# 1. Validate each score is 0-100 using chained comparisons
# 2. Check for suspicious patterns
# 3. Use truth table logic:
# valid_range AND not_suspicious AND not_identical
# 4. If valid, calculate average, highest, lowest, improvement
# 5. Provide appropriate feedback
# Example validation:
all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)
# Check if all identical
scores = [test1,test2,test3,test4]
all_identical = (test1 == test2 == test3 == test4)
# Check for huge jumps
huge_jump = (
    (test2 - test1 > 40) or (test1 - test2 > 40) or
    (test3 - test2 > 40) or (test2 - test3 >40) or
    (test4 - test3 > 40) or (test3 - test4 >40)
)
perfect_scores = (test1 == 100 and test2 == 100 and test3 == 100 and test4 == 100)
valid = all_valid_range and not all_identical and not huge_jump

print(" validation results: \n")
if all_valid_range:
    print("All scores in valid range 0-100")
else:
    print("One or more scores are out of the range you must enter 0-100")

if all_identical:
    print("all score are all_identical possible cheating detected")
elif huge_jump:
    print("Huge jump dectected between tests >40 points please verify.")
elif perfect_scores:
    print("Perfect scores on all tests must verify")
else:
    print("scores are normal")
# Combine validations using truth table logic
if valid:
    avg = (test1 + test2 + test3 + test4) /4
    highest = max(scores)
    lowest = min(scores)
    improvement = test4 - test1

if improvement > 10:
    trend = "Improving"
elif improvement < -10:
    trend = "declining"
else:
    trend = "stable"

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "d"
else:
    grade = "F"

status ="Passing" if avg >= 60 else "failing"

print("Statistics")
print(f"Average: {avg:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Trend: {trend}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if trend == "Improving":
    print("Performance: Improvement shown!")
elif trend == "Declining":
    print("Performance needs attention. Scores are going down.")
elif trend == "stable":
    print("Performance is stable.")
else:
    print("Validation failed")



print("=== EVENT SCHEDULING SYSTEM ===")

# Event 1
print("\nEVENT 1 DETAILS:")
event1_name = input("Event name: ")
event1_day = input("Day (Mon-Sun): ").lower()[:3]  # First 3 letters
event1_start = float(input("Start time (0-24): "))
event1_end = float(input("End time (0-24): "))

# Event 2
print("\nEVENT 2 DETAILS:")
event2_name = input("Event name: ")
event2_day = input("Day (Mon-Sun): ").lower()[:3]
event2_start = float(input("Start time (0-24): "))
event2_end = float(input("End time (0-24): "))

# 1. Validate times are in range 0-24
# 2. Validate end time > start time for each event
# 3. Check for conflicts using complex conditions
# 4. Calculate gap between events if same day
# 5. Check for early/late scheduling issues

# Valid days
valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# Validation using chained comparisons
event1_valid = (
    event1_day in valid_days and
    (0 <= event1_start <= 24) and
    (0 <= event1_end <= 24) and
    (event1_end > event1_start)
)

event2_valid = (
    event2_day in valid_days and
    (0 <= event2_start <= 24) and
    (0 <= event2_end <= 24) and
    (event2_end > event2_start)
)

# Check for conflicts
same_day = event1_day == event2_day
overlap = same_day and (event1_start < event2_end) and (event2_start < event1_end)

if same_day:
    if event2_start >= event1_end:
        gap = event2_start - event1_end
    elif event1_start >= event2_end:
        gap = event1_start - event2_end
    else:
        gap = 0
else:
    gap = None

back_to_back = same_day and gap is not None and gap < 0.55 and not overlap
to_early = (event1_start < 6 or event2_start < 6)
to_late = (event1_end > 23 or event2_end > 23)

print("\nschedule analysis\n")

if event1_valid and event2_valid:
    print("Both events have valid times")
else:
    print("One or both events have invalid times (Check the range)")

if overlap:
    print("Events overlap conflict detected")
elif back_to_back:
    print("Events are back to back (less than 30 minute gap)")
else:
    if same_day:
        print("No direct conflict")
    else:
        print("Events are on different days — no conflict")

    if to_early:
        print("One or more events start too early (before 6)")
    if to_late:
        print("One or more events end too late (after 23)")

# Only calculate durations if both events are valid
if event1_valid and event2_valid:
    event1duration = event1_end - event1_start
    event2duration = event2_end - event2_start
    totaltime = event1duration + event2duration

    print(f"\nEvent 1: {event1_name}")
    print(f"{event1_day.title()} {event1_start:.2f} - {event1_end:.2f} ({event1duration:.1f} hours)")

    print(f"Event 2: {event2_name}")
    print(f"{event2_day.title()} {event2_start:.2f} - {event2_end:.2f} ({event2duration:.1f} hours)")

    print(f"Total time commitment: {totaltime:.1f} hours")

    # Recommendations
    if overlap:
        print("Recommendation: Reschedule one event to avoid time conflict.")
    elif back_to_back:
        print("Recommendation: Consider adding buffer time between events.")
    elif to_early or to_late:
        print("Recommendation: Adjust schedule for time balance.")
    else:
        print("Recommendation: Schedule looks balanced and efficient!")
else:
    print("Unable to calculate details due to invalid input.")



print("=== RETAIL DISCOUNT CALCULATOR ===")

# Get inputs
price = float(input("Item price: $"))
quantity = int(input("Quantity: "))
customer_type = input("Customer type (regular/member/vip/employee): ").lower()
day = input("Day of week: ").lower()
coupon = input("Coupon code (or 'none'): ").upper()
subtotal = price * quantity
running_total = subtotal
total_discount = 0
discount_number = 1
print("Order Summary:")
print("Items:", quantity, "x $%.2f" % price, "= $%.2f" % subtotal)
print("Discounts Applied:")

# 1. Bulk discount
if quantity >= 50:
    rate = 0.20
elif quantity >= 20:
    rate = 0.15
elif quantity >= 10:
    rate = 0.10
else:
    rate = 0

if rate > 0:
    discount = running_total * rate
    running_total = running_total - discount
    total_discount = total_discount + discount
    print(discount_number, ". Bulk discount (", quantity, "items):", int(rate*100), "percent off = -$", "%.2f" % discount)
    print("Subtotal: $%.2f" % running_total)
    discount_number = discount_number + 1

if customer_type == "member":
    rate = 0.05
elif customer_type == "vip":
    rate = 0.10
elif customer_type == "employee":
    rate = 0.15
else:
    rate = 0

if rate > 0:
    discount = running_total * rate
    running_total = running_total - discount
    total_discount = total_discount + discount
    print(discount_number, ". ", customer_type.capitalize(), "discount:", int(rate*100), "percent off = -$", "%.2f" % discount)
    print("Subtotal: $%.2f" % running_total)
    discount_number = discount_number + 1

day_short = day[:3]
if day_short == "tue":
    rate = 0.05
elif day_short == "sat" or day_short == "sun":
    rate = 0.10
else:
    rate = 0

if rate > 0:
    discount = running_total * rate
    running_total = running_total - discount
    total_discount = total_discount + discount
    print(discount_number, ". ", day.capitalize(), "special:", int(rate*100), "percent off = -$", "%.2f" % discount)
    print("Subtotal: $%.2f" % running_total)
    discount_number = discount_number + 1

if coupon == "SAVE10":
    rate = 0.10
elif coupon == "SAVE20":
    rate = 0.20
elif coupon == "STUDENT":
    rate = 0.15
else:
    rate = 0

if rate > 0:
    discount = running_total * rate
    running_total = running_total - discount
    total_discount = total_discount + discount
    print(discount_number, ". Coupon", coupon, ":", int(rate*100), "percent off = -$", "%.2f" % discount)
    print("Subtotal: $%.2f" % running_total)
    discount_number = discount_number + 1
    
max_discount = subtotal * 0.40
if total_discount > max_discount:
    total_discount = max_discount
    running_total = subtotal - max_discount
    print("\nMaximum discount of 40 percent reached!")

total_percent = (total_discount / subtotal) * 100
print("\nTotal Discount: $%.2f (%.1f percent)" % (total_discount, total_percent))
print("Final Price: $%.2f" % running_total)
print("You saved: $%.2f!" % total_discount)