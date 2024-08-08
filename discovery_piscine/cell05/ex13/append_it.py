#!/usr/bin/env python3

# Create a program called append_it.py.
# This program should be executable.
# The program will display each parameter passed as an argument, one by one, by appending it with "ism".
# If the parameter already ends with "ism", it will be skipped and not displayed. If there are no parameters, it should display "none" followed by a newline.



import sys
def main():
    try:
        entrada = sys.argv[1:]
        ismo = "ism"
        if(len(entrada) < 2):
            print("none")
        else:
            for palavra in entrada:
                if(ismo not in palavra):
                    palavra_final = palavra + "ism"
                    print(palavra_final)

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()    
