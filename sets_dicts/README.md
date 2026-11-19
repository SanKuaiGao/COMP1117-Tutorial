# Tutorial 9 — Coding Practice: Sets and Dictionaries

A list keeps order and repeats, which is exactly what you want for a sequence of
steps. It is the wrong tool for two other jobs: "have I seen this value
already?" and "what is the value stored under this name?". This session gives
you the two containers built for those jobs and six tasks that use them to
compare, count, group and merge.

## Get started

Open [`tutorial9.py`](tutorial9.py) and run it:

```bash
python3 tutorial9.py
```

Every task starts with a placeholder value, so the file runs immediately and
prints something like `Task 2: None | expected: 1`. That is your to-do list:
replace the placeholder, run the file again, compare the two parts of the line.
Tasks 1, 3, 5 and 6 print their expected value on the next line, because the
result is too long to sit beside the label.

Dictionaries print in the order the keys were inserted, so a passing check looks
exactly like the expected text. Remember that `{'a': 1, 'b': 2}` and
`{'b': 2, 'a': 1}` are still **equal** dictionaries: order only matters for
printing, and for the two tasks that ask for it explicitly.

Tasks 5 and 6 print the input again after the call. If that line changes, your
function modified its argument.

## Which container should I use?

| | `list` | `set` | `dict` |
| --- | --- | --- | --- |
| Keeps order | yes | no | insertion order |
| Allows repeats | yes | no | keys are unique |
| Read one item | `a[0]` | not possible | `d['key']` |
| Membership test | slow scan | fast | fast, on keys |
| Written as | `[1, 2, 3]` | `{1, 2, 3}` | `{'a': 1}` |
| Empty | `[]` | `set()` | `{}` |

Ask first: do I need uniqueness or a fast membership test (set), or a lookup
from a key to a value (dict)?

## A set keeps each value once

```python
nums = [3, 1, 3, 2, 1]
unique = set(nums)
print(unique)              # {1, 2, 3}
print(len(unique))         # 3
print(2 in unique)         # True
print(5 in unique)         # False
```

Repeats disappear, and there is no `unique[0]`: a set has no index, so that line
raises `TypeError`. The printed order is not something to rely on — small
integers happen to look sorted, but sets of strings can print in a different
order on a different run.

**The `{}` trap:** `{}` makes an empty **dictionary**, not an empty set. Write
`set()` for an empty set.

```python
type({})        # <class 'dict'>
type(set())     # <class 'set'>
```

## Comparing two sets

Set operators answer "who is in both / either / only one?" without a loop:

| Operator | Meaning | Example with `a = {'Ann', 'Ben', 'Cat'}`, `b = {'Ben', 'Dan'}` |
| --- | --- | --- |
| `a & b` | in both | `{'Ben'}` |
| `a \| b` | in either | `{'Ann', 'Ben', 'Cat', 'Dan'}` |
| `a - b` | in `a`, not in `b` | `{'Ann', 'Cat'}` |
| `a ^ b` | in exactly one | `{'Ann', 'Cat', 'Dan'}` |

`&`, `|` and `^` give the same answer when you swap `a` and `b`. `-` does not:
`b - a` is `{'Dan'}`.

The result is a set, so its order is arbitrary. `sorted(...)` turns it into a
list in a fixed order, which is what makes a result easy to compare with an
expected answer:

```python
print(sorted(a & b))    # ['Ben']
```

## A dictionary maps keys to values

```python
stock = {'apple': 3, 'pear': 0}
stock['kiwi'] = 5                     # new key: adds it
stock['apple'] = stock['apple'] + 2   # existing key: replaces the value
print(stock)                          # {'apple': 5, 'pear': 0, 'kiwi': 5}
print(stock.get('mango', 0))          # 0
print('pear' in stock)                # True
print(5 in stock)                     # False
print(stock['mango'])                 # KeyError: 'mango'
```

- `in` checks **keys**, never values. `5 in stock` asks whether `5` is a key.
- `d[key]` raises `KeyError` when the key is missing.
- `d.get(key, default)` returns the default instead of raising. With no default
  it returns `None`.

Keys must be immutable (a string, an integer, a tuple). A list cannot be a key.

### The counting pattern

```python
counts = {}
for ch in 'banana':
    counts[ch] = counts.get(ch, 0) + 1
print(counts)              # {'b': 1, 'a': 3, 'n': 2}

for key, value in counts.items():
    print(key, value)
```

