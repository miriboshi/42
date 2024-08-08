#!/usr/bin/env python3

# Create a program called iszero.py
# This program should be executable. (Consider the permissions, especially)
# When executed, the program should prompt for a number to be entered.
# If the number is equal to zero, the program should display "This number is equal to zero."
# If the number is not equal to zero, the program should display "This number is different from zero."


numero_entrada = int(input())
if(numero_entrada == 0):
    saida = "This number is equal to zero."
else:
    saida = "This number is different from zero."

print(saida)