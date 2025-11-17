#CS1300_HW8_Luczko_KC.py
size = input("Enter table size (1-12): ")

while not(size.isdigit()and 1 <= int(size)<=12):
    print("Invalid please enter a number between 1-12")
    size = input("Enter table size (1-12): ")
size = int(size)

print(f"\nMultiplication table size({size}x{size})")
print("=" * (6 *(size + 1)))
print(f"{' ':>3}|", end= " ")
for column in range(1, size+1):
    print(f"{column:>3}", end= "")
print()
print("-" *(6*(size+1)))
for rowsize in range(1, size+1):
    print(f"{rowsize:>3}| ", end="")
    for column in range(1, size+1):
        print(f"{rowsize * column:>3}", end="")
    print()
print("=" *(6*(size + 1)))

print("Problem 2")

numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
found = False
print("=== Pattern Analysis ===")
print(f"Original numbers: {numbers}")

print("1. Search Pattern")
for x in range(len(numbers)):
    if numbers[x] > 75:
        print(f"First number greater than 75 is: {numbers[x]}(at position{x-1})")
        found = True
        break
if not found:
    print("No number greater than 75: ")

print("2. Filter Pattern")
evennumbers= []
for num in numbers:
    if num % 2 == 0:
        evennumbers.append(num)
    
print(f"Even Numbers: {evennumbers}")

print("3. Counter Pattern")
range0_25=0
range26_50 =0
range51_75=0
range76_100=0
for num in numbers:
    if 0 <= num <= 25:
        range0_25 +=1
    elif 26 <= num <= 50:
        range26_50 += 1
    elif 51 <= num <= 75:
        range51_75 +=1
    elif 76 <= num <= 100:
        range76_100 +=1
print(F"range 0-25: {range0_25} numbers")
print(F"range 26-50 {range26_50} numbers")
print(F"range 51-75: {range51_75} numbers")
print(F"range 76-100: {range76_100} numbers")

print("4. Accumulator Pattern:")
div3=[]
sumdiv3=0
for num in numbers:
    if num % 3 == 0:
        div3.append(num)
        sumdiv3+=num
print(f"Numbers divisible by 3: {div3}")
print(f"Sum of Numbers divisible by 3: {sumdiv3}")

print("5. Sentinel pattern")
print("Add more numbers use -1 to stop adding:")
while True:
    newinput= input("Enter Number ")
    if newinput.lstrip("-").isdigit():
        newnum = int(newinput)
        if newnum == -1:
            break
        numbers.append(newnum)
    else:
        print("Please enter a real number")
print(f"Update list:{numbers}")
print(f"new count: {len(numbers)} numbers")

print("Problem 3")
students = ["Alice", "Bob", "Carol", "David", "Emma"]
assignments = ["HW1", "HW2", "Quiz1", "Exam1", "Quiz2"]
grades = [
[92, 88, 95, 87, 90], # Alice
[78, 82, 73, 85, 80], # Bob
[95, 91, 98, 92, 94], # Carol
[65, 70, 68, 72, 75], # David
[88, 85, 82, 90, 87]  # Emma
]
print("=== Grading Report System ===")
print("grade table:")
print("          HW1  HW2  Quiz1  Exam1  Quiz2")
print("          ---------------------------------")
studentavf=[]
letteravg= []
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

for student in range(len(students)):
    row = grades[student]
    total = 0
    for score in row:
        total += score
    avg = total / len(row)
    studentavf.append(avg)
    letteravg.append(grade(avg))
    print(f"          {students[student]:<6}  {grades[student][0]:>3}   {grades[student][1]:>3}   {grades[student][2]:>3}   {grades[student][3]:>3}   {grades[student][4]:>3}")

print()
print("assignment statistics:")
for x in range(len(assignments)):
    total = 0
    highest = -1
    lowest = 999
    highstudent = ""
    lowstudent = ""
    for s in range(len(students)):
        score = grades[s][x]
        total += score
        if score > highest:
            highest = score
            highstudent = students[s]
        if score < lowest:
            lowest = score
            lowstudent = students[s]
    classavg = total / len(students)
    print(f"          {assignments[x]}:  Class Avg: {classavg:.1f}  Highest: {highest} ({highstudent})  Lowest: {lowest} ({lowstudent})")

print()
print("Special regoniztions:")
honor = []
warn = []
for i in range(len(students)):
    if studentavf[i] >= 90:
        honor.append(students[i])
    elif studentavf[i] < 70:
        warn.append(students[i])
print(f"          Honor Roll (avg >= 90): {', '.join(honor) if honor else 'None'}")
print(f"          Academic Warning (avg < 70): {', '.join(warn) if warn else 'None'}")

print()
print("summary:")
classavg = sum(studentavf) / len(studentavf)
highestavg = max(studentavf)
lowestavg = min(studentavf)
high_stdent = students[studentavf.index(highestavg)]
low_stdent = students[studentavf.index(lowestavg)]
print(f"          Highest Overall Average: {high_stdent} ({highestavg:.1f}%)")
print(f"          Lowest Overall Average:  {low_stdent} ({lowestavg:.1f}%)")
print(f"          Class Average:           {classavg:.1f}%")

print()
print("grade distribution:")
distribution = {"A":0,"B":0,"C":0,"D":0,"F":0}
for g in letteravg:
    distribution[g] += 1

for k in distribution:
    print(f"          {k}: {distribution[k]} student")