`get(ch, 0)` supplies `0` the first time a key is seen, so the same line handles
both a new key and an existing one. Writing `counts[ch] = counts[ch] + 1`
instead raises `KeyError` on the first `b`. Task 3 is this pattern with words.

A dictionary remembers insertion order: `counts.items()` visits `b`, `a`, `n` in
the order they first appeared.

## Predict, then run

```python
scores = {'Ann': 70, 'Ben': 85}
backup = scores
backup['Ann'] = 90
tags = set('hello')
print(scores['Ann'], len(tags), len(scores))
```

| Expression | Value | Why |
| --- | --- | --- |
| `scores['Ann']` | `90` | `backup = scores` does **not** copy; both names point to one dictionary |
| `len(tags)` | `4` | `set('hello')` is `{'h', 'e', 'l', 'o'}` — the two `l`s collapse |
| `len(scores)` | `2` | assigning to an existing key replaces a value; it does not add a key |

The printed line is `90 4 2`. If you predicted `70`, you assumed `backup` was a
copy. It is a second name for the same object:

```python
backup = dict(scores)     # a new dictionary
backup = scores.copy()    # the same thing
```

Now changing `backup` leaves `scores` alone. `dict(d)` copies the mapping, not
the values inside it; that is enough for these tasks, where the values are
strings and integers.

This aliasing idea is the whole point of Task 6: a function that returns the
right answer can still be wrong because it changed its input.

## Design checklist

Before you code:

1. Do I need unique values and fast membership (set), or a key → value lookup
   (dict), or both?
2. What is the result: a set, a sorted list, a tuple, a dictionary?
3. What does empty input look like in this result — `[]`, `set()`, `{}` or
   `None`?
4. Am I allowed to change the argument, and how would I copy it if not?
5. What tie or repeated value could make two correct-looking answers differ?

Before you move on:

1. Did I print the **returned** value?
2. Did I test empty input and a repeat?
3. Is the input still the same after the call?

## The tasks

| Task | Function | Practises |
| --- | --- | --- |
| 1 | `course_overlap(a, b)` | set algebra, `sorted()`, returning two lists |
| 2 | `first_repeat(items)` | a `seen` set, early return, `None` |
| 3 | `word_counts(text)` | the counting pattern with `.get()` |
| 4 | `most_common(counts)` | a loop with a tie-breaking rule |
| 5 | `group_by_grade(grades)` | a dictionary of lists, sorting each list |
| 6 | `merge_stock(shop_a, shop_b)` | copying a dictionary, merging counts |

### Task 1 — Courses in common

`a` and `b` are lists of course codes; a code may appear more than once.
Return a tuple `(both, only_a)`:

- `both` — codes that are in `a` **and** in `b`;
- `only_a` — codes that are in `a` but not in `b`.

Repeats count once, and each list must be sorted in ascending order. Do not
change `a` or `b`.

```python
course_overlap(['COMP1117', 'MATH1013', 'COMP1117'],
               ['MATH1013', 'ENGG1330'])
# (['MATH1013'], ['COMP1117'])

course_overlap(['A', 'B'], [])
# ([], ['A', 'B'])
```

**Which operator?** `&` is "in both", `-` is "in `a` but not in `b`". Note the
direction: `set_a - set_b` is not `set_b - set_a`.

**Why `sorted()`?** `set_a & set_b` is a set, and a set has no fixed order, so
returning it directly would fail a test that compares with a list — sometimes on
one run and not another. `sorted()` returns a plain list in a known order:

```python
def course_overlap(a, b):
    set_a = set(a)
    set_b = set(b)
    both = sorted(set_a & set_b)
    only_a = sorted(set_a - set_b)
    return both, only_a
```

`set(a)` already removes the repeated `'COMP1117'`, and it builds a new set, so
the input lists are untouched. Check `(['A', 'A'], ['A'])` → `(['A'], [])`,
`([], [])` → `([], [])`, and `(['A', 'B'], ['C'])` → `([], ['A', 'B'])`.

### Task 2 — The first repeated value

Read `items` from left to right. Return the first value whose second appearance
comes earliest. If every value appears only once, or the list is empty, return
`None`.

Use a set to remember the values seen so far. Do not use `count()` and do not
use a nested loop.

```python
first_repeat([3, 1, 4, 1, 3])   # 1
first_repeat(['a', 'b', 'c'])   # None
first_repeat([])                # None
```

The answer is `1`, not `3`, because the second `1` (index 3) is reached before
the second `3` (index 4). The question is not "which value repeats", but "which
repeat comes first".

Trace the `seen` set on `[3, 1, 4, 1, 3]`:

