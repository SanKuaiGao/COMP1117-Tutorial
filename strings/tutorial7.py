"""COMP1117 Tutorial 7 - Coding Practice: Strings.

Open this file in VS Code and work through the tasks in order.
Run it after each task:

    python3 tutorial7.py

Every function below returns a harmless placeholder value, so the file
always runs. Replace the placeholder with your own code, then compare the
printed result with the "expected" text printed with it.

The strings are printed with repr() so that spaces, tabs and empty strings
are visible: repr('') shows '', and repr('a b') shows 'a b' with a real
space. Do not add repr() inside your functions - it belongs in the tests.

The checks at the bottom are not a complete test suite - add your own
cases. A normal input, an empty input and a tie are a good start.
"""


# =====================================================================
# Task 1 - Clean up a message
#   Return the cleaned message:
#       1. lowercase every letter and remove every "!"
#       2. collapse each run of whitespace into one ordinary space, and
#          remove leading and trailing whitespace
#       3. return '' when nothing remains
#   Removing "!" does not insert a space: 'one!two' -> 'onetwo'.
#   Expected: '  PYTHON\tis Fun!!!  ' -> 'python is fun'
# =====================================================================
def normalise_text(text):
    return ''


# =====================================================================
# Task 2 - Find the longest word
#   Return (number of words, first longest word).
#   A word is a non-empty part of text.split(); punctuation stays attached.
#   Keep the original spelling and case. A tie keeps the earlier word.
#   Use a loop - not max() and not sorting.
#   Expected: 'Python is fun' -> (3, 'Python')
#             ''             -> (0, '')
# =====================================================================
def word_summary(text):
    return 0, ''


# =====================================================================
# Task 3 - Build a text report
#   Call normalise_text() and then word_summary() on the cleaned text.
#   Return exactly four lines:
#       Text: <cleaned text>
#       Words: <count>
#       Longest: <longest word, or (none)>
#       Average length: <total word length / count, one decimal>
#   Use 0.0 for the average when there are no words, and no trailing
#   newline at the end.
#   Expected: '  Python\tis FUN!!! ' ->
#       Text: python is fun
#       Words: 3
#       Longest: python
#       Average length: 3.7
# =====================================================================
def text_report(text):
    return ''


# =====================================================================
# Task 4 - Name initials
#   Return the uppercase initials with a full stop after each one:
#       'Ada Lovelace' -> 'A.L.'
#   No spaces between initials. '' for an empty or whitespace-only name.
#   Expected: '  alan\tturing ' -> 'A.T.'
# =====================================================================
def initials(name):
    return ''


# =====================================================================
# Task 5 - Count one character
#   Count how often target appears in text, ignoring letter case.
#   target is always exactly one character; it may be a space or
#   punctuation mark. Return an integer.
#   Expected: ('Banana', 'A') -> 3    ('a a', ' ') -> 1
# =====================================================================
def count_character(text, target):
    return 0


# =====================================================================
# Task 6 - A different palindrome rule
#   Ignore letter case and ALL whitespace (spaces, tabs, line breaks),
#   but keep digits and punctuation. Return True when the remaining
#   string equals its reverse, otherwise False.
#   Expected: 'Never odd or even' -> True    'ab,ba!' -> False
# =====================================================================
def is_palindrome(text):
    return False


# =====================================================================
# Task 7 - Mask a username
#   Keep the first character of the part before "@", replace every other
#   character of it with "*", and keep "@" and the domain unchanged.
#   Preserve the case of everything you keep.
#   Expected: 'alice@example.com' -> 'a****@example.com'
#             'A@HKU.HK'          -> 'A@HKU.HK'
# =====================================================================
def mask_email(email):
    return ''


# =====================================================================
# Tests - check your work. Add cases, but keep these ones passing.
# =====================================================================
print("Task 1:", repr(normalise_text('  PYTHON\tis Fun!!!  ')),
      "| expected: 'python is fun'")
print("Task 1:", repr(normalise_text('')), "| expected: ''")

print("Task 2:", word_summary('Python is fun'), "| expected: (3, 'Python')")
print("Task 2:", word_summary('red blue gold'), "| expected: (3, 'blue')")
print("Task 2:", word_summary(''), "| expected: (0, '')")

# The report is four lines, so the expected value is written once above.
expected_report = ('Text: python is fun\n'
                   'Words: 3\n'
                   'Longest: python\n'
                   'Average length: 3.7')
print("Task 3:", repr(text_report('  Python\tis FUN!!! ')))
print("Task 3: expected:", repr(expected_report))

expected_empty = ('Text: \n'
                  'Words: 0\n'
                  'Longest: (none)\n'
                  'Average length: 0.0')
print("Task 3:", repr(text_report('')))
print("Task 3: expected:", repr(expected_empty))

print("Task 4:", repr(initials('Ada Lovelace')), "| expected: 'A.L.'")
print("Task 4:", repr(initials('  alan\tturing ')), "| expected: 'A.T.'")
print("Task 4:", repr(initials('')), "| expected: ''")

print("Task 5:", count_character('Banana', 'A'), "| expected: 3")
print("Task 5:", count_character('a a', ' '), "| expected: 1")
print("Task 5:", count_character('', 'x'), "| expected: 0")

print("Task 6:", is_palindrome('Never odd or even'), "| expected: True")
print("Task 6:", is_palindrome('ab,ba!'), "| expected: False")
print("Task 6:", is_palindrome(''), "| expected: True")

print("Task 7:", repr(mask_email('alice@example.com')),
      "| expected: 'a****@example.com'")
print("Task 7:", repr(mask_email('A@HKU.HK')), "| expected: 'A@HKU.HK'")
