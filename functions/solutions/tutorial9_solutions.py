"""COMP1117 Tutorial 9 - Coding Practice: Functions (worked solutions).

One possible solution per task. This is not the only correct answer:
different code is fine as long as it returns the right value for normal,
boundary and unusual inputs.

Run this file to check every expected result at once:

    python3 tutorial9_solutions.py

It ends with "All checks passed." when every assertion holds.
"""


# Task 1 - Rectangle metrics
def rectangle_metrics(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


# Task 2 - Temperature converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# Task 3 - Delivery fee
def delivery_fee(weight, express):
    fee = 25

    if weight > 2:
        fee = fee + (weight - 2) * 8

    if express:
        fee = fee + 15

    return fee


# Task 4 - Count vowels
def count_vowels(text):
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count = count + 1

    return count


# Task 5 - List average
def list_average(numbers):
    if len(numbers) == 0:
        return None

    total = 0
    for number in numbers:
        total = total + number

    return total / len(numbers)


# Task 6 - Prime checker
def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor = divisor + 1

    return True


# Task 7 - Grade report
def letter_grade(mark):
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    return "F"


def grade_report(name, mark):
    letter = letter_grade(mark)
    return f"{name}: {mark} ({letter})"


# =====================================================================
# Checks
# =====================================================================
# Task 1: normal case, then a square
assert rectangle_metrics(4, 3) == (12, 14)
assert rectangle_metrics(1, 1) == (1, 4)
assert rectangle_metrics(5, 2) == (10, 14)

# Task 2: two benchmarks and the point where both scales agree
assert celsius_to_fahrenheit(0) == 32.0
assert celsius_to_fahrenheit(100) == 212.0
assert celsius_to_fahrenheit(-40) == -40.0
assert celsius_to_fahrenheit(25) == 77.0

# Task 3: below, at, and above the 2 kg boundary; express on and off
assert delivery_fee(1.5, False) == 25
assert delivery_fee(2, False) == 25
assert delivery_fee(2.5, False) == 29.0
assert delivery_fee(4, False) == 41
assert delivery_fee(4, True) == 56
assert delivery_fee(2, True) == 40

# Task 4: mixed case, all capitals, no vowels, empty string
assert count_vowels("Hello") == 2
assert count_vowels("FUNCTIONS") == 3
assert count_vowels("rhythm") == 0
assert count_vowels("") == 0

# Task 5: several values, one value, empty list
assert list_average([2, 4, 6]) == 4.0
assert list_average([5]) == 5.0
assert list_average([]) is None

# Task 6: smallest prime, composite, prime, and the not-prime cases
assert is_prime(2) is True
assert is_prime(9) is False
assert is_prime(17) is True
assert is_prime(1) is False
assert is_prime(0) is False
assert is_prime(-7) is False
assert is_prime(25) is False

# Task 7: every threshold, from both sides
assert letter_grade(80) == "A"
assert letter_grade(79) == "B"
assert letter_grade(70) == "B"
assert letter_grade(69) == "C"
assert letter_grade(60) == "C"
assert letter_grade(59) == "D"
assert letter_grade(50) == "D"
assert letter_grade(49) == "F"
assert grade_report("Ada", 84) == "Ada: 84 (A)"

print("All checks passed.")
