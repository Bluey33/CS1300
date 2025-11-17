#CS1300_Hw9_Luczko_KC.py
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * 9/5 + 32
# Formula: F = C * 9/5 + 32
# Your code here
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9
# Formula: C = (F - 32) * 5/9
# Your code here
def temperature_report(temp, scale="C"):
    """Print temperature in both scales.
    Parameters:
    temp: temperature value
    scale: "C" for Celsius or "F" for Fahrenheit (default "C")
    """
    if scale == "C":
        f = celsius_to_fahrenheit(temp)
        print(f"{temp:.1f}°C is {f:.1f}°F")
    elif scale == "F":
        c = fahrenheit_to_celsius(temp)
        print(f"{temp:.1f}°F is {c:.1f}°C")
    else:
        print("Invalid scale USE C OR F")
# Your code here
# If scale is "C", show temp in C and converted to F
# If scale is "F", show temp in F and converted to C
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(68))
temperature_report(25)
temperature_report(77, "F")

def calculatee_weighted_grade(homework,midterm,final,hw_weight=0.3,mid_weight=0.3,final_weight=0.4):
    """
    Calculate the weighted grade.
    """
    return (homework * hw_weight) + (midterm * mid_weight) + (final * final_weight)
def get_letter_grade(score):
    """
    convert numeric score to letter grade
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def print_grade_report(name,hw,mid,final):
    """Print complete grade report for a student"""
    weighted_grade = calculatee_weighted_grade(hw,mid,final)
    letter_grade = get_letter_grade(weighted_grade)
    print("--- Grade Report ---")
    print(f"Student: {name}")
    print(f"Homework: {hw}")
    print(f"Midterm: {mid}")
    print(f"Final: {final}")
    print(f"Weighted Grade: {weighted_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")

print("Test outputs")
grade1 = calculatee_weighted_grade(85,78,92)
print(f"Grade 1: {grade1}")
grade2 = calculatee_weighted_grade(90,85,80,hw_weight=0.4,mid_weight=0.2,final_weight=0.4)
print(f"Grade 2: {grade2}")
print_grade_report("Alice Smith",88,91,85)

total_points = 0 
bonus_multiplier = 1.1
def add_score(points):
    """Add points to total points"""
    global total_points
    total_points += points
    return total_points
def apply_bonus():
    """Apply bonus multiplier to total """
    global total_points
    global bonus_multiplier
    total_points = total_points * bonus_multiplier
def get_final_score():
    """Get final score"""
    return total_points
def reset_game():
    """Reset total points to 0"""
    global total_points
    total_points = 0
print("test 3 outputs")
reset_game()
add_score(100)
add_score(50)
apply_bonus()
print(f"Total points: {get_final_score()}")
print("Bonus")
def add_scorenoglobal(total2, points):
    return total2 + points
def apply_bonusnoglobal(total2, multiplier):
    return total2 * multiplier
def get_final_scorenoglobal(total2):
    return total2
def reset_gamenoglobal():
    return 0
print("bonus outputs")
total2 = reset_gamenoglobal()
total2 = add_scorenoglobal(total2, 100)
total2 = add_scorenoglobal(total2, 50)
total2 = apply_bonusnoglobal(total2, 1.1)
print(f"Total points: {get_final_scorenoglobal(total2)}")
