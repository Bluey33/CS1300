# calculator.py
# Simple Calculator with Type Handling
# KC
# 8/25/2025
print("=" * 40)
print(" ARITHMETIC CALCULATOR")
print("=" * 40)
# TODO: Create variables for two numbers
# Use meaningful variable names
first_number =  15.5 # Change to your values
second_number = 4 # Change to your values
# TODO: Display the numbers and their types
print(f"First number: {first_number} (Type: {type(first_number).__name__})")
print(f"Second number: {second_number} (Type: {type(second_number).__name__})")
print("-" * 40)
# TODO: Perform all arithmetic operations
print("CALCULATIONS:")
# Addition
sum_result = first_number + second_number
print(f"Addition: {first_number} + {second_number} = {sum_result}")
# Subtraction
diff_result = first_number - second_number
print(f"Subtraction: {first_number} - {second_number} = {diff_result}")
# Multiplication
product_result = first_number * second_number
print(f"Multiplication: {first_number} * {second_number} = {product_result}")
# Division (regular)
division_result = first_number / second_number
print(f"Division: {first_number} / {second_number} = {division_result}")
# Integer Division
int_div_result = first_number // second_number
print(f"Integer Division: {first_number} // {second_number} = {int_div_result}")
# Modulo
mod_result = first_number % second_number
print(f"Modulo: {first_number} % {second_number} = {mod_result}")
# Exponentiation
exp_result = first_number ** second_number
print(f"Exponentiation: {first_number} ** {second_number} = {exp_result}")
print("-" * 40)
# TODO: Type analysis section
print("TYPE ANALYSIS:")
# Check and display the type of each result
# Show which operations always return floats
# Show which preserve integer type
print("-" * 40)
# TODO: Fun calculations section
print("FUN CALCULATIONS:")
# Calculate the area of a circle with radius = first_number
pi = 3.14159
area = pi * first_number
print(f"Area of circle with radius {first_number}: {area:.2f}")
# Calculate compound interest
# Principal = first_number * 100, Rate = second_number%, Time = 5 years
principal = first_number * 100
rate = second_number / 100
time = 5
amount = principal * (1 + rate) ** time
print(f"${principal} at {second_number}% for {time} years = ${amount:.2f}")
# Calculate how many whole pizzas and slices
# If first_number is people and each pizza has 8 slices
# Each person gets second_number slices
total_slices_needed = first_number * second_number
whole_pizzas = total_slices_needed// 8
extra_slices = total_slices_needed % 8
print(f"{first_number} people × {second_number} slices each =")
print(f" Need {whole_pizzas} pizzas with {extra_slices} slices left over")
print("=" * 40)

#Calc 1 FUN CALCULATIONS: 10 , 3
#Area of circle with radius 10: 31.42
#$1000 at 3% for 5 years = $1159.27
#10 people × 3 slices each =
# Need 3 pizzas with 6 slices left over
#calc 2 FUN CALCULATIONS: 7,2
#Area of circle with radius 7: 21.99
#$700 at 2% for 5 years = $772.86
#7 people × 2 slices each =
# Need 1 pizzas with 6 slices left over
#calc 3 FUN CALCULATIONS: 15.5, 4
#Area of circle with radius 15.5: 48.69
#$1550.0 at 4% for 5 years = $1885.81
#15.5 people × 4 slices each =
# Need 7.0 pizzas with 6.0 slices left over