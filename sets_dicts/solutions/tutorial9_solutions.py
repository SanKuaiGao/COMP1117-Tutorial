"""COMP1117 Tutorial 9 - Coding Practice: Sets and Dictionaries (solutions).

One possible solution per task. This is not the only correct answer:
different code is fine as long as it returns the right value for normal,
empty, boundary and unusual inputs, and does not change its arguments.

Run this file to check every expected result at once:

    python3 tutorial9_solutions.py

It ends with "All checks passed." when every assertion holds.
"""


# Task 1 - Courses in common
def course_overlap(a, b):
    set_a = set(a)
    set_b = set(b)

    both = sorted(set_a & set_b)
    only_a = sorted(set_a - set_b)
    return both, only_a


# Task 2 - The first repeated value
def first_repeat(items):
    seen = set()

    for item in items:
        if item in seen:
            return item
        seen.add(item)

    return None


# Task 3 - Count the words
def word_counts(text):
    counts = {}

    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1

    return counts


# Task 4 - The most common word
def most_common(counts):
    best_word = ''
    best_count = 0

    for word, count in counts.items():
        better = count > best_count
        tie = count == best_count and word < best_word
        if better or tie:
            best_word = word
            best_count = count

    return best_word, best_count


# Task 5 - Group students by grade
def group_by_grade(grades):
    groups = {}

    for name, grade in grades.items():
        if grade not in groups:
            groups[grade] = []
        groups[grade].append(name)

    for names in groups.values():
        names.sort()

    return groups


# Task 6 - Merge two stock lists
def merge_stock(shop_a, shop_b):
    total = dict(shop_a)

    for item, quantity in shop_b.items():
        total[item] = total.get(item, 0) + quantity

    return total


# =====================================================================
# Checks
# =====================================================================
# Task 1: the class examples, then duplicates, one empty side, both
# empty, and a check that the arguments were not changed.
assert course_overlap(['COMP1117', 'MATH1013', 'COMP1117'],
                      ['MATH1013', 'ENGG1330']) == (['MATH1013'],
                                                    ['COMP1117'])
assert course_overlap(['A', 'B'], []) == ([], ['A', 'B'])
assert course_overlap([], ['A']) == ([], [])
assert course_overlap([], []) == ([], [])
assert course_overlap(['A', 'A'], ['A']) == (['A'], [])
assert course_overlap(['b', 'a'], ['a']) == (['a'], ['b'])
assert course_overlap(['A', 'B'], ['C']) == ([], ['A', 'B'])

a = ['COMP1117', 'MATH1013']
b = ['MATH1013']
course_overlap(a, b)
assert a == ['COMP1117', 'MATH1013']
assert b == ['MATH1013']

# Task 2: the class examples, a zero that must not be treated as missing,
# repeats of repeats, and one item.
assert first_repeat([3, 1, 4, 1, 3]) == 1
assert first_repeat(['a', 'b', 'c']) is None
assert first_repeat([]) is None
assert first_repeat([0, 1, 2, 0]) == 0
assert first_repeat([1, 1]) == 1
assert first_repeat([1, 2, 2, 1]) == 2
assert first_repeat([5]) is None
assert first_repeat(['x', 'y', 'x', 'y']) == 'x'

# Task 3: the class examples, whitespace-only text, repeats, and the
# insertion order of the keys.
assert word_counts('the cat and The hat') == {'the': 2, 'cat': 1,
                                              'and': 1, 'hat': 1}
assert word_counts('Go, go GO!') == {'go,': 1, 'go': 1, 'go!': 1}
assert word_counts('') == {}
assert word_counts('   ') == {}
assert word_counts('\t\n') == {}
assert word_counts('a a a') == {'a': 3}
assert list(word_counts('the cat and The hat')) == ['the', 'cat', 'and', 'hat']

# Task 4: a tie won alphabetically, a single key, an empty dictionary,
# and a tie in which every word is equal.
assert most_common({'the': 2, 'cat': 1, 'hat': 2}) == ('hat', 2)
assert most_common({}) == ('', 0)
assert most_common({'a': 1}) == ('a', 1)
assert most_common({'b': 1, 'a': 1}) == ('a', 1)
assert most_common({'z': 5, 'a': 3}) == ('z', 5)
assert most_common({'b': 2, 'a': 2, 'c': 2}) == ('a', 2)

# Task 5: the class example, empty input, one student, and the input
# dictionary unchanged after the call.
assert group_by_grade({'Ben': 'B', 'Cat': 'A', 'Ann': 'A'}) == {
    'B': ['Ben'],
    'A': ['Ann', 'Cat'],
}
assert group_by_grade({}) == {}
assert group_by_grade({'Zoe': 'B'}) == {'B': ['Zoe']}

grades = {'Dan': 'C', 'Ann': 'A', 'Ben': 'A'}
grouped = group_by_grade(grades)
assert grouped == {'C': ['Dan'], 'A': ['Ann', 'Ben']}
assert grades == {'Dan': 'C', 'Ann': 'A', 'Ben': 'A'}

# Task 6: the class examples, empty sides, an item only in one shop,
# key order, and both inputs unchanged after the call.
assert merge_stock({'pen': 3, 'ink': 1},
                   {'ink': 4, 'cap': 2}) == {'pen': 3, 'ink': 5, 'cap': 2}
assert merge_stock({}, {'cap': 2}) == {'cap': 2}
assert merge_stock({}, {}) == {}
assert merge_stock({'a': 1}, {}) == {'a': 1}
assert merge_stock({'pen': 3}, {'book': 2}) == {'pen': 3, 'book': 2}

shop_a = {'pen': 3, 'ink': 1}
shop_b = {'ink': 4, 'cap': 2}
merged = merge_stock(shop_a, shop_b)
assert merged == {'pen': 3, 'ink': 5, 'cap': 2}
assert list(merged) == ['pen', 'ink', 'cap']
assert shop_a == {'pen': 3, 'ink': 1}
assert shop_b == {'ink': 4, 'cap': 2}

# Task 6 with a shop_a that has no item shared with shop_b.
assert list(merge_stock({'pen': 3}, {'ink': 4})) == ['pen', 'ink']

print("All checks passed.")
