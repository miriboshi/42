#!/usr/bin/env python3

# Create a program called scan_it.py.
# This program should take two parameters.
# The first parameter is a keyword to search for in a string.
# The second parameter is the string to be searched.
# This program should be executable.
# When executed, the program should display the number of times the keyword appears in the string.
# If the number of parameters is different from 2 or if the first string does not appear in the second, it should display none followed by a newline.


import sys
def main():
    try:
        entrada = sys.argv[1:]
        if (len(entrada) != 2):
            print("none")
        else:
            if entrada[0] in entrada[1]:
              quantidade = entrada[1].count(entrada[0])
              print(quantidade)

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
