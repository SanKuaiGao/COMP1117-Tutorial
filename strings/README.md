# Tutorial 7 — Coding Practice: Strings

Text is the most common input a program receives, and Python gives you a small
set of sharp tools for it. This session brings together the operations you have
already met — indexing, slicing, `split`, `join` and f-strings — and turns them
into seven small functions that **return** a value instead of printing one.

## Get started

Open [`tutorial7.py`](tutorial7.py) and run it:

```bash
python3 tutorial7.py
```

Every task starts with a placeholder value, so the file runs immediately and
prints something like `Task 1: '' | expected: 'python is fun'`. That is your
to-do list: replace the placeholder, run the file again, compare the two parts
of the line. (Task 3 prints its expected value on the next line, because the
result itself contains newlines.)

The checks print strings with `repr()` so that invisible characters show up:
`repr('a\tb')` shows the tab as `\t`, and `repr('')` shows that the string is
empty rather than missing. Use `repr()` in your own experiments, but `return`
the plain string from your functions.

The checks at the bottom of the file are a starting point, not a full test
suite. Add your own cases.

## A string cannot be changed in place

```python
message = 'Hello!'
print(message.lower())   # hello!
print(message)           # Hello!
```

`lower()` does not edit `message`. It builds a new string and returns it; if you
ignore that return value, the work is thrown away. Inside a function, `return`
the new string so the caller can use it.

The operations used in this tutorial:

| Expression | Result | Note |
| --- | --- | --- |
| `len('Python')` | `6` | number of characters |
| `'Python'[0]` | `'P'` | indexing; negative indexes count from the end |
| `'Python'[-1]` | `'n'` | the last character |
| `'Python'[1:4]` | `'yth'` | the stop index is excluded |
| `'Python'[::-1]` | `'nohtyP'` | a step of `-1` reverses |
| `'*' * 3` | `'***'` | repetition builds a new string |
| `'Hi'.lower()` | `'hi'` | a new string, not an edit |
| `'a!b'.replace('!', '')` | `'ab'` | deleting, not replacing with a space |
| `'  a\tb '.split()` | `['a', 'b']` | whitespace runs are separators |
| `' '.join(['a', 'b'])` | `'a b'` | the separator goes between the parts |
| `'Banana'.lower().count('a')` | `3` | each step works on the previous result |
| `f'{3.6666:.1f}'` | `'3.7'` | one decimal place, in text form only |

`[0]` on an empty string raises `IndexError`. `[1:4]` and `[::-1]` on an empty
string are safe: the first gives `''`, the second also `''`.

## From text to words, and back

`split()` with **no argument** treats every run of whitespace — spaces, tabs and
line breaks — as one separator, and it drops empty pieces at the ends.
`split(' ')` splits only at ordinary single spaces, so a tab is not a separator
and the empty pieces are kept.

| Expression | Result |
| --- | --- |
| `'  red\tblue  '.split()` | `['red', 'blue']` |
| `'  red\tblue  '.split(' ')` | `['', '', 'red\tblue', '', '']` |
| `'a  b'.split()` | `['a', 'b']` |
| `'a  b'.split(' ')` | `['a', '', 'b']` |
| `''.split()` | `[]` |
| `''.split(' ')` | `['']` |

That last row matters: the test "is this text empty?" is `text.split() == []`,
not `text.split(' ') == []`.

`' '.join(words)` does the opposite job: it puts one ordinary space between the
words. Changing the separator changes the result — `''.join(['a', 'b'])` is
`'ab'`, and `'-'.join(['a', 'b'])` is `'a-b'`.

## Build a string with an f-string

Calculate first, then decide how the value should look:

```python
total = 10
count = 3
average = total / count
print(f'Average: {average:.1f}')   # Average: 3.3
```

`{:...}` formats the text; it does not change the number stored in `average`.
`\n` inside an f-string starts a new line. Adjacent f-strings inside
parentheses are joined into one string, which is how the four-line report in
Task 3 is built without a long single line:

```python
report = (f'first\n'
          f'second')
```

## Predict, then run

Before running anything below, write down the four values. This is the whole
method of the session: predict, run, compare, explain the difference.

```python
original = '  Hi\tTHERE  ! '
pieces = original.lower().replace('!', '').split()
joined = ' '.join(pieces)
```

