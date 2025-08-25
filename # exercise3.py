# exercise3.py
# Arithmetic Operations Lab
# KC
# 8/25/2025
# Test numbers
a = 17
b = 5
c = 2.5
print("Test Values:")
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)
# TODO: Perform each operation and observe results
# Addition
add_result = a + b
print(f"{a} + {b} = {add_result}")
# Subtraction
sub_result = a - b
print(f"{a} - {b} = {sub_result}")
# Multiplication
mul_result = a*b
print(f"{a} - {b} = {mul_result}")
# Division (/) - note the type!
div_result = a / b
print(f"{a} / {b} = {div_result} (Type: {type(div_result)})")
# Integer Division (//)
int_div_result = a // b
print(f"{a} // {b} = {int_div_result}")
# Modulo (%)
mod_result = a % b
print (f"{a} % {b} = {mod_result}")
# Exponentiation (**)
exp_result = a ** b
print(f"{a} ** {b}={exp_result}")
print("-" * 30)
# TODO: Mixed type operations
print("Mixed Type Operations:")
# What happens with int + float?
mixed1 = a + c
print(f"{a} + {c} = {mixed1} (Type: {type(mixed1)})")
#Observations to Note:
#• What's the difference between / and // ?
#• What type does regular division ( / ) always return?
#• How does Python handle very large numbers?
#• What happens with negative integer division?
#Commit your work: git commit -m "Complete arithmetic operations lab"
#Part 4: Expression Evaluation (10 minutes)
#Exercise 4: Order of Operations ( exercise4.py )
#Practice with operator precedence:
print(f"{a} + {c} = {mixed1} (Type: {type(mixed1)})")
# Try more mixed operations
mixed2 = a * c
print(f"{a} * {c} = {mixed2} (Type: {type(mixed2)})")
mixed3 = a / c
print(f"{a} / {c} = {mixed3} (Type: {type(mixed3)})")
# TODO: Special cases to explore
print("\nSpecial Cases:")
# Large numbers
big = 10 ** 100 # 10 to the power of 100
print(f"10^100 = {big}")
print(f"Python handles large numbers: {type(big)}")
# Negative division
neg_result = -17 // 5
print(f"-17 // 5 = {neg_result} (Note: rounds DOWN)")
# Division by zero (uncomment to see error)
# error_result = 10 / 0

#• What's the difference between / and // ?
# / is divisiom // is interger division 
#• What type does regular division ( / ) always return?
#float 
#• How does Python handle very large numbers?
# very well python converts large numbers automatically
#• What happens with negative integer division?
# it rounds down 
# git commit "complete arithmetic lab"