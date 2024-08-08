#!/usr/bin/env python3
import re 
import math

# Create a program called round_up.py.
# This program should be executable.
# Your script will ask the user for a number.
# You should then display the entered number rounded up
try:
    result = 0
    number_string = input("Give me a number: ")
    #numero é recebido como string, necessário conversão, porém é necessário verificar tipo do numero
    if re.match(r'^-?\d+$', number_string):
        number = int(number_string)
    elif re.match(r'^-?\d*\.\d+$', number_string):
        number = float(number_string)

    if (number > 1):
        result = math.ceil(number)
    elif( number > 0 ) and (number < 1 ):
        result = 1
    else:
        result = math.ceil(number)

except:
    result="none"



print(result)