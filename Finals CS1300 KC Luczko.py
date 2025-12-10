#Finals CS1300 KC Luczko
def count_positive(numbers):
    """
    Count how many positive numbers (greater than 0) are in a list.
    Parameters:
    numbers: A list of numbers
    Returns:
    The count of positive numbers
    """
# Your code here
def count_positive(numbers):
    count_positive = 0
    for number in numbers:
        if number >0:
            count_positive += 1
    return count_positive

pass
#Test your function:
print(count_positive([5, -2, 0, 3, -1, 8])) # Should print: 3
print(count_positive([-1, -2, -3])) # Should print: 0
print(count_positive([10, 20, 30])) # Should print: 3
print(count_positive([])) # Should print: 0

def get_age_group(age):
    """
    Classify age into a group.
    0-12: Child
    13-19: Teen
    20-59: Adult
    60+: Senior
    Parameters:
    age: Person's age (integer)
    Returns:
    Age group as a string
    """
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teen"
    elif age >= 20 and age <= 59:
        return "Adult"
    else:  # age >= 60
        return "Senior"

def count_age_groups(ages):
    """
    Count how many people in each age group.
    Parameters:
    ages: List of ages
    Returns:
    Dictionary with counts for each group
    """
    groups = {"Child": 0, "Teen": 0, "Adult": 0, "Senior": 0}
    for age in ages:
        category = get_age_group(age)
        groups[category] += 1
    return groups

# Test your functions:
print(get_age_group(5)) # Should print: Child
print(get_age_group(15)) # Should print: Teen
print(get_age_group(30)) # Should print: Adult
print(get_age_group(65)) # Should print: Senior
ages_list = [5, 15, 25, 35, 65, 8, 18, 70]
print(count_age_groups(ages_list)) # Should show counts for each group


def is_palindrome(word):
    """
    Check if a word is a palindrome (same forwards and backwards).
    Case-insensitive.
    Parameters:
    word: String to check
    Returns:
    True if palindrome, False otherwise
    """
    # Convert to lowercase
    word = word.lower()
    # Compare word with its reverse
    return word == word[::-1]

# Test your function:
print(is_palindrome("racecar")) # Should print: True
print(is_palindrome("hello")) # Should print: False
print(is_palindrome("Mom")) # Should print: True
print(is_palindrome("noon")) # Should print: True
print(is_palindrome("python")) # Should print: False

def create_pattern(n):
    """
    Create a number pattern up to n.
    For example, if n=3:
    1
    1 2
    1 2 3
    Parameters:
    n: Number of rows
    Returns:
    List of strings, each representing a row
    """
    pattern = []
    # Build each row of the pattern
    for i in range(1, n + 1):
        row = " ".join(str(x) for x in range(1, i + 1))
        pattern.append(row)
    return pattern
def print_pattern(n):
    """
    Print the number pattern.
    """
    rows = create_pattern(n)
    for row in rows:
        print(row)
# Test your function:
print_pattern(3)
# Should print:
# 1
# 1 2
# 1 2 3
print_pattern(5)
# Should print:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Return value test:
result = create_pattern(3)
print(result) # Should print: ['1', '1 2', '1 2 3']

def reverse_list(items):
    """
    Reverse a list by creating a new reversed list.
    Parameters:
    items: The list to reverse
    Returns:
    A new list with items in reverse order
    """
    reversed_list = []
    for item in items:
        reversed_list.insert(0, item)
    return reversed_list
# Test your function:
print(reverse_list([1, 2, 3, 4, 5])) # Should print: [5, 4, 3, 2, 1]
print(reverse_list(["a", "b", "c"])) # Should print: ["c", "b", "a"]
print(reverse_list([10])) # Should print: [10]
print(reverse_list([])) # Should print: []
