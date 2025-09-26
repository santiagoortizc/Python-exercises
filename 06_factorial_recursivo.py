'''
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva
'''

def factorial(num):
  
  if num == 0 or num == 1:
    return 1
  
  return num * factorial(num - 1)
  
print(factorial(6))
print(factorial(9))
print(factorial(11))
print(factorial(31))
print(factorial(2))