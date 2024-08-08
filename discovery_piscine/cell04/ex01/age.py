#!/usr/bin/env python3

# Create a program called age.py.
# This program should be executable.
# The program asks the user to enter their age and then displays the user’s age in 10 years, 20 years, and 30 years


age = input("Please tell me your age: ")
contador = 10
while (contador <=30):
    soma = int(age) + contador
    print("In {} years, you'll be {} years old.".format(contador, soma))
    contador += 10
