"""
Crea una función que imprima los 30 próximos años bisiestos
siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.
"""


def leap_year(year: int):
    cont, x = 0, year+1
    while cont < 30:
        if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
            print(x)
            cont += 1
        x += 1


leap_year(2000)
