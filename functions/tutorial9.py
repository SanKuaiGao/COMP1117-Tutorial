"""COMP1117 Tutorial 9 - Coding Practice: Functions.

Open this file in VS Code and work through the tasks in order.
Run it after each task:

    python3 tutorial9.py

Every function below returns a harmless placeholder value, so the file
always runs. Replace the placeholder with your own code, then compare the
printed result with the "expected" comment on the same line.

The test lines at the bottom are not a complete test suite - add your own
cases. A normal input, a boundary value and an empty or smallest input are
a good start.
"""


# =====================================================================
# Task 1 - Rectangle metrics
#   Return the area and the perimeter of a rectangle as a tuple.
#       area      = width * height
#       perimeter = 2 * (width + height)
#   Expected use:
#       area, perimeter = rectangle_metrics(4, 3)   # 12 and 14
# =====================================================================
def rectangle_metrics(width, height):
    area = 0
    perimeter = 0
    return area, perimeter


# =====================================================================
# Task 2 - Temperature converter
#       F = C * 9 / 5 + 32
#   Return the result. Do not print inside the function.
#   Tests to pass: 0 -> 32.0, 100 -> 212.0, -40 -> -40.0
# =====================================================================
def celsius_to_fahrenheit(celsius):
    return 0.0


# =====================================================================
# Task 3 - Delivery fee
#   Base fee $25; add $8 for each kg above 2; add $15 when express is True.
#   Expected: (1.5, False) -> 25   (4, False) -> 41   (4, True) -> 56
# =====================================================================
def delivery_fee(weight, express):
    return 0


# =====================================================================
# Task 4 - Count vowels
#   Count a, e, i, o, u in text, ignoring case. Return an integer.
#   Expected: "Hello" -> 2   "FUNCTIONS" -> 3   "rhythm" -> 0
#   Hint: loop through text.lower().
# =====================================================================
def count_vowels(text):
    return 0


# =====================================================================
# Task 5 - List average
#   Add the numbers with a loop (not sum()).
#   Return None for an empty list, otherwise total / length.
#   Expected: [2, 4, 6] -> 4.0   [5] -> 5.0   [] -> None
# =====================================================================
def list_average(numbers):
    return None


# =====================================================================
# Task 6 - Prime checker
#   Return True when n is prime, otherwise False.
#   Prime means: an integer greater than 1 with no divisor except 1 and
#   itself. 0, 1 and negative numbers are not prime.
#   Expected: 2 -> True   9 -> False   17 -> True   1 -> False
#   Hint: if n % divisor == 0, you have found a divisor.
# =====================================================================
def is_prime(n):
    return False


# =====================================================================
# Task 7 - Grade report
#   Write TWO functions and call one from the other.
#   letter_grade(mark) returns "A", "B", "C", "D" or "F":
#       A: mark >= 80    B: mark >= 70    C: mark >= 60
#       D: mark >= 50    F: otherwise
#   grade_report(name, mark) returns a string like "Ada: 84 (A)".
#   Expected: grade_report("Ada", 84) -> "Ada: 84 (A)"
# =====================================================================
def letter_grade(mark):
    return "?"


def grade_report(name, mark):
    letter = "?"
    return f"{name}: {mark} ({letter})"


# =====================================================================
# Tests - check your work. Add cases, but keep these ones passing.
# =====================================================================
print("Task 1:", rectangle_metrics(4, 3), "| expected: (12, 14)")

print("Task 2:", celsius_to_fahrenheit(0), "| expected: 32.0")
print("Task 2:", celsius_to_fahrenheit(100), "| expected: 212.0")
print("Task 2:", celsius_to_fahrenheit(-40), "| expected: -40.0")

print("Task 3:", delivery_fee(1.5, False), "| expected: 25")
print("Task 3:", delivery_fee(4, False), "| expected: 41")
print("Task 3:", delivery_fee(4, True), "| expected: 56")

print("Task 4:", count_vowels("Hello"), "| expected: 2")
print("Task 4:", count_vowels("FUNCTIONS"), "| expected: 3")
print("Task 4:", count_vowels("rhythm"), "| expected: 0")

print("Task 5:", list_average([2, 4, 6]), "| expected: 4.0")
print("Task 5:", list_average([5]), "| expected: 5.0")
print("Task 5:", list_average([]), "| expected: None")

print("Task 6:", is_prime(2), "| expected: True")
print("Task 6:", is_prime(9), "| expected: False")
print("Task 6:", is_prime(17), "| expected: True")
print("Task 6:", is_prime(1), "| expected: False")

print("Task 7:", grade_report("Ada", 84), "| expected: Ada: 84 (A)")
