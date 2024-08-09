#!/usr/bin/env python3

import sys

# Create a program called parameters.py.
# This program should be executable.
# The program will display the number of parameters passed to it, followed by a newline.

# Verificar o número de argumentos passados
entrada = len(sys.argv[1:])
print("Number of parameters: ", entrada) 