"""
Crea una función que calcule el valor del parámetro perdido
correspondiente a la ley de Ohm.
- Enviaremos a la función 2 de los 3 parámetros(V, R, I), y retornará
  el valor del tercero(redondeado a 2 decimales).
- Si los parámetros son incorrectos o insuficientes, la función retornará
  la cadena de texto "Invalid values".
"""


def ohm(v: float | None = None, r: float | None = None, i: float | None = None) -> float | str:
    valid = []
    if v is not None:
        valid.append(v)
    if r is not None:
        valid.append(r)
    if i is not None:
        valid.append(i)

    if len(valid) != 2:
        return "Invalid values"
    else:
        if i == 0 or r == 0:
            return "Invalid values"

    if v is None:
        return round(i * r, 2)
    elif r is None:
        return round(v / i, 2)
    elif i is None:
        return round(v / r, 2)


print(ohm(v=10, r=5))
print(ohm(v=0, r=5))
print(ohm(v=10, r=0))
