# Tutorial 3 — Debugging

Finding out *why* a program is wrong, instead of changing lines until the red
text disappears.

A bug is not a punishment. An error message is the computer telling you where it
first noticed a problem.

## What is in this folder

| Path | What it demonstrates | Broken on purpose? |
| --- | --- | --- |
| [`demo/hello.py`](demo/hello.py) | Your first program from Tutorial 1 still runs | No |
| [`demo/hello_syntax.py`](demo/hello_syntax.py) | A `SyntaxError`: a string without its closing quote | **Yes** |
| [`demo/age.py`](demo/age.py) | A `TypeError`: `input()` returns text, not a number | **Yes** |
| [`demo/marks.py`](demo/marks.py) | A logic error: runs, but the average is wrong | **Yes** — keep it for the debugger demo |
| [`demo/marks_print.py`](demo/marks_print.py) | The same logic error, diagnosed with `print()` | Wrong result, by design |
| [`practice/marks.py`](practice/marks.py) | **Task 1**: three bugs, one of each kind | **Yes** — your task |
| [`practice/temperature.py`](practice/temperature.py) | **Task 2**: three bugs, two with messages | **Yes** — your task |
| [`solutions/`](solutions/) | Worked answers with each bug explained | No |

Run a file from this folder with:

```bash
python3 demo/marks.py
```

or open it in VS Code and use **Run Python File**.

## Three kinds of problems

| Kind | When it happens | Example | What you see |
| --- | --- | --- | --- |
| **Syntax error** | Before anything runs — Python cannot read the file | `print("Hello World)` | `SyntaxError`, with a line number and a `^` |
| **Runtime error** | While the program is running | `"18" + 1` | `TypeError`, `NameError`, `ValueError`, … and the program stops |
| **Logic error** | Never — the program is valid | `a + b + c / 3` | No message at all; only a wrong answer |

A program can finish without any error message and still be wrong. That is why
you need an expected result to compare against.

## The debugging routine

```text
predict → run → inspect → change one thing → retest
```

1. **Predict.** What should happen for *this* input? Write the expected value
   down.
2. **Run.** What actually happens? Keep the same input while you diagnose, so
   that comparisons mean something.
3. **Inspect.** Read the error, or print the values, or pause in the debugger.
4. **Change one thing**, and be able to say *why* that change should help.
5. **Retest.** The same case first, then another case you know the answer to.

Changing five lines at once and hoping is not debugging: if it starts working,
you have learned nothing about what was wrong.

## Reading an error message

Python prints a traceback. Read it **from the bottom up**:

