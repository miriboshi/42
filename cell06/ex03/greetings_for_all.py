#!/usr/bin/env python3

# Create a program greetings_for_all.py that does not take any parameters.
# This program must be executable.
# Create a method inside called greetings that takes a name as a parameter and displays a welcome message with that name.
# If the method is called without an argument, its default parameter will be "noble stranger".
# If the method is called with an argument that is not a string, an error message should be displayed instead of the welcome message

import sys

def main():
    try:
        entrada = len(sys.argv)
        if(entrada > 1 ):
            print("none")
        else:
            print(greetings('Alexandra'))
            print(greetings('Wil'))
            print(greetings())
            print(greetings(42))

    except Exception as e:
        print(f"An error occurred: {e}")

def greetings(nome=None) -> str:
    try:
        if nome is not None:
            if isinstance(nome, str):
                retorno = f'Hello, {nome}'
            else:
                retorno = "Error! The name must be a string."
        else:
            retorno = "Hello, noble stranger."
        
        return retorno
    
    except Exception as e:
        return f"Error! {e}"



# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
