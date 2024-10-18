"""Author: Pious Jacob
Date: 18/10/2024
Write a Python program that uses functions from the math module to perform the following operations on a number provided by the user:
    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2."""
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("Square root of number",number,":",square_root)
factorial=math.factorial(number)
print("Factorial of",number,":",factorial)
power=math.pow(number,2)
print(number,"raised to 2:",power)