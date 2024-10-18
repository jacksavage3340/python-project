"""Author: Pious Jacob
Date: 18/10/2024
Write a Python program that asks the user to input their name and age. After receiving the input,
display a message that includes the user's name and age.
Expected Output:
Enter your name: John
Enter your age: 25
Hello, John! You are 25 years old."""
n=input("Enter your name:")
a=int(input("Enter your age:"))
print("Hello",n+"! You are",a,"years old.")

'''Task 2
Write a Python program that stores a string in a variable.
Extract a specific part of the string (substring) and then concatenate it with another string.
Finally, display the new string.'''
str1="Hello, World!"
str2=" Everyone!"
str3=str1[7:12]+str2
print(str3)

