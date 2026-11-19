# Sets and dictionaries cheat sheet — Tutorial 9

The two containers from this session, on one page. The
[Tutorial 9 README](README.md) explains *why*; this page is for when you only
need the spelling.

## Choosing a container

| Need | Use | Example |
| --- | --- | --- |
| An ordered sequence, repeats allowed | `list` | `[3, 1, 3]` |
| Unique values, fast "is it in here?" | `set` | `{3, 1}` |
| A value looked up by a name or key | `dict` | `{'Ann': 70}` |

| | `list` | `set` | `dict` |
| --- | --- | --- | --- |
| Order | kept | no | insertion order |
| Repeats | yes | no | keys unique |
| `a[0]` | works | `TypeError` | `d['key']` only |
| `x in a` | slow | fast | fast, **keys** |
| Empty | `[]` | `set()` | `{}` |

## Sets

```python
nums = [3, 1, 3, 2, 1]
unique = set(nums)     # {1, 2, 3}
empty = set()          # NOT {}  -- {} is a dict
```

| Operation | Example | Result |
| --- | --- | --- |
| `set(iterable)` | `set('hello')` | `{'h', 'e', 'l', 'o'}` |
| `len(s)` | `len({1, 2, 2})` | `2` |
| `x in s` | `2 in {1, 2}` | `True` |
| `s.add(x)` | `s.add(4)` | adds one value |
| `s.discard(x)` | `s.discard(4)` | removes it, no error if absent |
| `s.remove(x)` | `s.remove(9)` | removes it, `KeyError` if absent |
| `s & t` | `{1, 2} & {2, 3}` | `{2}` — in both |
| `s \| t` | `{1, 2} \| {2, 3}` | `{1, 2, 3}` — in either |
| `s - t` | `{1, 2} - {2, 3}` | `{1}` — in `s`, not `t` |
| `s ^ t` | `{1, 2} ^ {2, 3}` | `{1, 3}` — in exactly one |
| `s <= t` | `{1} <= {1, 2}` | `True` — subset |
| `s >= t` | `{1, 2} >= {1}` | `True` — superset |
| `sorted(s)` | `sorted({3, 1, 2})` | `[1, 2, 3]` |

`&`, `|` and `^` are symmetric; `-` is not. A set has no index, so `sorted()`
is how you get a stable order for printing or returning.

## Dictionaries

```python
stock = {'apple': 3, 'pear': 0}
stock['kiwi'] = 5            # adds a new key
stock['apple'] = 7           # replaces the value
```

| Operation | Example | Result |
| --- | --- | --- |
| `d[key]` | `stock['apple']` | the value; `KeyError` if missing |
| `d.get(key)` | `stock.get('mango')` | `None` if missing |
| `d.get(key, default)` | `stock.get('mango', 0)` | `0` if missing |
| `key in d` | `'pear' in stock` | `True` — keys only |
| `len(d)` | `len(stock)` | number of keys |
| `d.keys()` | `stock.keys()` | all keys |
| `d.values()` | `stock.values()` | all values |
| `d.items()` | `for k, v in d.items():` | key–value pairs |
| `d.pop(key, default)` | `stock.pop('kiwi', 0)` | value, and removes the key |
| `del d[key]` | `del stock['pear']` | removes the key; `KeyError` if missing |
| `d.update(other)` | `stock.update({'cap': 2})` | add or replace from another dict |
| `dict(d)` / `d.copy()` | `copy = dict(stock)` | a **new** dictionary |
| `d.clear()` | `stock.clear()` | removes everything |

`5 in stock` is `False` even when `5` is a value. Membership tests keys.

## Two patterns to memorise

```python
# Counting: get(key, 0) handles the first time
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

# Dict of lists: create the list on first sight, then append
groups = {}
for name, grade in grades.items():
    if grade not in groups:
        groups[grade] = []
    groups[grade].append(name)
```

## Copying: `=` is not a copy

```python
backup = scores          # same dictionary, two names
backup = dict(scores)    # new dictionary
backup = scores.copy()   # new dictionary
```

After `backup = scores`, `backup['Ann'] = 90` changes `scores` too. Copying is
what keeps a function from modifying its argument. Shallow copy: the dict is
new, the values inside it are shared.

## Recipes from the tasks

```python
# Task 1: courses in common
set_a, set_b = set(a), set(b)
both = sorted(set_a & set_b)
only_a = sorted(set_a - set_b)

# Task 2: first repeated value
def first_repeat(items):
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None

# Task 3: count words
counts = {}
for word in text.lower().split():
    counts[word] = counts.get(word, 0) + 1

# Task 4: most common, alphabetical tie-break
best_word, best_count = '', 0
for word, count in counts.items():
    if count > best_count or (count == best_count and word < best_word):
        best_word, best_count = word, count

# Task 5: group by grade
groups = {}
for name, grade in grades.items():
    groups.setdefault(grade, []).append(name)
for names in groups.values():
    names.sort()

# Task 6: merge two stock dictionaries
total = dict(shop_a)
for item, quantity in shop_b.items():
    total[item] = total.get(item, 0) + quantity
```

`setdefault(grade, [])` does the "create the list if it is missing" step in one
call. The longer `if grade not in groups` version in the README is the one to
understand first.

## Testing these containers

| Check | Why |
| --- | --- |
| `[]`, `set()`, `{}` | empty input takes a different path |
| A repeated value | proves a set deduplicated or a counter counted |
| A tie | two answers share the maximum |
| `0` or `''` as the answer | `if result:` hides false values |
| The input after the call | a correct return value can still hide a mutation |
| `list(d)` key order | the two tasks that specify key order |
| `sorted(...)` before comparing | set order is not stable between runs |

An `assert` stops at the first wrong answer, which is what you want while
developing:

```python
assert word_counts('the cat and The hat') == {'the': 2, 'cat': 1,
                                              'and': 1, 'hat': 1}
assert shop_a == {'pen': 3, 'ink': 1}   # input unchanged
```

## Mistakes at a glance

| Symptom | Cause |
| --- | --- |
| `TypeError: 'set' object is not subscriptable` | indexing a set |
| `type({})` is `dict`, not `set` | `{}` is an empty dict; write `set()` for an empty set |
| `KeyError` on the first word | `counts[word] = counts[word] + 1` |
| `KeyError` in Task 5's append | the grade's list was never created |
| Test passes one day, fails the next | returning a set and relying on its order |
| Caller's dictionary changed | `total = shop_a` instead of `dict(shop_a)` |
| First-inserted word wins a tie | missing the alphabetical tie rule |
| `False` for `5 in stock` | `in` tests keys, not values |
