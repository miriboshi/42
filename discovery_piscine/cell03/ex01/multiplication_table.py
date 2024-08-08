#!/usr/bin/env python3

# Create a program called multiplication_table.py.
# This program should be executable.
# The program accepts user input. This input is a number, which you will store in a numeric variable.
# This number represents the multiplication table you will display. (For example, if the input is 2, you need to display the table for 2)

numero = int(input())
contador = 0
while(contador < 10):
    multiplicacao = numero * contador
    print("{} x {} = {}".format(contador, numero, numero * contador))
    #print(f"{contador} x " )
    contador = contador + 1

