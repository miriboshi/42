#!/usr/bin/env python3

# Create a program called aff_rev_params.py.
# This program should be executable.
# When executed, the program should display all the strings passed as parameters, followed by a newline, in reverse order.
# If there are fewer than two parameters, it should display none followed by a newline.

import sys
def main():
    try:
        entrada = sys.argv
        contador = len(entrada) -1
        if (len(entrada) <= 2):
            print("none")
        else:
            while (contador > 0):
                print(entrada[contador])
                contador -=1


    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
