# String cheat sheet — Tutorial 7

The operations used in this session, on one page. The
[Tutorial 7 README](README.md) explains *why*; this page is for when you only
need the spelling.

## Strings are values, not containers you edit

```python
s = 'Hello!'
s.upper()          # 'HELLO!'  -- thrown away
loud = s.upper()   # 'HELLO!'  -- kept
s                  # 'Hello!'  -- never changed
```

Every method **returns a new string**. Assign it or return it.

## Reading characters

| Expression | `'Python'` gives | Meaning |
| --- | --- | --- |
| `s[0]` | `'P'` | first character |
| `s[1]` | `'y'` | second character |
| `s[-1]` | `'n'` | last character |
| `s[1:4]` | `'yth'` | from 1 up to but **not** including 4 |
| `s[:3]` | `'Pyt'` | from the start |
| `s[3:]` | `'hon'` | to the end |
| `s[::-1]` | `'nohtyP'` | reversed |
| `s * 2` | `'PythonPython'` | repetition |
| `len(s)` | `6` | number of characters |

`s[0]` on `''` raises `IndexError`; `''[1:4]` and `''[::-1]` both give `''`.

## Methods worth remembering

| Method | Example | Result |
| --- | --- | --- |
| `.lower()` | `'Hi'.lower()` | `'hi'` |
| `.upper()` | `'hi'.upper()` | `'HI'` |
| `.strip()` | `'  hi  '.strip()` | `'hi'` (ends only) |
| `.replace(a, b)` | `'a!b'.replace('!', '')` | `'ab'` |
| `.split()` | `'  a\tb '.split()` | `['a', 'b']` |
| `.split(sep)` | `'a,b'.split(',')` | `['a', 'b']` |
| `.count(t)` | `'Banana'.count('a')` | `3` |
| `.startswith(p)` | `'Hello'.startswith('He')` | `True` |
| `.find(t)` | `'Hello'.find('l')` | `2` (or `-1`) |
| `in` | `'ell' in 'Hello'` | `True` |
| `sep.join(parts)` | `'-'.join(['a', 'b'])` | `'a-b'` |
| `len(s)` | `len('')` | `0` |

`.find()` returns `-1` when the text is absent; `.index()` raises `ValueError`
instead. Prefer `in` when you only need a yes/no answer.

## `split()` versus `split(' ')`

| Expression | Result |
| --- | --- |
| `'  red\tblue  '.split()` | `['red', 'blue']` |
| `'  red\tblue  '.split(' ')` | `['', '', 'red\tblue', '', '']` |
| `'a  b'.split()` | `['a', 'b']` |
| `'a  b'.split(' ')` | `['a', '', 'b']` |
| `''.split()` | `[]` |
| `''.split(' ')` | `['']` |

No argument = "any run of whitespace is one separator, and drop the empty ends".
Use it whenever the text came from a user, a file or `input()`.

## f-strings

| Code | Output |
| --- | --- |
| `f'{name}'` | the value of `name` |
| `f'{average:.1f}'` | one decimal place, e.g. `3.7` |
| `f'{count:3d}'` | right-aligned in three columns |
| `f'{word:>8}'` | right-aligned in eight columns |
| `f'a\nb'` | two lines |
| `f'{value!r}'` | the `repr()` form — good for debugging |

Formatting changes the **text** only; `average` keeps its full value.

## Recipes from the tasks

```python
# Task 1: clean a message
cleaned = ' '.join(text.lower().replace('!', '').split())

# Task 2: words and the first longest one
words = text.split()
longest = ''
for word in words:
    if len(word) > len(longest):
        longest = word

# Task 3: total letters, then a safe average
total = 0
for word in words:
    total = total + len(word)
average = total / len(words) if words else 0.0

# Task 4: initials
result = ''
for part in name.split():
    result = result + part[0].upper() + '.'

# Task 5: case-insensitive count
text.lower().count(target.lower())

# Task 6: palindrome ignoring case and whitespace
compact = ''.join(text.lower().split())
compact == compact[::-1]

# Task 7: mask a username
username, domain = email.split('@')
username[0] + '*' * (len(username) - 1) + '@' + domain
```

## Testing text

Spaces, tabs and empty strings are invisible in output, so print the `repr()`:

| Code | Shows |
| --- | --- |
| `print(repr('a b'))` | `'a b'` |
| `print(repr('a\tb'))` | `'a\tb'` |
| `print(repr(''))` | `''` |
| `print(repr(text_report('')))` | the exact four lines, escapes included |

An `assert` fails loudly the moment an expected value is wrong:

```python
assert initials('') == ''
assert mask_email('A@HKU.HK') == 'A@HKU.HK'
```

Run the file to see the failing line, fix one thing, run again — the same
predict → run → compare routine as always.

## Mistakes at a glance

| Symptom | Cause |
| --- | --- |
| `None` printed instead of a result | no `return`, or `pass` left in the body |
| Wrong word count | `split(' ')` on text with tabs or line breaks |
| Last tied word returned | `>=` instead of `>` |
| Average too high | `len(cleaned)` counts the spaces |
| `ZeroDivisionError` | average calculated before checking for zero words |
| Tab survives the palindrome cleanup | `replace(' ', '')` instead of `split()`/`join()` |
| `IndexError` | `text[0]` on an empty string |
| Case changed where it should not be | `.lower()` applied to the whole email |
| `3.6666666666666665` in the report | missing `:.1f` |
