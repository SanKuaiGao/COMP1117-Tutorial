mark1 = 80
mark2 = 90
mark3 = 70
average = mark1 + mark2 + mark3 / 3
print("Average:", average)

# ---------------------------------------------------------------------
# Logic error demo: the program runs, but the answer is wrong.
#
# Expected: Average: 80.0
# Actual:   Average: 193.33333333333334
#
# There is no error message, so the only way to find this bug is to
# compare the answer with one you worked out yourself.
#
# Division happens before addition, so only mark3 is divided by 3.
#
# Keep this file broken on purpose: Tutorial 3 uses line 5 for the
# breakpoint demonstration. The repaired version is in solutions/marks.py.
# ---------------------------------------------------------------------
