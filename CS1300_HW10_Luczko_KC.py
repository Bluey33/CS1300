import os

def get_numbers():
    """
    Get numbers from user until they enter 'done'.
    Return list of floats.
    """
    numbers = []
    while True:
        enter = input("Enter a number (or 'done' to stop): ")
        
        if enter.lower() == "done":
            break
        
        try:
            num = float(enter)
            numbers.append(num)
        except ValueError:
            print("Invalid input, please enter a number.")
    
    return numbers


def calculate_stats(numbers):
    """
    Calculate min, max, average, and range.
    Return all four values. 
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    range_val = maximum - minimum
    return minimum, maximum, average, range_val


def format_stats(minimum, maximum, average, range_val):
    """
    Format statistics for display.
    Return formatted string.
    """
    result = (
        f"Minimum: {minimum:.2f}\n"
        f"Maximum: {maximum:.2f}\n"
        f"Average: {average:.2f}\n"
        f"Range: {range_val:.2f}"
    )
    return result


def main():
    """Main program using modular design."""
    print("=== Statistics Calculator ===")
    
    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered. Exiting")
        return

    minimum, maximum, average, range_val = calculate_stats(numbers)
    result = format_stats(minimum, maximum, average, range_val)
    
    print("\n" + result)


#main()


def validate_score(score_str):
    """
    Helper: Validate that string is valid score (0-100).
    Return True/False.
    """
    score_str = score_str.strip()
    if not score_str.isdigit():
        return False
    score = int(score_str)
    return 0 <= score <= 100
    # Check if in range 0-100


def get_valid_score(prompt):
    """
    Helper: Get validated score from user.
    Keep asking until valid.
    """
    while True:
        value = input(prompt)
        if validate_score(value):
            return int(value)
        print("Invalid score, enter a number between 0 and 100")
    # Keep looping until valid input
    # Return integer score


def calculate_letter(score):
    """
    Helper: Convert score to letter grade.
    """
    # A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: < 60
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


def process_student():
    """
    CS1300_Function_homework2.md 2025-10-30
    3 / 4
    Process one student's grades.
    Get 3 test scores, calculate average and letter.
    """
    # Use helper functions
    name = input("Enter student name: ")
    scores = [
        get_valid_score("score 1: "),
        get_valid_score("score 2: "),
        get_valid_score("score 3: ")
    ]
    # Get name and 3 scores
    average = sum(scores) / len(scores)
    letter = calculate_letter(average)
    return name, scores, average, letter
    # Calculate and return results
    


def display_report(name, scores, average, letter):
    """
    Display formatted student report.
    """
    # Format nicely with student info
    print("--- Student Report ---")
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Final grade: {letter}")
    print("--- End Report ---")


def main():
    """
    Main program - process multiple students.
    """
    while True:
        try:
            count = int(input("how many students: "))
            if count > 0:
                break
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Invalid input, enter a number.")

    class_scores = []
    # Process each student
    for i in range(count):
        name, scores, average, letter = process_student()
        display_report(name, scores, average, letter)
        class_scores.append(average)
    # Optional: Calculate class average
    if len(class_scores) > 0:
        class_avg = sum(class_scores) / len(class_scores)
        print(f"Class average: {class_avg:.2f}")


#main()


def getvalidprice():
    """Ask repeatedly until user enters a valid no negative price."""
    while True:
        price_str = input("Price: ")
        try:
            price = float(price_str)
            if price >= 0:
                return price
            else:
                print("Price must be positive.")
        except ValueError:
            print("Invalid number, try again.")


def gatheritems():
    """Collect items and prices from the user."""
    items = []
    prices = []

    while True:
        item = input("Item (or done): ").strip()
        if item.lower() == "done":
            break
        price = getvalidprice()
        items.append(item)
        prices.append(price)

    return items, prices


def calculatetotal(prices):
    """Return total and discounted total."""
    total = sum(prices)
    discount = 0
    if total > 50:
        discount = round(total * 0.10, 2)
        total -= discount
    return total, discount


def printreceipt(items, prices, total, discount):
    """Print the formatted shopping list and totals."""
    print("=== Shopping List ===")

    for item, price in zip(items, prices):
        print(f"{item:<10} ${price:>5.2f}")
    print("----------------------")
    subtotal = sum(prices)
    print(f"Subtotal:         ${subtotal:,.2f}")
    if discount > 0:
        print(f"10% Discount:    -${discount:,.2f}")

    print(f"Final Total:      ${total:,.2f}")
    print("======================")


def savetofile(filename, items, prices):
    """Save shopping list to a file."""
    with open(filename, "w") as f:
        for item, price in zip(items, prices):
            f.write(f"{item},{price}\n")
    print(f"Shopping list saved to {filename}")


def loadfromfile(filename):
    """Load shopping list from a file."""
    if not os.path.exists(filename):
        print(f"No file found: {filename}")
        return [], []

    items = []
    prices = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",", 1)
            if len(parts) != 2:
                continue
            item, price_str = parts
            try:
                price = float(price_str)
                items.append(item)
                prices.append(price)
            except ValueError:
                print(f"Skipping invalid line: {line}")
    print(f"Shopping list loaded from {filename}")
    return items, prices


def shopping():
    print("Do you want to load an existing list? (yes/no)")
    if input("> ").strip().lower() == "yes":
        filename = input("Enter filename to load ").strip()
        items, prices = loadfromfile(filename)
    else:
        items, prices = gatheritems()

    total, discount = calculatetotal(prices)
    printreceipt(items, prices, total, discount)

    print("Do you want to save this list? (yes/no)")
    if input("> ").strip().lower() == "yes":
        filename = input("Enter filename to save: ").strip()
        savetofile(filename, items, prices)
shopping()


