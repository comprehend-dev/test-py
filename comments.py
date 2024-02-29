# Importing os module
import os

def calculate_square(num):
    """
    This function calculates the square of a number.

    :param num: the number to calculate the square of
    :return: the square of the input number
    """
    # Calculate the square
    result = num ** 2
    
    return result

# Comment lines are also considered as insignificant code
print("The square of 5:", calculate_square(5))  # Inline comment

"""
In this script, we first import the 'os' module,
and then define a 'calculate_square' function.
The function takes in a number as an argument
and returns the square of that number.

At the end, we call the function with input 5, and print the result.
"""
