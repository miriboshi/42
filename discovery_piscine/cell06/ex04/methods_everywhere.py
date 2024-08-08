#!/usr/bin/env python3

# Create a program methods_everywhere.py that takes parameters.
# This program must be executable.
# You must create two different methods in this program:
# The method shrink takes a string as a parameter and displays the first eight characters of that string

# Use slices.
# The method enlarge takes a string as a parameter and appends ’Z’ characters to make it a total of eight characters. Then, it displays the resulting string

# Similar to arrays, you can add characters to a string using the concatenation operator

# For each argument of the program: if the argument has more than eight characters,
# call the shrink method on it; if the argument has less than eight characters, call the enlarge method on it; 
# and if the argument has exactly eight characters, display it directly followed by a new line.
# If the number of parameters is less than 1, display ’none’ followed by a new line.

import sys

def main():
    try:
        entrada = sys.argv
        if(len(entrada) < 2 ):
            print("none")
        else:
            for palavra in entrada[1:]:
                if(len(palavra)>=8):
                    print(shrink(palavra))
                else:
                    print(enlarge(palavra))
    except Exception as e:
        print(f"An error occurred: {e}")
        

def shrink(palavra) -> str:
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
