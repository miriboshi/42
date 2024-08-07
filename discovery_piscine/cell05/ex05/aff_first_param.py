#!/usr/bin/env python3

# Create a program called aff_first_param.py.
# This program should be executable.
# The program displays the first string parameter passed, followed by a newline.
# If there are no parameters, display "none" followed by a newline.
import sys

entrada = len(sys.argv)

if(len(sys.argv) < 2):
    print("none")
else:
    print(sys.argv[1])
