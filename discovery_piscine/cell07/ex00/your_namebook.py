#!/usr/bin/env python3

# Create a script called your_namebook.py.
# It should contain a method called array_of_names.
# This method takes a dictionary associating first names with last names as a parameter.
# It will build an array with the full names of the people, with the first letter capitalized. It returns this array. Refer to the example.
# For example, the following script:


import sys

def main():
    try:        
        persons = {
            "jean": "valjean",
            "grace": "hopper",
            "xavier": "niel",
            "fifi": "brindacier"
        }
        print(array_of_names(persons))
              
    except Exception as e:
        print(f"An error occurred: {e}")
        
def array_of_names(persons) -> str:
    nome_completo = '\n'.join(f'{chave} {valor}' for chave, valor in persons.items())
    return nome_completo


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