| index | item | `seen` before | `item in seen`? | action |
| --- | --- | --- | --- | --- |
| 0 | 3 | `set()` | no | add 3 |
| 1 | 1 | `{3}` | no | add 1 |
| 2 | 4 | `{3, 1}` | no | add 4 |
| 3 | 1 | `{3, 1, 4}` | **yes** | return `1` |

```python
def first_repeat(items):
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None
```

**Test membership before adding.** If you add first, every item is immediately
"in seen", and the function returns `items[0]`.

**Return, do not print.** The early `return item` leaves the function at once;
the `return None` after the loop is reached only when nothing repeated.

Check `[0, 1, 2, 0]` → `0`. A solution that stores the answer and tests
`if result:` would treat `0` as "no answer" — that is why the function returns
directly.

### Task 3 — Count the words

Words are `text.lower().split()`. Punctuation stays attached to its word.
Return a dictionary from each word to how many times it appears. Keys appear in
the order each word is first seen, and there are no words in an empty or
whitespace-only string, so return `{}`.

```python
word_counts('the cat and The hat')
# {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

word_counts('Go, go GO!')
# {'go,': 1, 'go': 1, 'go!': 1}

word_counts('')
# {}
```

`lower()` makes `'The'` and `'the'` the same key. `split()` with no argument
handles spaces, tabs and line breaks, and an empty string gives an empty word
list, so the loop simply never runs and `counts` stays `{}`.

```python
def word_counts(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

`'Go,'` and `'go'` are different keys. That is the stated rule for this task:
the comma is part of the word. (Tutorial 7's `replace(',', '')` would remove it,
if the rule asked for that.)

Dictionary equality ignores order, so
`{'cat': 1, 'the': 2, ...} == {'the': 2, 'cat': 1, ...}`. The insertion-order
requirement is separate — `list(counts)` should follow first appearance.

### Task 4 — The most common word

`counts` maps words to positive integers, for example the result of
`word_counts()`. Return `(word, count)` for the largest count. When several
words share the largest count, return the one that comes **first
alphabetically**. Return `('', 0)` for an empty dictionary.

Use a loop over `counts.items()` — not `max()` and not sorting.

```python
most_common({'the': 2, 'cat': 1, 'hat': 2})   # ('hat', 2)
most_common({})                               # ('', 0)
```

A tie on count is the interesting case: `'hat'` and `'the'` both have 2, and
`'hat' < 'the'` alphabetically.

| step | word, count | best before | better? | tie? | best after |
| --- | --- | --- | --- | --- | --- |
| 1 | `'the'`, 2 | `('', 0)` | 2 > 0 — yes | — | `('the', 2)` |
| 2 | `'cat'`, 1 | `('the', 2)` | 1 > 2 — no | no | `('the', 2)` |
| 3 | `'hat'`, 2 | `('the', 2)` | 2 > 2 — no | 2 == 2 and `'hat' < 'the'` — yes | `('hat', 2)` |

```python
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
```

Starting from `('', 0)` means the first word always wins on `count > 0`, and an
empty dictionary returns the required default without a special case.

Two rules, two comparisons: **strictly greater** for the count, and `<` for the
word on an equal count. Remove the tie line and `'the'` wins, because it was
inserted first — that is the mistake the task is testing for.

### Task 5 — Group students by grade

`grades` maps a student name to a grade letter. Return a new dictionary with one
key for each grade that appears, and the sorted list of names with that grade as
the value. Do not change `grades`; return `{}` for empty input.

```python
group_by_grade({'Ben': 'B', 'Cat': 'A', 'Ann': 'A'})
# {'B': ['Ben'], 'A': ['Ann', 'Cat']}

group_by_grade({})
# {}
```

Trace the loop:

| name | grade | `groups` before | action | `groups` after |
| --- | --- | --- | --- | --- |
| `Ben` | `B` | `{}` | `B` is new: create `[]`, append | `{'B': ['Ben']}` |
| `Cat` | `A` | `{'B': ['Ben']}` | `A` is new: create `[]`, append | `{'B': ['Ben'], 'A': ['Cat']}` |
| `Ann` | `A` | `{'B': ['Ben'], 'A': ['Cat']}` | `A` exists: append | `{'B': ['Ben'], 'A': ['Cat', 'Ann']}` |

Sorting each list at the end gives `{'B': ['Ben'], 'A': ['Ann', 'Cat']}`.

```python
def group_by_grade(grades):
    groups = {}
    for name, grade in grades.items():
        if grade not in groups:
            groups[grade] = []
        groups[grade].append(name)
    for names in groups.values():
        names.sort()
    return groups
