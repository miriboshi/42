#!/usr/bin/env python3


# Create a program upcase_it.py (again!)
# This program must be executable.
# You must define a method in this program. This method is called upcase_it.
# The upcase_it method takes a string as an argument. It should return the string in uppercase.
# Test the method by calling it in your program. In the example below, we test it with "hello"
import sys

def main():
    try:
        entrada = len(sys.argv)
        if(entrada > 1 ):
            print("Invalid")
        else:
            print(upcase_it("hello"))

    except Exception as e:
        print(f"An error occurred: {e}")

def upcase_it(word) -> str:
    retorno = word.upper()
    return retorno


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()


