"""COMP1117 Tutorial 7 - Coding Practice: Strings (worked solutions).

One possible solution per task. This is not the only correct answer:
different code is fine as long as it returns the right value for normal,
empty, boundary and unusual inputs.

Run this file to check every expected result at once:

    python3 tutorial7_solutions.py

It ends with "All checks passed." when every assertion holds.
"""


# Task 1 - Clean up a message
def normalise_text(text):
    cleaned = text.lower().replace('!', '')
    return ' '.join(cleaned.split())


# Task 2 - Find the longest word
def word_summary(text):
    words = text.split()
    longest = ''

    for word in words:
        if len(word) > len(longest):
            longest = word

    return len(words), longest


# Task 3 - Build a text report
def text_report(text):
    cleaned = normalise_text(text)
    word_count, longest = word_summary(cleaned)

    total_length = 0
    for word in cleaned.split():
        total_length = total_length + len(word)

    average = 0.0
    if word_count > 0:
        average = total_length / word_count

    if longest == '':
        longest = '(none)'

    # The space stays after "Text:" even when the text is empty.
    return (f'Text: {cleaned}\n'
            f'Words: {word_count}\n'
            f'Longest: {longest}\n'
            f'Average length: {average:.1f}')


# Task 4 - Name initials
def initials(name):
    result = ''

    for part in name.split():
        result = result + part[0].upper() + '.'

    return result


# Task 5 - Count one character
def count_character(text, target):
    return text.lower().count(target.lower())


# Task 6 - A different palindrome rule
def is_palindrome(text):
    compact = ''.join(text.lower().split())
    return compact == compact[::-1]


# Task 7 - Mask a username
def mask_email(email):
    username, domain = email.split('@')
    masked = username[0] + '*' * (len(username) - 1)
    return masked + '@' + domain


# =====================================================================
# Checks
# =====================================================================
# Task 1: the class examples, then ! between words, whitespace only,
# punctuation that must survive, and a message that is already clean.
assert normalise_text('  PYTHON\tis Fun!!!  ') == 'python is fun'
assert normalise_text('  Keep, THIS? 42! ') == 'keep, this? 42'
assert normalise_text('') == ''
assert normalise_text('one!two') == 'onetwo'
assert normalise_text('!!!') == ''
assert normalise_text('  \t\n ') == ''
assert normalise_text(' A ! B ') == 'a b'
assert normalise_text('Already clean') == 'already clean'

# Task 2: normal input, a tie, punctuation counting towards length,
# whitespace-only input and a single word.
assert word_summary('Python is fun') == (3, 'Python')
assert word_summary('red blue gold') == (3, 'blue')
assert word_summary('') == (0, '')
assert word_summary('   ') == (0, '')
assert word_summary('single') == (1, 'single')
assert word_summary('a bb cc dd') == (4, 'bb')
assert word_summary('red, blue') == (2, 'red,')

# Task 3: the two class examples, then an exact average and a tie.
assert text_report('  Python\tis FUN!!! ') == (
    'Text: python is fun\n'
    'Words: 3\n'
    'Longest: python\n'
    'Average length: 3.7'
)
assert text_report('') == (
    'Text: \n'
    'Words: 0\n'
    'Longest: (none)\n'
    'Average length: 0.0'
)
assert text_report('a bb ccc') == (
    'Text: a bb ccc\n'
    'Words: 3\n'
    'Longest: ccc\n'
    'Average length: 2.0'
)
assert text_report('cat dog') == (
    'Text: cat dog\n'
    'Words: 2\n'
    'Longest: cat\n'
    'Average length: 3.0'
)
assert text_report('!!!') == (
    'Text: \n'
    'Words: 0\n'
    'Longest: (none)\n'
    'Average length: 0.0'
)

# Task 4: two names, extra whitespace, one part, empty and blank input.
assert initials('Ada Lovelace') == 'A.L.'
assert initials('  alan\tturing ') == 'A.T.'
assert initials('') == ''
assert initials('   ') == ''
assert initials('x') == 'X.'
assert initials('ada  lovelace') == 'A.L.'

# Task 5: mixed case, every letter a match, a space and a punctuation
# mark as targets, no match and an empty text.
assert count_character('Banana', 'A') == 3
assert count_character('a a', ' ') == 1
assert count_character('', 'x') == 0
assert count_character('AAAA', 'a') == 4
assert count_character('BANANA', 'n') == 2
assert count_character('a.b.c', '.') == 2
assert count_character('abc', 'z') == 0

# Task 6: the class examples, a tab that replace(' ', '') would miss,
# punctuation that makes a difference, and mixed case.
assert is_palindrome('Never odd or even') is True
assert is_palindrome('ab,ba!') is False
assert is_palindrome('') is True
assert is_palindrome('   ') is True
assert is_palindrome('a\tbba') is True
assert is_palindrome('ab!ba') is True
assert is_palindrome('Ab') is False

# Task 7: a normal address, a one-character username, the shortest
# possible domain, a dot in the username and a mixed-case domain.
assert mask_email('alice@example.com') == 'a****@example.com'
assert mask_email('A@HKU.HK') == 'A@HKU.HK'
assert mask_email('bob@x') == 'b**@x'
assert mask_email('user.name@hku.hk') == 'u********@hku.hk'
assert mask_email('alice@Example.COM') == 'a****@Example.COM'

print("All checks passed.")
