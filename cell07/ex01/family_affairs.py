#!/usr/bin/env python3

# Create a script called family_affairs.py.
# It will contain a method called find_the_redheads.
# This method will take a dictionary as a parameter, representing family members with their first name as the key and their hair color as the value.
# This method will use the filter function to gather the first names of the red-haired individuals into a new list, which it will return.
# For example, the following script:

import sys

def main():
    try:        
        dupont_family = {
            "florian": "red",
            "marie": "blond",
            "virginie": "brunette",
            "david": "red",
            "franck": "red"
        }
        print(find_the_redheads(dupont_family))
              
    except Exception as e:
        print(f"An error occurred: {e}")
        
def find_the_redheads(dupont) -> str:
    nome_completo = []
    valor_procurado = "red"
    for chave, valor in dupont.items():
        if valor == valor_procurado:
            nome_completo.append(chave)
    return nome_completo


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
