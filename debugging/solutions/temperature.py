"""Tutorial 3, Task 2 - one possible solution.

The three bugs in practice/temperature.py, in the order Python reports them:

1. TypeError, line 2:  celsius = input(...)
   input() returns text. Python repeats the text instead of multiplying
   the number, and then cannot divide the result. Convert where the value
   enters the program:  celsius = int(input(...))

2. NameError, line 3:  farenheit
   A spelling mistake in a variable name. It must match fahrenheit.

3. Logic error, line 2:  + 23 instead of + 32
   There is no message for this one. Testing 0 C (which must give 32.0)
   makes the wrong constant obvious.

Checks: 0 -> 32.0, 25 -> 77.0, 100 -> 212.0
"""

celsius = int(input("Temperature in Celsius? "))
fahrenheit = celsius * 9 / 5 + 32
print("That is", fahrenheit, "degrees Fahrenheit")
