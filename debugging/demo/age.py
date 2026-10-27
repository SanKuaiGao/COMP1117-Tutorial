age = input("How old are you? ")
next_year = age + 1
print("Next year you will be", next_year)

# ---------------------------------------------------------------------
# TypeError demo: input() always returns text, even when you type digits.
#
# Run it, type 18 and press Enter. The program asks a question first, so
# this error happens while the program is already running.
#
# input() gave you the string "18", not the number 18, so line 2 tries to
# combine text with a number and Python stops.
#
# The fix belongs where the value enters the program (line 1), not on the
# line where Python complained:
#
#     age = int(input("How old are you? "))
#
# Entering "eighteen" or "18.5" would then raise a ValueError instead:
# int() can only convert text that looks like a whole number.
# ---------------------------------------------------------------------
