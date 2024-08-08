#!/usr/bin/env python3

# Create a program called advanced_mult.py.
# This program should be executable.
# This program will display all multiplication tables in the following format:

import sys

entrada = len(sys.argv)
if(entrada < 2):
    multiplicado = 0
    while multiplicado < 11:
        fator = 0
        table = []
        while fator < 11:
            produto = multiplicado * fator 
            table.append(str(produto))
            fator += 1
        print("Table de {}: {}".format(multiplicado, " ".join(table)))
        multiplicado = multiplicado + 1
else:
    print("none")