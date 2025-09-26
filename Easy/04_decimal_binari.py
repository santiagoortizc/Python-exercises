'''
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def decimal_binari(decm):
  binari = ""
  
  if decm == 0:
    return 0
  elif decm == 1:
    return 1
  else:
    while decm > 1:
      residuo = decm % 2
      binari = str(residuo) + binari
      decm = decm // 2
  
  return f"1{binari}"

for i in range(21):
  print(decimal_binari(i)," ", i)