| Expression | Predicted value | Why |
| --- | --- | --- |
| `original.lower()` | `'  hi\tthere  ! '` | case changes; the tab and the spaces stay |
| `.replace('!', '')` | `'  hi\tthere   '` | the `!` disappears; the spaces around it remain |
| `.split()` | `['hi', 'there']` | the whitespace run in the middle is one separator |
| `joined` | `'hi there'` | one space between the words |
| `original` | `'  Hi\tTHERE  ! '` | none of the methods changed it |

The chain is read left to right: `lower()` produces a string, `replace()` works
on that string, and `split()` works on the result of `replace()`. Each step uses
the previous value, and `original` is never edited.

## Design checklist

Before you code:

1. What single job should this function do?
2. What is the input, and what can it look like at its smallest (empty string,
   one word, one character)?
3. What exactly should be returned — a string, a number, a tuple?
4. What is one input whose answer I can work out by hand?

Before you move on:

1. Did I actually call the function, and did I print the **returned** value?
2. Did I test an empty input and a tie or boundary case?
3. Does every path return a value of the right type?

## The tasks

| Task | Function | Practises |
| --- | --- | --- |
| 1 | `normalise_text(text)` | method chaining, `split()`/`join()`, empty result |
| 2 | `word_summary(text)` | a loop with a running best value, a tie, a tuple |
| 3 | `text_report(text)` | calling helpers, an f-string, a divide-by-zero guard |
| 4 | `initials(name)` | building a string in a loop, `upper()` |
| 5 | `count_character(text, target)` | case-insensitive counting, `str.count()` |
| 6 | `is_palindrome(text)` | cleaning text, slicing with `[::-1]` |
| 7 | `mask_email(email)` | `split('@')`, `'*' * n`, preserving case |

### Task 1 — Clean up a message

Return a cleaned version of `text`:

1. lowercase every letter and remove every `!`;
2. collapse each run of whitespace into one ordinary space, and remove leading
   and trailing whitespace;
3. return `''` when nothing remains.

Removing `!` does **not** insert a space, so `'one!two'` becomes `'onetwo'`.

```python
normalise_text('  PYTHON\tis Fun!!!  ')   # 'python is fun'
normalise_text('  Keep, THIS? 42! ')     # 'keep, this? 42'
normalise_text('')                        # ''
```

Check: `' A ! B '` → `'a b'` (remove `!` first, then the remaining two spaces
collapse), `'!!!'` → `''`, `'  \t\n '` → `''`.

Follow the text through the steps and keep each returned value:

```text
'  PYTHON\tis Fun!!!  '
  .lower()            -> '  python\tis fun!!!  '
  .replace('!', '')   -> '  python\tis fun   '
  .split()            -> ['python', 'is', 'fun']
  ' '.join(...)       -> 'python is fun'
```

**Why this works:** `split()` with no argument already handles spaces, tabs and
repeated whitespace, so `' '.join(cleaned.split())` does steps 2 and 3 in one
line. Removing `!` must happen *before* splitting: in `'a ! b'`, a leftover `!`
would sit in the word list as a word of its own.

`text.strip()` is not enough — it only removes whitespace at the two ends, not
the doubled spaces in the middle. And `replace('!', ' ')` is not the same
transformation: compare `'one!two'` with `'one two'`.

### Task 2 — Find the longest word

Return `(number_of_words, longest_word)` for `text`.

- A word is a non-empty part of `text.split()`; punctuation stays attached and
  counts towards the length.
- Preserve the spelling and case of the chosen word.
- If several words tie for longest, return the **first** one.
- Use a loop — not `max()` and not sorting.
- Empty or whitespace-only input gives `(0, '')`.

```python
word_summary('Python is fun')   # (3, 'Python')
word_summary('red blue gold')   # (3, 'blue')
word_summary('')                # (0, '')
```

Trace the loop on `'red blue gold'`:

| Step | Candidate | Length | `longest` before | Longer? | `longest` after |
| --- | --- | --- | --- | --- | --- |
| 1 | `'red'` | 3 | `''` | 3 > 0 — yes | `'red'` |
| 2 | `'blue'` | 4 | `'red'` | 4 > 3 — yes | `'blue'` |
| 3 | `'gold'` | 4 | `'blue'` | 4 > 4 — no | `'blue'` |

