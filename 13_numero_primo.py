"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

from math import sqrt

def is_prime(num):
  
  if num < 2: #0 y 1 no son primos
    return False
  
  for i in range(2, int( 1 + sqrt(num) )): #sqrt(num) es la raiz cuadrada de num
    if num % i == 0:
      return False #si el numero es divisible por i, no es primo
  return True

for i in range(1,101):
  if is_prime(i):
    print(i)  