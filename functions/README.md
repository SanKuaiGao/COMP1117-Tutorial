# Tutorial 6 — Coding Practice: Functions

Turning repeated logic into functions, using parameters and return values, and
testing each function with examples you can check by hand.

## Get started

Open [`tutorial6.py`](tutorial6.py) and run it:

```bash
python3 tutorial6.py
```

Every task starts with a placeholder value, so the file runs immediately and
prints something like `Task 1: (0, 0) | expected: (12, 14)`. That is your to-do
list: replace the placeholder, run the file again, compare the two halves of the
line.

The tests at the bottom of the file are a starting point, not a full test suite.
Add your own cases.

## Anatomy of a function

```python
def rectangle_area(width, height):     # header: def, name, parameters, colon
    area = width * height              # body: indented, runs when called
    return area

result = rectangle_area(4, 3)          # call: arguments 4 and 3
print(result)                          # 12
```

| Term | Meaning | In the example |
| --- | --- | --- |
| **Parameter** | A name in the function definition | `width`, `height` |
| **Argument** | A value supplied in a call | `4`, `3` |
| **Return value** | A value sent back to the caller | `12` |

`print` displays a value on the screen; `return` gives a value back to the
caller, which can store it, compare it, or pass it to another function. A
function that only prints cannot be tested easily, so **return** the result and
print it at the call site.

## Trace before you run

```python
def add_tax(price, rate):
    return price * (1 + rate)

first = add_tax(100, 0.1)
second = add_tax(first, 0.05)
print(second)
```

Write the intermediate values down before you execute it:

| Step | Value |
| --- | --- |
| `first` | `100 * 1.1` = `110.0` |
| second call's arguments | `first` (110.0) and `0.05` |
| `second` | `110 * 1.05` = `115.5` |

The return value of the first call becomes an argument of the second — that is
what makes functions reusable. (If you run it, Python may print
`115.50000000000001`. That is ordinary binary floating-point rounding, not a bug
in your code.)

## Design checklist

Before you code:

1. What single job should this function do?
2. What inputs does it need?
3. What value should it return?

Before you move on:

1. Did I actually call the function?
2. Did I test a boundary case?
3. Does every path return a value?

Name functions after their job: `count_vowels` is clearer than `cv`.

## The tasks

| Task | Function | Practises |
| --- | --- | --- |
| 1 | `rectangle_metrics(w, h)` | returning two values as a tuple |
| 2 | `celsius_to_fahrenheit(c)` | a formula, returning instead of printing |
| 3 | `delivery_fee(weight, express)` | two independent conditions |
| 4 | `count_vowels(text)` | a loop with an accumulator, `lower()` |
| 5 | `list_average(numbers)` | an early return, the empty case |
| 6 | `is_prime(n)` | multiple return paths, a `while` loop |
| 7 | `letter_grade(mark)`, `grade_report(name, mark)` | one function calling another |

### Task 1 — Rectangle metrics

Return both the area and the perimeter of a rectangle **as a tuple**:

- area = width × height
- perimeter = 2 × (width + height)

```python
area, perimeter = rectangle_metrics(4, 3)
print(area)        # 12
print(perimeter)   # 14
```

Check: `(1, 1)` → `(1, 4)`, `(5, 2)` → `(10, 14)`.
`return area, perimeter` builds the tuple; the caller unpacks it.

### Task 2 — Temperature converter

`F = C * 9 / 5 + 32`, returned, not printed.

Check: `0` → `32.0`, `100` → `212.0`, `-40` → `-40.0`.
In Python `/` always gives a float, so `0` is not special-cased.

### Task 3 — Delivery fee

Base fee $25; add $8 for each kg **above** 2 kg; add $15 when `express` is
`True`.

Check: `(1.5, False)` → `25`, `(4, False)` → `41`, `(4, True)` → `56`.
Boundaries worth testing: `(2, False)` → `25`, `(2.5, False)` → `29`,
`(2, True)` → `40`.

Why two separate `if` statements instead of `elif`? Express service can apply
whether or not the parcel is over 2 kg, so the two surcharges are independent.

### Task 4 — Count vowels

Count `a, e, i, o, u` in a string, ignoring case, and return an integer.

Check: `"Hello"` → `2`, `"FUNCTIONS"` → `3`, `"rhythm"` → `0`.
Hint: loop through `text.lower()` and test `if character in "aeiou"`.
The accumulator changes only when the condition is true.

### Task 5 — List average

Add the numbers with a **loop** (not `sum()`), and return `None` for an empty
list, otherwise `total / len(numbers)`.

Check: `[2, 4, 6]` → `4.0`, `[5]` → `5.0`, `[]` → `None`.

Handle the empty list first and return early: that avoids `ZeroDivisionError`,
and the rest of the function can then assume at least one value exists.
`None` is the honest answer — no average exists for an empty list.

### Task 6 — Prime checker

Return `True` when `n` is prime, otherwise `False`. A prime is an integer
greater than 1 with no divisor except 1 and itself, so 0, 1 and negative numbers
are not prime.

Check: `2` → `True`, `9` → `False`, `17` → `True`, `1` → `False`.

Hint: if `n % divisor == 0` you have found a divisor. Testing divisors up to
`n - 1` is correct; stopping at `divisor * divisor <= n` is faster and still
correct.

### Task 7 — Grade report

Write two functions:

- `letter_grade(mark)` returns `"A"` for mark ≥ 80, `"B"` ≥ 70, `"C"` ≥ 60,
  `"D"` ≥ 50, otherwise `"F"`.
- `grade_report(name, mark)` **calls** `letter_grade` and returns
  `"Ada: 84 (A)"`.

Test every threshold from both sides: 80, 79, 70, 69, 60, 59, 50, 49.
Checking from the highest threshold down makes each early `return` correct.

## Testing checklist

- A normal input
- A boundary value
- An empty or smallest input
- A result you can verify by hand

## Common mistakes

| Mistake | What happens | Fix |
| --- | --- | --- |
| Calling before defining | `NameError` | Define the function above the call |
| Missing `return` | The function returns `None` | Return the value you computed |
| Printing instead of returning | The caller receives `None` | `return` the value; print at the call site |
| Wrong indentation | `IndentationError`, or code outside the function | The whole body belongs to the function block |
| Testing only one case | A boundary bug survives | Add boundary and empty cases |
| Forgetting to update a variable in a `while` loop | The loop never ends | Change the counter inside the loop |

## Answers

[`solutions/tutorial6_solutions.py`](solutions/tutorial6_solutions.py) has one
possible solution per task plus a set of assertions:

```bash
cd solutions
python3 tutorial6_solutions.py    # prints: All checks passed.
```

Your code does not have to look like the solutions. It has to return the right
value for normal, boundary and unusual inputs.