**Why `>` and not `>=`:** with `>=`, step 3 would replace `'blue'` with
`'gold'`, and a tie would return the *last* word instead of the first. Strictly
greater means "only a genuinely longer word wins".

Starting from `longest = ''` works for an empty word list too: the loop does not
run, and `(0, '')` is returned without a special case.

Remember that punctuation is part of the word: in `'red, blue'` the first word
is `'red,'`, length 4, so the answer is `(2, 'red,')` — a tie with `'blue'` that
the first word wins.

### Task 3 — Build a text report

Return four lines built from the first two functions:

```python
text_report('  Python\tis FUN!!! ')
```

```text
Text: python is fun
Words: 3
Longest: python
Average length: 3.7
```

Rules:

1. Call `normalise_text(text)`, then call `word_summary()` on the cleaned
   string.
2. The average is the sum of the **word** lengths divided by the word count;
   the spaces between words are not letters.
3. Use exactly the labels `Text:`, `Words:`, `Longest:` and `Average length:`,
   each followed by one space.
4. Show the average with one decimal place using an f-string.
5. When there are no words, use `0.0` and `(none)`.
6. The `Text:` line keeps its space when the text is empty, and there is **no**
   trailing newline after the last line.

```python
text_report('')
```

```text
Text: 
Words: 0
Longest: (none)
Average length: 0.0
```

That first line really is `'Text: '` — the label, then one space, then nothing.

**Why `len(cleaned)` is wrong:** for `'python is fun'`, `len(cleaned)` is 13
because the two separating spaces are characters too; 13 / 3 would print `4.3`.
Add `len(word)` over `cleaned.split()` instead, which gives 6 + 2 + 3 = 11 and
then 11 / 3 = 3.666…, displayed as `3.7`.

**Why the guard matters:** `total_length / word_count` raises
`ZeroDivisionError` when there are no words. Set `average = 0.0` first, and
divide only inside `if word_count > 0`.

For Task 3 you need Tasks 1 and 2 working. If you want to attempt the report on
its own, copy the two helpers from the
[solutions file](solutions/tutorial7_solutions.py) and keep going.

### Task 4 — Name initials

Return the uppercase initials of `name`, each followed by a full stop, with no
spaces between them.

```python
initials('Ada Lovelace')     # 'A.L.'
initials('  alan\tturing ')  # 'A.T.'
initials('')                 # ''
```

Rules: split on whitespace, take the first character of each part, uppercase it,
then add `.`. Empty or whitespace-only input returns `''`.

```python
def initials(name):
    result = ''
    for part in name.split():
        result = result + part[0].upper() + '.'
    return result
```

**Why `part[0]` is safe:** `name.split()` never produces an empty string, so
every part has a first character — even when the input has leading, trailing or
repeated whitespace. For `'   '`, `split()` returns `[]`, the loop does not run,
and `result` stays `''`.

Trace `'alan turing'`: parts `['alan', 'turing']` → `'A' + '.'` → `'A.'` →
`'A.' + 'T' + '.'` → `'A.T.'`. A one-letter part still works: `'x'` → `'X.'`.

### Task 5 — Count one character

Count how often `target` appears in `text`, ignoring letter case. `target` is
always exactly one character; it may be a space or a punctuation mark. Return an
integer.

```python
count_character('Banana', 'A')   # 3
count_character('a a', ' ')      # 1
count_character('', 'x')         # 0
```

**Lowercase both arguments.** `text.lower()` alone would compare `'banana'`
against `'A'` and count nothing. For the space target, `'a a'` has exactly one
space, so the answer is 1 — the two `a`s are not spaces.

`str.count()` is accepted because the one-character guarantee makes it agree
with a loop:

```python
def count_character(text, target):
    counter = 0
    for character in text.lower():
        if character == target.lower():
            counter = counter + 1
    return counter
```

Lowercasing does not change digits, spaces or punctuation, which is why a target
of `' '` or `'.'` still works.

### Task 6 — A different palindrome rule

Return `True` when `text` reads the same forwards and backwards **after**
ignoring letter case and **all** whitespace — but keeping digits and every
punctuation mark.

```python
is_palindrome('Never odd or even')   # True
is_palindrome('ab,ba!')              # False
is_palindrome('')                    # True
```

