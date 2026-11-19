"""COMP1117 Tutorial 9 - Coding Practice: Sets and Dictionaries.

Open this file in VS Code and work through the tasks in order.
Run it after each task:

    python3 tutorial9.py

Every function below returns a harmless placeholder value, so the file
always runs. Replace the placeholder with your own code, then compare the
printed result with the "expected" text printed with it.

Dictionaries print in insertion order, so the checks below are readable
when they pass. Equality of dictionaries ignores order, but Task 3's answer
does keep the order in which words are first seen, and Task 6 keeps the
keys of shop_a first.

Every task also requires you to leave the input unchanged. Task 5 and
Task 6 print the input again after the call so that a mutation shows up.

The checks at the bottom are not a complete test suite - add your own
cases. An empty input, a repeat and a tie are a good start.
"""


# =====================================================================
# Task 1 - Courses in common
#   a and b are lists of course codes; a code may appear more than once.
#   Return (both, only_a) as a tuple of two lists:
#       both    - codes in a and in b
#       only_a  - codes in a but not in b
#   Repeats count once, each list is sorted, and a and b are not changed.
#   Expected: (['COMP1117', 'MATH1013', 'COMP1117'],
#              ['MATH1013', 'ENGG1330'])
#             -> (['MATH1013'], ['COMP1117'])
# =====================================================================
def course_overlap(a, b):
    return [], []


# =====================================================================
# Task 2 - The first repeated value
#   Read items from left to right and return the first value whose second
#   appearance comes earliest. Return None if nothing repeats (including an
#   empty list). Use a set of values seen so far; no count(), no nested loop.
#   Expected: [3, 1, 4, 1, 3] -> 1     ['a', 'b', 'c'] -> None
# =====================================================================
def first_repeat(items):
    return None


# =====================================================================
# Task 3 - Count the words
#   Words are text.lower().split(); punctuation stays attached.
#   Return a dictionary from each word to how many times it appears.
#   Keys appear in the order each word is first seen; {} when there are no
#   words.
#   Expected: 'the cat and The hat' ->
#             {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
# =====================================================================
def word_counts(text):
    return {}


# =====================================================================
# Task 4 - The most common word
#   counts maps words to positive integers. Return (word, count) for the
#   largest count. A tie goes to the word that is first alphabetically.
#   Return ('', 0) for an empty dictionary. Use a loop, not max().
#   Expected: {'the': 2, 'cat': 1, 'hat': 2} -> ('hat', 2)
# =====================================================================
def most_common(counts):
    return '', 0


# =====================================================================
# Task 5 - Group students by grade
#   grades maps a student name to a grade letter. Return a new dictionary
#   from each grade that appears to the sorted list of names with it.
#   Do not change grades; return {} for empty input.
#   Expected: {'Ben': 'B', 'Cat': 'A', 'Ann': 'A'} ->
#             {'B': ['Ben'], 'A': ['Ann', 'Cat']}
# =====================================================================
def group_by_grade(grades):
    return {}


# =====================================================================
# Task 6 - Merge two stock lists
#   shop_a and shop_b map item names to quantities. Return a NEW dictionary
#   with every item from either shop; for an item in both, add the
#   quantities. Keep shop_a's keys first, then the keys only in shop_b.
#   Do not change either input.
#   Expected: ({'pen': 3, 'ink': 1}, {'ink': 4, 'cap': 2}) ->
#             {'pen': 3, 'ink': 5, 'cap': 2}
# =====================================================================
def merge_stock(shop_a, shop_b):
    return {}


# =====================================================================
# Tests - check your work. Add cases, but keep these ones passing.
# =====================================================================
print("Task 1:", course_overlap(['COMP1117', 'MATH1013', 'COMP1117'],
                                ['MATH1013', 'ENGG1330']))
print("Task 1: expected: (['MATH1013'], ['COMP1117'])")
print("Task 1:", course_overlap(['A', 'B'], []), "| expected: ([], ['A', 'B'])")

print("Task 2:", first_repeat([3, 1, 4, 1, 3]), "| expected: 1")
print("Task 2:", first_repeat(['a', 'b', 'c']), "| expected: None")
print("Task 2:", first_repeat([]), "| expected: None")

print("Task 3:", word_counts('the cat and The hat'))
print("Task 3: expected: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}")
print("Task 3:", word_counts(''), "| expected: {}")

print("Task 4:", most_common({'the': 2, 'cat': 1, 'hat': 2}),
      "| expected: ('hat', 2)")
print("Task 4:", most_common({}), "| expected: ('', 0)")

grades = {'Ben': 'B', 'Cat': 'A', 'Ann': 'A'}
print("Task 5:", group_by_grade(grades))
print("Task 5: expected: {'B': ['Ben'], 'A': ['Ann', 'Cat']}")
print("Task 5: grades after the call:", grades,
      "| expected: {'Ben': 'B', 'Cat': 'A', 'Ann': 'A'}")

shop_a = {'pen': 3, 'ink': 1}
shop_b = {'ink': 4, 'cap': 2}
print("Task 6:", merge_stock(shop_a, shop_b))
print("Task 6: expected: {'pen': 3, 'ink': 5, 'cap': 2}")
print("Task 6: shop_a after the call:", shop_a,
      "| expected: {'pen': 3, 'ink': 1}")
print("Task 6: shop_b after the call:", shop_b,
      "| expected: {'ink': 4, 'cap': 2}")
