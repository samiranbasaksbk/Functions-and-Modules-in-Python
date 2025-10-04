# Task 2: Using the Math Module for Calculations

import math

# Taking input from the user
num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number for logarithm calculation.")
else:
    # Using math module functions
    sqrt_value = math.sqrt(num)
    log_value = math.log(num)
    sine_value = math.sin(num)  # num is treated as radians

    # Displaying the results
    print(f"\n--- Calculated Results ---")
    print(f"Square Root of {num}: {sqrt_value}")
    print(f"Natural Logarithm of {num}: {log_value}")
    print(f"Sine of {num} radians: {sine_value}")
