"""
Crea una función que retorne el número total de bumeranes de
un array de números enteros e imprima cada uno de ellos.
- Un bumerán(búmeran, boomerang) es una secuencia formada por 3 números
  seguidos, en el que el primero y el último son iguales, y el segundo
  es diferente. Por ejemplo[2, 1, 2].
- En el array[2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes([2, 1, 2] y [4, 2, 4]).
"""


def find_boomerangs(array: list):

    n = len(array)

    if n < 3:
        return "Invalid array length"

    count = 0

    for i in range(0, n-2):
        if array[i] == array[i+2] and array[i] != array[i+1]:
            print(f"[{array[i]}, {array[i+1]}, {array[i+2]}]")
            count += 1

    return f"Boomerangs encontrados: {count}"


print(find_boomerangs([2, 1, 2, 3, 3, 4, 2, 4]))
print(find_boomerangs([2, 1, 2, 1, 2]))
print(find_boomerangs([2, 1, 3]))
print(find_boomerangs([2, 1]))