```

**Why the `if grade not in groups` line is required:** the first time a grade is
seen there is no list yet, so `groups[grade].append(name)` would raise `KeyError`.
Create the empty list once, then append unconditionally.

We build a **new** dictionary and new lists, so `grades` is unchanged. Sorting
at the end is simpler than keeping every list sorted during insertion, and it
does the same job.

### Task 6 — Merge two stock lists

`shop_a` and `shop_b` map item names to non-negative quantities. Return a new
dictionary with every item from either shop; when an item is in both, add the
quantities. Keep `shop_a`'s keys in their order, followed by items that appear
only in `shop_b`, in `shop_b`'s order. Do not change either input.

```python
merge_stock({'pen': 3, 'ink': 1}, {'ink': 4, 'cap': 2})
# {'pen': 3, 'ink': 5, 'cap': 2}

merge_stock({}, {'cap': 2})
# {'cap': 2}

merge_stock({}, {})
# {}
```

```python
def merge_stock(shop_a, shop_b):
    total = dict(shop_a)
    for item, quantity in shop_b.items():
        total[item] = total.get(item, 0) + quantity
    return total
```

**`dict(shop_a)` is the whole trick.** `total = shop_a` would give the same
return value on the first call, but it would then write the merged quantities
into the caller's dictionary. `dict(shop_a)` copies the keys and values into a
new dictionary; adding to `total` leaves `shop_a` alone.

`get(item, 0)` treats an item missing from `shop_a` as zero, so one line handles
both a shared item (`3 + 4`) and a new one (`0 + 2`).

Key order comes for free: copying keeps `shop_a`'s order, and a key inserted
from `shop_b` goes at the end. Check `list(merged) == ['pen', 'ink', 'cap']`.

If `shop_b` is empty the loop does not run, and the result is already a copy of
`shop_a`.

## Testing checklist

From the last slide, and worth using for every task:

- an empty list, dictionary or string;
- repeated values, to prove a set removed them or a counter counted them;
- a tie, where two answers share the maximum;
- the input **unchanged** afterwards.

Add to that:

- a value that is "missing" but false — `0` or `''` — so a check like
  `if result:` does not hide it;
- both sides empty, and one side empty;
- a result you can verify by hand, such as `set('hello')` having four members.

If a function returns the placeholder (`[]`, `{}`, `None`, `('', 0)`), its body
has not been written yet.

## Common mistakes

| Mistake | What happens | Fix |
| --- | --- | --- |
| `{}` used for an empty set | You get an empty dictionary | `set()` |
| `unique[0]` on a set | `TypeError`: a set has no index | Iterate, or `sorted()` it first |
| `d[key]` for a key that may be missing | `KeyError` | `d.get(key, default)`, or check `in` first |
| `5 in stock` expecting a value | `in` checks keys only | `5 in stock.values()` |
| `backup = scores` | Two names, one dictionary: edits show up in both | `dict(scores)` or `scores.copy()` |
| Returning sets from Task 1 | Order is arbitrary and tests fail intermittently | `sorted(...)` to return lists |
| `set_b - set_a` in Task 1 | Flags codes only in `b`; the direction is backwards | `set_a - set_b` |
| Adding to `seen` before testing | Every item is "seen"; returns `items[0]` | Test membership first |
| `if result:` to detect no repeat | A repeat of `0` is treated as missing | `return` inside the loop; `None` after it |
| `counts[word] = counts[word] + 1` | `KeyError` on the first occurrence | `counts.get(word, 0) + 1` |
| No tie rule in Task 4 | The first-inserted word wins, not the alphabetical one | Compare words on equal counts |
| No `if grade not in groups` | `KeyError` on `groups[grade].append(...)` | Create the list on first sight |
| Returning `shop_a` itself from Task 6 | The return value looks right but the caller's dictionary changed | Start from `dict(shop_a)` |
| Relying on printed set order | Looks sorted for small integers, changes for strings | Sort before printing or comparing |

## Answers

[`solutions/tutorial9_solutions.py`](solutions/tutorial9_solutions.py) has one
possible solution per task plus a set of assertions that also check the inputs
are unchanged:

```bash
cd solutions
python3 tutorial9_solutions.py    # prints: All checks passed.
```

Your code does not have to look like the solutions. It has to return the right
value for normal, empty, boundary and unusual inputs — and it must leave its
arguments alone unless the task says otherwise.
