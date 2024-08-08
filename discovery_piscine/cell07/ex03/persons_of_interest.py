# Create a script called persons_of_interest.py.
# It will contain a method called famous_births.
# This method will take a dictionary representing historical figures as a parameter. 
# Each entry in the dictionary is itself a dictionary with the keys: :name and :date_of_birth.
# The method will sort the dictionary passed as a parameter in order of birth dates, and then display each entry (see the example below).
# For example, the following script

import sys

def main():
    try:        
        women_scientists = {
            "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
            "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
            "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
            "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
        }

        famous_births(women_scientists)
              
    except Exception as e:
        print(f"An error occurred: {e}")
        
def famous_births(turma) -> str:
    # is a great scientist born in
    return

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
