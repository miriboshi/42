#!/usr/bin/env python3

# Create a program hello_all.py.
# This program must be executable.
# This program will contain a method called "hello". This method will display "Hello, everyone!".
# After defining your method, you will test it by calling it in your program. Like in the example below, except that we have hidden the method definition

import sys

def main():
    try:
        entrada = len(sys.argv)
        if(entrada > 1 ):
            print("Invalid")
        else:
            hello()

    except Exception as e:
        print(f"An error occurred: {e}")

def hello() -> str:
    print("Hello, everyone!")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
