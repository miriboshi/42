#!/usr/bin/env python3

# Create a program called downcase_it.py.
# This program should be executable.
# The program takes a string as a parameter.
# It should display the string in lowercase, followed by a newline.
# If the number of parameters is different from 1, it should display "none" followed by a newline

import sys
def main():
    try:
        entrada = sys.argv[1:]
        if (len(entrada) < 1):
            print("none")
        else:
            for palavra in entrada:
                print(f'"{palavra.lower()}"', end='')

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
