#!/usr/bin/env python3

# Create a program called count_it.py.
# This program should be executable.
# The program will display "parameters:" followed by the number of parameters passed as arguments, followed by a newline. Then, for each parameter, it will display the parameter itself and its length, followed by a newline. 
# If there are no parameters, it should display "none" followed by a newline.

import sys
def main():
    try:
        entrada = len(sys.argv)
        frase = sys.argv
        if(entrada < 2):
            print("none")
        else:
            print("parameters: {}".format(entrada-1))
            for palavra in frase[1:]:
                print("{}: {}".format(palavra, len(palavra)))

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
