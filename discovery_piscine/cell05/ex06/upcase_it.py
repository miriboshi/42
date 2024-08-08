#!/usr/bin/env python3


# Create a program called upcase_it.py that takes a string as a parameter.
# This program should be executable.
# The program should display the string in uppercase, followed by a newline.
# If the number of parameters is different from 1, display "none" followed by a newline.


import sys
def main():
    try:
        entrada = sys.argv[1:]
        if (len(entrada) < 1):
            print("none")
        else:
            for palavra in entrada:
                print(f'"{palavra.upper()}"', end='')

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
