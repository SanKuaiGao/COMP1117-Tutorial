mark1 = 80
mark2 = 90
mark3 = 70
print("marks:", mark1, mark2, mark3)
print("sum:", mark1 + mark2 + mark3)
average = mark1 + mark2 + mark3 / 3
print("average:", average)

# ---------------------------------------------------------------------
# Diagnosing demo/marks.py with print(): look at the values first.
#
# The wrong expression on line 6 is kept exactly as it is. Printing the
# inputs and the sum shows which step first produces a wrong value.
#
# Output:
#
#     marks: 80 90 70
#     sum: 240
#     average: 193.33333333333334
#
# Inputs are correct, the sum is correct, so the mistake is in the
# average line itself. Compare with solutions/marks.py.
#
# Temporary print() calls are a diagnostic tool: delete them when the
# task asks for an exact output format.
# ---------------------------------------------------------------------
