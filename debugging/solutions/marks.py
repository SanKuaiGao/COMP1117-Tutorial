"""Tutorial 3, Task 1 - one possible solution.

The three bugs in practice/marks.py, in the order Python reports them:

1. SyntaxError, line 5:  print("Average:" average)
   Two arguments need a comma between them: print("Average:", average)

2. TypeError, line 4:  mark3 = "70"
   "70" with quotes is text, so / cannot divide it. Remove the quotes.

3. Logic error, line 4:  mark1 + mark2 + mark3 / 3
   Division happens before addition, so only mark3 was divided by 3.
   Group the sum first:  (mark1 + mark2 + mark3) / 3

Result:
    Average: 80.0
"""

mark1 = 80
mark2 = 90
mark3 = 70
average = (mark1 + mark2 + mark3) / 3
print("Average:", average)
