#!/usr/bin/env python3


# Create a program called to25.py.
# This program should be executable.
# The program accepts user input. This input is a number, which you will store in a numeric variable.
# Next, create a loop that displays all the numbers from the input number up to 25.
# If the input number is greater than 25, display "Error" followed by a new line

numero = int(input("Enter a number less than 25: "))
if (numero > 25):
    print("Error")
else:
    while(numero <= 25):
        print("Inside the loop, my variable is ", numero)
        numero += 1
