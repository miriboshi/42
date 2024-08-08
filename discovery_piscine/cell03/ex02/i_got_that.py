#!/usr/bin/env python3

# Create a program called i_got_that.py.
# This program should be executable.
# This script should contain a while loop that accepts user input, writes a response, and only stops when the user enters "STOP".
# Each iteration of the loop should accept user input.

resposta = input("What you gotta say? : ")
while True:
    if resposta == "STOP":
        break
    resposta = input("I got that! Anything else? : ")
