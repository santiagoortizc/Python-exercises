"""
Crea un programa que determine si dos vectores son ortogonales.
- Los dos array deben tener la misma longitud.
- Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""


def vectores_ortogonales(vec1: list, vec2: list) -> bool:
    if len(vec1) != len(vec2):
        raise ValueError("Los vectores no tienen la misma longitud")
    return sum(a*b for a, b in zip(vec1, vec2)) == 0


print(vectores_ortogonales([2, -8], [4, 1]))
