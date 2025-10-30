#CS 1300 Homework #7 By Kc Luczko
temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]
x = 1
print("===========================")
print("Temperature Analysis Report")
print("===========================")

for temp in temperatures:
    Celsius = (temp - 32) * 5 / 9
    print(f"Day {x}: {temp}°F ({Celsius:.1f}°C)")
    x += 1

print("Statistics:")
average = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average:.1f}°F")
highestnum = max(temperatures)
print(f"Highest temperature: {highestnum}°F")
lowestnum = min(temperatures)
print(f"Lowest temperature: {lowestnum}°F")

daysabove72 = [temp for temp in temperatures if temp > 72]
print(f"Days above 72°F: {len(daysabove72)}")

print("Question 2: ")
count = 5
import random
secret = random.randint(1, 20)
guesses = []
print("=== NUMBER GUESSING GAME ===")
print("I'm thinking of a number between 1 and 20.")
print(f"You have {count} chances")

for attempt in range(1, count + 1):
    guess = int(input(f"Attempt {attempt}: Make a guess: "))
    guesses.append(guess)

    if guess == secret:
        print(f"Correct The number was {secret}")
        print(f"It took you {attempt} guesses")
        break
    elif guess < secret:
        print("Too low Try higher.")
    else:
        print("Too high Try lower.")

else:
    print(f"Out of guesses, The number was {secret}")

print("Your guesses were:", guesses)







print("Question 3")
grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0
invalid_count = 0
valid_grades = []
gradenum = 0
print("==================")
print("Processing Grades...")
print("==================")

for grade in grades:
    if grade < 0 or grade > 100:
        print(f"skipping invalid grade: {grade}")
        invalid_count += 1
        continue  
    gradenum += 1
    valid_grades.append(grade)

    if grade >= 90:
        letter = "A"
        a_count += 1
    elif grade >= 80:
        letter = "B"
        b_count += 1
    elif grade >= 70:
        letter = "C"
        c_count += 1
    elif grade >= 60:
        letter = "D"
        d_count += 1
    else:
        letter = "F"
        f_count += 1

    print(f"Grade {gradenum}: {grade} ({letter})")

print("Summary Report")
print("==============")
print(f"total grades processed: {len(valid_grades)}")
print(f"invalid grades skipped: {invalid_count}")
print("grade Distribution:")
print(f"A: {a_count} students")
print(f"B: {b_count} students")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students")

if len(valid_grades) > 0:
    average = sum(valid_grades) / len(valid_grades)
    print(f"class Average: {average:.1f}")
else:
    print("no valid grades to calculate average.")

