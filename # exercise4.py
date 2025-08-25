# exercise4.py
# Order of Operations Practice
# KC 
# 8/25/2025
# TODO: Predict the result BEFORE running each expression
# Write your prediction as a comment, then check if correct
# Expression 1
# Prediction: 14
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")
# Expression 2
# Prediction: 20
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")
# Expression 3
# Prediction: 15
result3 = 10 / 2 * 3
print(f"10 / 2 * 3 = {result3}")
# Expression 4
# Prediction: 1.666
result4 = 10 / (2 * 3)
print(f"10 / (2 * 3) = {result4}")
# Expression 5
# Prediction: 512
result5 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result5}")
print("(Note: Exponentiation is right-to-left!)")
# Expression 6
# Prediction: 512
result6 = 2 ** (3 ** 2)
print(f"2 ** (3 ** 2) = {result6}")
# TODO: Create your own complex expression
# Use at least 4 operations
my_expression =  (5+3) *2 - 4 ** 2/2
print(f"My expression: {my_expression}")
# TODO: Break down a complex expression step by step
#5+3=8
#8*2=16
# 4 ** 2 = 16
#16/2 = 8.0
# 16 - 8.0 = 8.0
#= 8.0

complex = 10 + 20 * 30 / 10 - 5 ** 2
print("\nStep-by-step evaluation of: 10 + 20 * 30 / 10 - 5 ** 2")
print("Step 1: 5 ** 2 = 25")
print("Step 2: 20 * 30 = 600")
print("Step 3: 600 / 10 = 60.0")
print("Step 4: 10 + 60.0 = 70.0")
print("Step 5: 70.0 - 25 = 45.0")
print(f"Final result: {complex}")