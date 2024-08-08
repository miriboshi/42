#!/usr/bin/env python3

# Create a program called scope_that.py that does not take any parameters.
# This program must be executable.
# Inside the program, create a method called add_one that takes a parameter and adds 1 to the parameter passed to the method.
# Initialize a variable in the body of the program, display it, and then call the method that adds 1.
# Display your variable again in the body of the program.
# What do you observe?


import sys

def main():
    try:
        entrada = sys.argv
        if(len(entrada) < 2 ):
            print("none")
        else:
            add_one())
    except Exception as e:
        print(f"An error occurred: {e}")
        

def add_one(palavra) -> str:
    try:
        if len(palavra) > 8:
            retorno = (palavra[:8])
        else:
            retorno = palavra
        
        return retorno
    
    except Exception as e:
        return f"Error! {e}"
    
    
def enlarge(palavra) -> str:
    try:
        letra = "z"
        count = len(palavra)
        while (count < 8):
            palavra = palavra + letra
            count += 1        
                
        return palavra
    
    except Exception as e:
        return f"Error! {e}"




# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