```text
  File "/Users/you/COMP1117-Tutorial/debugging/demo/age.py", line 2, in <module>
    next_year = age + 1
                ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

1. **Last line** — the error type and the message. `TypeError`: the operation
   does not work with these types of value.
2. **The line above it** — the file, the line number and the offending code.
3. **The caret `^`** — where Python noticed it.

The reported location is where the problem was **detected**, not always where it
was **caused**. An unclosed bracket on line 10 is often reported on line 20.

## Tool 1: `print()` to look inside

Insert temporary prints *before* you change the suspicious line:

```python
mark1 = 80
mark2 = 90
mark3 = 70
print("marks:", mark1, mark2, mark3)          # inputs: 80 90 70
print("sum:", mark1 + mark2 + mark3)          # sum: 240
average = mark1 + mark2 + mark3 / 3           # still the broken line
print("average:", average)                    # 193.33333333333334
```

Inputs are correct, the sum is correct, the average is wrong → the mistake is in
the average line. That is evidence, not a guess.

Delete the temporary prints when the task requires an exact output format.

## Tool 2: the VS Code debugger

| Action | What it does |
| --- | --- |
| **Run Python File** | Runs the program normally: no pauses, output in the Terminal |
| **Start Debugging** (`F5`) | Runs the program under the debugger, so breakpoints work |
| **Breakpoint** (click left of a line number) | Pauses **before** that line executes |
| **VARIABLES panel** | Shows every variable that currently exists, and its value |
| **Step Over** (`F10`) | Executes the next statement, then pauses again |
| **Continue** (`F5`) | Runs to the next breakpoint, or to the end |
| **Stop** (`Shift+F5`) | Ends the debug session and returns you to editing |

A breakpoint only pauses when you **start a debugging session** — running the
file normally ignores it. If the program asks for input, the question appears in
the **Terminal**: click it, type the value, press Enter.

If a variable is not in VARIABLES yet, the assignment has not run: pause *after*
that line, or step over it once.

## Task 1 — Fix the bugs

Open [`practice/marks.py`](practice/marks.py).

```python
mark1 = 80
mark2 = 90
mark3 = "70"
average = mark1 + mark2 + mark3 / 3
print("Average:" average)
```

Make it print exactly:

```text
Average: 80.0
```

There are three bugs, one of each kind. Python reports them one at a time, in
this order: `SyntaxError` → `TypeError` → wrong answer (no message).

Work like this:

1. Run it. Read the last line of the message.
2. Fix one thing. Run again.
3. When there is no red message but the answer is still wrong, add a `print()`
   or set a breakpoint and look at the variables.
4. Extra test: change the marks to 100, 100, 100 — do you get `100.0`?

<details>
<summary>Hints, one level at a time</summary>

- Bug 1: the two items inside `print()` need something between them.
- Bug 2: `"70"` with quotes is text. What happens if you remove the quotes?
- Bug 3: which operation runs first in `a + b + c / 3`? You want the sum to be
  divided, so group it.

</details>

Answer: [`solutions/marks.py`](solutions/marks.py).

## Task 2 — Debug with a breakpoint

Open [`practice/temperature.py`](practice/temperature.py).

```python
celsius = input("Temperature in Celsius? ")
fahrenheit = celsius * 9 / 5 + 23
print("That is", farenheit, "degrees Fahrenheit")
```

The rule is °F = °C × 9 / 5 + 32. With 25 as input it must print:

```text
That is 77.0 degrees Fahrenheit
```

1. Run it with `25`. Fix the red messages one at a time (read the last line!).
2. No more red messages? Test values you know: 0 °C must give 32.0, 100 °C must
   give 212.0.
3. Still wrong? Put a breakpoint on the `print` line, press `F5`, type the input
   in the **Terminal**, and read `fahrenheit` in the VARIABLES panel. Then look
   at the calculation again.
4. Done when 25 °C prints `That is 77.0 degrees Fahrenheit` and 0 °C prints
   `That is 32.0 degrees Fahrenheit`.

Three bugs, but Python only tells you about two of them.

<details>
<summary>Hints, one level at a time</summary>

- Bug 1: `input()` gives you text. `"25" * 9` is `"252525252525252525"`, and that
  cannot be divided. Convert the value where it enters the program.
- Bug 2: one variable name is spelled differently from the others.
- Bug 3: at 0 °C the program prints 23.0. Test with a known answer to find the
  wrong constant.

</details>

Answer: [`solutions/temperature.py`](solutions/temperature.py).

## Common messages, and what they usually mean

| Message | Usual cause | What to change |
| --- | --- | --- |
| `SyntaxError: invalid syntax` | A missing comma, bracket, quote or colon | Look at the caret `^`; check the line above too |
| `SyntaxError: unterminated string literal` | A quote was opened and never closed | Add the closing quote |
| `IndentationError: unexpected indent` | Inconsistent spaces at the start of a line | Use 4 spaces consistently; let VS Code indent for you |
| `NameError: name 'prnt' is not defined` | A typo, or a variable used before it is assigned | Check the spelling and the order of the lines |
| `TypeError: can only concatenate str (not "int") to str` | Adding text and a number | `int()` / `str()` conversion at the point the value enters |
| `TypeError: unsupported operand type(s) for /: 'str' and 'int'` | Arithmetic on text (`input()` returns text) | Convert with `int()` or `float()` |
| `ValueError: invalid literal for int() with base 10: 'abc'` | `int()` received something that is not a number | Validate the input, or enter an integer |
| `ZeroDivisionError: division by zero` | Dividing by a length or a value that is 0 | Check for the empty case before dividing |

The exact wording of a message varies between Python versions; the error **type**
and the line number are the parts that matter.

## Running into a problem?

| Symptom | What to do |
| --- | --- |
| The program pauses on a red line and does nothing | It is waiting for input in the **Terminal** |
| The breakpoint never pauses | You used **Run Python File**; use **Start Debugging** |
| A variable is missing from VARIABLES | Pause after its assignment, or step over that line |
| You edited the program while it was paused | **Stop**, save, then start a fresh debugging session |
| No red squiggle, but the answer is wrong | It is a logic error: compare with a known answer, print values, set a breakpoint |
