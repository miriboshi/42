#!/usr/bin/env python3

#  Create a program called isneg.py.
# This program should be executable.
# When executed, the program should prompt for a number to be entered.
# If the number is negative, the program should display "This number is negative."
# If the number is positive, the program should display "This number is positive."
# If the number is equal to zero, the program should display "This number is both positive and negative."


numero_entrada = input()
if(int(numero_entrada) > 0):
    saida = "This number is positive."
elif(int(numero_entrada)  < 0):
    saida = "This number is negative."
elif(int(numero_entrada) == 0):
    saida = "This number is both positive and negative."

print(saida)