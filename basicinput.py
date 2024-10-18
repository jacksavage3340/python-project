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
#task2

"""Author: Pious Jacob
Date: 18/10/2024
Write a Python program that demonstrates the usage of arithmetic, comparison, and logical operators.
Perform a few operations and print the results."""
a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
print("Sum:",a+b,"Division:",a/b)
print("Is a greater than b?:",a>b)
print("Are a and b equal?:",a==b)
print("Logical AND:",a>0 and b>0)
print("Logical OR:",a>0 or b>10)
#taks3