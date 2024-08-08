#!/usr/bin/env python3

# Take the previous program and modify it to remove duplicates from the output.
# Note that you should not explicitly remove values from your arrays.
# For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], the expected output would be:

array_primario = [2, 8, 9, 48, 8, 22, -12, 2]
array_resultado = []
contador = 0
while(contador < len(array_primario)):
    if(array_primario[contador]>5):
        novo_valor = array_primario[contador] + 2
        array_resultado.append(novo_valor)
    contador = contador + 1

print(list(set(array_primario)))
print(set(array_resultado))