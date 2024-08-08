#!/usr/bin/env python3

# Create a program downcase_all.py.
# This program must be executable.
# You must define a method in this program. This method is called downcase_it.
# The downcase_it method takes a string as an argument. It should return the string in lowercase.
# Apply this method, and display its return value, on the program’s parameters.
# If there are no parameters, display "none" followed by a line break.
import sys

def main():
    try:
        entrada = sys.argv
        if(len(entrada) < 2 ):
            print("none")
        else:
            print(lowercase_it(entrada))

    except Exception as e:
        print(f"An error occurred: {e}")

def lowercase_it(frase) -> str:
    for palavra in frase:
        retorno = palavra.lower()
    return retorno


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()


