#!/usr/bin/env python3
import re

# Create a program called float.py.
# This program should be executable.
# Your script will ask the user for a number.
# You should then display whether the entered number is a decimal or not.


entrada = input("Give me a number: ")
# if re.match(r'^-?\d+$', entrada):
#'^-?\d+$'
# ^:Indica o início da string. Garante que a correspondência comece desde o início da string.
# -?: - é um caractere literal que representa um sinal negativo.  O ? após o - torna o sinal negativo opcional. Portanto, a string pode começar com um - ou não. Esse -? permite que a expressão corresponda tanto a números positivos quanto a números negativos.
# \d+:  representa um dígito (0-9). + significa "um ou mais" dígitos. Portanto, \d+ corresponde a uma sequência de um ou mais dígitos. Isso indica que a parte inteira do número deve conter pelo menos um dígito.
# $:Indica o final da string. Garante que a correspondência vá até o final da string.
#     tipo = "Inteiro"
# elif re.match(r'^-?\d*\.\d+$', entrada):
#r'^-?\d*\.\d+$'
# ^:Indica o início da string. Garante que a correspondência comece desde o início da string.
# -?: - é um caractere literal que representa um sinal negativo.
# ? após o - torna o sinal negativo opcional, ou seja, a string pode começar com um - ou não.
# \d*:\d representa um dígito (0-9). * significa "zero ou mais" dígitos. Portanto, \d* corresponde a uma sequência de zero ou mais dígitos. Isso permite que a parte inteira do número seja opcional ou que não haja dígitos antes do ponto decimal.
# \.: corresponde a um ponto literal. Em expressões regulares, o ponto é um caractere especial que representa qualquer caractere, então usamos a barra invertida (\) para escapá-lo e fazer com que corresponda ao ponto real.
# \d+:representa um dígito (0-9). + significa "um ou mais" dígitos. Portanto, \d+ corresponde a uma sequência de um ou mais dígitos, que são obrigatórios após o ponto decimal.
# $: Indica o final da string. Garante que a correspondência vá até o final da string.
#    tipo = "Float"
inteiro = False
flutuante = False

try:
    int(entrada)
    inteiro = True
except ValueError:
    inteiro = False
    try:
        float(entrada)
        flutuante = True
    except ValueError:
        flutuante = False

if flutuante:
    tipo = "This number is a decimal"
elif inteiro:
    tipo = "This number is an integer"
else:
    tipo = "Not a number"

print(tipo)
