celsius = input("Temperature in Celsius? ")
fahrenheit = celsius * 9 / 5 + 23
print("That is", farenheit, "degrees Fahrenheit")

# ---------------------------------------------------------------------
# Tutorial 3, Task 2 - fix the bugs with the help of a breakpoint.
#
# The program should convert a Celsius temperature to Fahrenheit:
#
#     F = C * 9 / 5 + 32
#
# Run it with 25 and it must print:
#
#     That is 77.0 degrees Fahrenheit
#
# There are three bugs, but Python only tells you about two of them.
#
# 1. Run it with 25. Fix the red messages one at a time (read the LAST
#    line of the message).
# 2. No more red messages? Test values you know: 0 C must give 32.0,
#    100 C must give 212.0.
# 3. Still wrong? Put a breakpoint on line 3, press F5, type the input
#    in the TERMINAL, and read fahrenheit in the VARIABLES panel. Then
#    look at line 2 again.
# 4. Done when 25 C prints "That is 77.0 degrees Fahrenheit" and 0 C
#    prints "That is 32.0 degrees Fahrenheit".
# ---------------------------------------------------------------------
