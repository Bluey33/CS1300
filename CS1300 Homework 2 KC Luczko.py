 #CS 1300 Homework 2
#Name: KC Luczko
#DATE : 9/8/2025
# Description: Variables, Input/Output, and Type Conversions
print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)

print("========================================")
print("PERSONAL FINANCE CALCULATOR")
print("========================================")

income = float(input("Enter your monthly income: "))
housing = float(input("Enter housing/rent cost: "))
food = float(input("Enter food expenses: "))
transport = float(input("Enter transportation cost: "))
other = float(input("Enter other expenses: "))

total_expenses = housing + food + transport + other
remaining = income - total_expenses
savings_rate = (remaining / income) * 100 

print("Total expenses:", total_expenses)
print("Remaining money:", remaining)
print(f"Savings rate: {savings_rate:.1f}")


print("\n" + "=" *40)
print("Problem 2: Grade Statistics Calculator")
print("=" * 40)
score1 = float(input("Enter score for Test 1 (out of 100):"))
score2 = float(input("Enter score for Test 2 (out of 100): "))
score3 = float(input("Enter score for Test 3 (out of 100): "))
score4 = float(input("Enter score for Test 4 (out of 100): "))
score5 = float(input("Enter score for Test 5 (out of 100): "))

total = score1 + score2 + score3 + score4 + score5
average = total /5
max_total = 500
percentage = (total / max_total) *100
points_needed = (0.9 * max_total) -total

print("****************************************")
print("GRADE REPORT")
print("****************************************")
print("Test Scores Entered:")
print("Test 1:",score1,"/100")
print("Test 2:",score2,"/100")
print("Test 3:",score3,"/100")
print("Test 4:",score4,"/100")
print("Test 5:",score5,"/100")
print("****************************************")
print("Statistics:")
print("Total Points:",total,"/500")
print("Average Score:",average)
print("Overall Grade:",percentage,"%")
print("Points needed for90%:",points_needed)

print("****************************************")

print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40)

est_hour = int(input("Enter current hour (EST, 0-23): "))
minute = int(input("Enter current minute (0-59): "))

cst_hour = (est_hour - 1) %24
mst_hour = (est_hour - 2) %24
pst_hour = (est_hour - 3) %24

est_12 = (est_hour %12) + (12 * (est_hour % 12 ==0))
cst_12 = (cst_hour %12) + (12 * (cst_hour % 12 ==0))
mst_12 = (mst_hour %12) + (12 * (mst_hour % 12 ==0))
pst_12 = (pst_hour %12) + (12 * (pst_hour % 12 ==0))


est_period = ["AM", "PM"][(est_hour //12) %2]
cst_period = ["AM", "PM"][(cst_hour // 12) %2]
mst_period = ["AM", "PM"][(mst_hour // 12) %2]
pst_period = ["AM", "PM"][(pst_hour // 12) %2]

print("+--------------------------------------+")
print("|            CURRENT TIMES             |")
print("+--------------------------------------+")
print("| Time Zone |  Time   | 12-hr Format   |")
print("|-----------|---------|----------------|")
print("| EST       |", f"{est_hour}: {minute:02d}",f"{est_12}:{minute:02d} {est_period}", "|")
print("| CST       |", f"{cst_hour}:{minute:02d}",f"{cst_12}:{minute:02d} {cst_period}", "|")
print("| MST       |", f"{mst_hour}: {minute:02d}",f"{mst_12}:{minute:02d} {mst_period}", "|")
print("| PST       |", f"{pst_hour}:{minute:02d}",f"{pst_12}:{minute:02d} {pst_period}", "|")
print("+--------------------------------------+")
# I had a really  had time with this section of the homework 
# It was super confusing how to do the 12 hr formatting


print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)

print("################################################")
print("RECIPE SCALER")
print("################################################")
original = int(input("Enter original serving size: "))
desired = int(input("Enter desired serving size: "))

scale = desired / original

name1 = input("Ingredient 1 name:")
amount1 = float(input("Amount:"))
unit1 = input("Unit:")

name2 = input("Ingredient 2 name:")
amount2 = float(input("Amount:"))
unit2 = input("Unit:")

name3 = input("Ingredient 3 name:")
amount3 = float(input("Amount:"))
unit3 = input("Unit:")

name4 = input("Ingredient 4 name:")
amount4 = float(input("Amount:"))
unit4 = input("Unit:")

name5 = input("Ingredient 5 name:")
amount5 = float(input("Amount:"))
unit5 = input("Unit:")

scaled1 = amount1 * scale
scaled2 = amount2 * scale
scaled3 = amount3 * scale
scaled4 = amount4 * scale
scaled5 = amount5 * scale

print("################################################")
print("RECIPE SCALING RESULTS")
print("################################################")
print("Scaling factor:", f"{scale:.2f}", f"({original}{desired} servings)")
print("------------------------------------------------")
print("Original Recipe (" + str(original) + " servings)Scaled Recipe (" + str(desired) + " servings)")
print("-----------------------------|---------------------------")
print(name1 +":"+f" {amount1:.2f}"+unit1 +name1+f" {scaled1:.2f}"+ unit1)
print(name2 +":"+f" {amount2:.2f}"+unit2 +name2+f" {scaled2:.2f}"+ unit2)
print(name3 +":"+f" {amount3:.2f}"+unit3 +name3+f" {scaled3:.2f}"+ unit3)
print(name4 +":"+f" {amount4:.2f}"+unit4 +name4+f" {scaled4:.2f}"+ unit4)
print(name5 +":"+f" {amount5:.2f}"+unit5 +name5+f" {scaled5:.2f}"+ unit5)
print("################################################")


print("\n" + "=" * 50)
print("END OF HOMEWORK 2")
print("=" * 50)