#!/usr/bin/env python3

# Create a program called mult.py.
# This program should be executable.
# When executed, the program should prompt for two numbers to be entered.
# The program will display whether the result of multiplying the two numbers is positive, negative, or zero.
# Then the program will display the result of the multiplication.


numero_entrada1 = int(input())
numero_entrada2 = int(input())
resultado = numero_entrada1 * numero_entrada2
saida1 = "{} * {} = {}".format(numero_entrada1,numero_entrada2,resultado)
if(int(resultado) > 0):
    saida =  "\nThe result is positive.\n"
elif(int(resultado)  < 0):
    saida = "\nThe result is negative.\n"
elif(int(resultado) == 0):
    saida = "\nThe result is positive and negative\n"

print(saida1,saida)