#!/usr/bin/env python3

# Create a program called play_with_arrays.py.
# This program should be executable.
# First, define an array of numbers.
# Then, iterate over this array and build a new array by adding 2 to each value of the original array.
# You should have two arrays in your program: the original array and the new array you created.
# Finally, display both arrays on the screen.
# For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], you should have the following output:

array_primario = [2, 8, 9, 48, 8, 22, -12, 2]
array_resultado = []
contador = 0
while(contador < len(array_primario)):
    if(array_primario[contador]>5):
        novo_valor = array_primario[contador] + 2
        array_resultado.append(novo_valor)
    contador = contador + 1

print(array_primario)
print(array_resultado)