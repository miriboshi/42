#!/usr/bin/env python3

# Create a program called parameter_matching.py.
# This program should be executable.
# If a parameter is passed as an argument to the program, it should prompt the user to enter a word.
# If the word entered by the user is the same as the parameter passed, the program should display "Good job!". Otherwise, it should display "Nope, sorry..." followed by a newline.
# If the number of parameters passed to the program is different from 1, it should display "none" followed by a newline.


import sys
def main():
    try:
        entrada = len(sys.argv)
        if(entrada == 2):
            palavra = input("What was the parameter? ")
            if(palavra == sys.argv[1]):
                print("Good job!")
            else:
                print("Nope, sorry..")
        elif(entrada != 2):
            print("none")
    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()