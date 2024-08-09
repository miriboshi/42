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
        if(len(entrada) >1 ):
            print("none")
        else:
            variavel_string = "teste"
            variavel_numerica = 1
            print(f"Valor inicial da variável: {variavel_string}")    
            variavel_st = add_one(variavel_string)     
            print(f"Valor da variável após adicionar 1: {variavel_st}")
            print(f"Valor inicial da variável: {variavel_numerica}")    
            variavel_int = add_one(variavel_numerica)    
            print(f"Valor da variável após adicionar 1: {variavel_int}")

    except Exception as e:
        print(f"An error occurred: {e}")
        
def add_one(valor) -> str:
    if((type(valor)== int) or (type(valor)== float)):
        return valor + 1
    else:
        return (valor + "1")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
