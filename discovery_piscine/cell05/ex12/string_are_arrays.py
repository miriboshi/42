#!/usr/bin/env python3


# Create a program called string_are_arrays.py that takes a string as a parameter.
# This program should be executable.
# When executed, the program should display "z" for each occurrence of the character"z" in the string passed as a parameter, followed by a newline.
# If the number of parameters is different from 1, or if there are no "z" characters in the string, it should display "none" followed by a newline.

import sys
def main():
    try:
        entrada = sys.argv[1:]  # Exclui o nome do script dos argumentos
        letra = 'z'
        encontrado = False
        resultado = ""
        # Itera sobre cada argumento passado
        for argumento in entrada:
            # Itera sobre cada caractere do argumento
            for caractere in argumento:
                # Verifica se o caractere é a letra 'z'
                if caractere == letra:
                    # Imprime a letra 'z'
                    resultado += letra
                    encontrado = True

        if encontrado:
            print(resultado)
        else:
            print("none")

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()


