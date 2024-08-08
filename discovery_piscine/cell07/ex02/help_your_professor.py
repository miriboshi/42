#!/usr/bin/env python3

# Create a script called help_your_professor.py.
# It will contain a method called average.
# This method will take a dictionary as a parameter, associating the students’ first names with their scores on an assignment, 
# and calculate the class average for that assignment.
# For example, the following script:

import sys

def main():
    try:        
        class_3B = {
            "marine": 18,
            "jean": 15,
            "coline": 8,
            "luc": 9
        }
        class_3C = {
            "quentin": 17,
            "julie": 15,
            "marc": 8,
            "stephanie": 13
        }
        print(f"Average for class 3B: {average(class_3B)}.")
        print(f"Average for class 3C: {average(class_3C)}.")
              
    except Exception as e:
        print(f"An error occurred: {e}")
        
def average(turma) -> str:
    soma = 0
    for chave, valor in turma.items():
        soma = soma + valor

    media = (soma)/len(turma)

    return media

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
