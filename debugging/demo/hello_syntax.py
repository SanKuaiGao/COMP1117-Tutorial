print("Hello World)

# ---------------------------------------------------------------------
# SyntaxError demo: a string that is opened but never closed.
#
# This file is broken on purpose.
#
# Python reads the whole file before running any of it, so nothing here
# runs at all. The message reports the LAST line and puts a caret ^ under
# the place where Python noticed the problem.
#
# Careful: that line is where the problem was DETECTED, not always where
# it was caused. An unclosed bracket on line 3 is often reported on line 9.
#
# The fix is one character: add the closing quote.
# ---------------------------------------------------------------------