**Choose what to ignore before reversing.** Build one cleaned string and use it
on both sides of the comparison:

```python
def is_palindrome(text):
    compact = ''.join(text.lower().split())
    return compact == compact[::-1]
```

`split()` with no argument removes every kind of whitespace — spaces, tabs and
line breaks — and `join` glues the pieces back together with nothing between
them. `replace(' ', '')` removes only ordinary spaces, so `'a\tbba'` would still
contain a tab and be reported as `False`.

This rule keeps punctuation, which is what makes the task interesting:

| Input | Cleaned | Reverse | Result |
| --- | --- | --- | --- |
| `'Never odd or even'` | `'neveroddoreven'` | `'neveroddoreven'` | `True` |
| `'ab!ba'` | `'ab!ba'` | `'ab!ba'` | `True` |
| `'ab,ba!'` | `'ab,ba!'` | `'!ab,ba'` | `False` |
| `'a\tbba'` | `'abba'` | `'abba'` | `True` |
| `''` or `'   '` | `''` | `''` | `True` |

The last row is not a special case in the code: an empty string equals its own
reverse.

### Task 7 — Mask a username

Hide all but the first character of the part of an email address before the
`@`.

```python
mask_email('alice@example.com')   # 'a****@example.com'
mask_email('A@HKU.HK')            # 'A@HKU.HK'
```

Rules: the input has exactly one `@`, a non-empty username and a non-empty
domain, and no whitespace. Keep the username's first character, replace each
remaining username character with one `*`, and keep `@` and the whole domain
unchanged. Preserve the case of everything you keep.

```python
def mask_email(email):
    username, domain = email.split('@')
    masked = username[0] + '*' * (len(username) - 1)
    return masked + '@' + domain
```

**Count the stars:** `'alice'` has 5 characters, so 4 are masked —
`'a' + '****'`. `'A'` has 1 character, so `'*' * 0` is `''` and the address is
unchanged. `'user.name@hku.hk'` has 9 characters, so 8 stars.

`split('@')` with no limit is enough because the input guarantees exactly one
`@`. Do not lowercase the address: `'A@HKU.HK'` must stay exactly as it is.

## Testing checklist

For each function, try:

- a normal input from the examples;
- an empty string `''`, and for the name/report tasks a whitespace-only `'   '`;
- a boundary: a one-letter username, a one-word text, a tie between two
  longest words;
- a tab or line break, to prove `split()` is doing the whitespace work;
- a punctuation mark, to prove it is kept (Task 6) or counted (Tasks 2 and 5);
- a result you can verify by hand, character by character.

If a function still returns the placeholder from the starter — `''`, `0` or
`False` — the body has not been written yet. If it returns `None`, you probably
forgot the `return`.

## Common mistakes

| Mistake | What happens | Fix |
| --- | --- | --- |
| Calling `text.lower()` and ignoring the result | `text` keeps its original case | Use or return the new string |
| `split(' ')` on text containing tabs | Tabs are not separators; the word count is wrong | Use `split()` with no argument |
| `>=` in the longest-word loop | The last tied word wins | Use strict `>` |
| `len(cleaned)` as the total word length | Separating spaces are counted as letters | Add `len(word)` over `cleaned.split()` |
| Dividing by the word count without a guard | `ZeroDivisionError` on empty input | Check `word_count > 0` first |
| `replace(' ', '')` for the palindrome | Tabs and newlines survive | `''.join(text.lower().split())` |
| Printing inside the function | The caller receives `None` | `return` the value; print at the call site |
| Lowercasing the whole email | `'A@HKU.HK'` becomes `'a@hku.hk'` | Lowercase only where case must be ignored |
| No `:.1f` in the average | `3.6666666666666665` | `f'{average:.1f}'` |
| A trailing newline after the last line | Task 3 checks fail on the exact string | Stop the f-string after the average |
| `[0]` on an empty string | `IndexError` | Check for empty input, or rely on `split()` giving `[]` |

## Answers

[`solutions/tutorial7_solutions.py`](solutions/tutorial7_solutions.py) has one
possible solution per task plus an extra set of assertions:

```bash
cd solutions
python3 tutorial7_solutions.py    # prints: All checks passed.
```

Your code does not have to look like the solutions. It has to return the right
value for normal, empty, boundary and unusual inputs — and it should be short
enough that you can explain every line.
