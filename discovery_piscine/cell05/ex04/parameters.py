#!/usr/bin/env python3

import sys

# Create a program called parameters.py.
# This program should be executable.
# The program will display the number of parameters passed to it, followed by a newline.

# Verificar o número de argumentos passados
entrada = len(sys.argv)

argumentos = entrada - 1
i = 1

for i in range(1, len(sys.argv)):
    print(f'"{sys.argv[i]}"', end=' ')
    i =+ 1

print("\nNumber of parameters: ", argumentos) 