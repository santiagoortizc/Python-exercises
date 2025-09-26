"""
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
"""

for i in range(1, 101):
  print(i)
  
  
n=1
while n <=100:
  print(n)
  n+=1


# El * toma cada número de esa lista y lo pasa individualmente a la función print() como si fueran argumentos separados
print(*[i for i in range(1, 101)], sep="\n")
