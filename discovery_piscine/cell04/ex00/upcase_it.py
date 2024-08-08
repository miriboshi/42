#!/usr/bin/env python3

# Create a program called upcase_it.py.
# This program should be executable. (Remember permissions, in particular)
# This script will first ask the user for a word, then display it in uppercase
def main():
    word = input("Give me a word: ")
    try:
        if(word == None or word.isdigit() ):
            print("Invalid")
        else:
            print(word.upper())

    except Exception as e:
        print(f"An error occurred: {e}")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
