#!/usr/bin/env python3

#  Create a program called calculator.py.
# This program should be executable.
# Your script will ask the user for two numbers.
# You must store these numbers as numerical values in two variables.
# You should then display the result of their addition, subtraction, division, and multiplication

first_number = input("Give me the first number: ")
second_number = input("Give me the second number: ")
soma = int(first_number) + int(second_number)
subtracao = int(first_number) - int(second_number)
multiplicacao = int(first_number) * int(second_number)
divisao = int(first_number) // int(second_number)
print(first_number, " + ", second_number, " = ", str(soma))
print(first_number, " - ", second_number, " = ", str(subtracao))
print(first_number, " * ", second_number, " = ", str(multiplicacao))
print(first_number, " / ", second_number, " = ", str(divisao))


#ver sugestão de melhoria de código