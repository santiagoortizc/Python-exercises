'''
Crea una función que reciba dos cadenas como parámetro (str1, str2)
  e imprima otras dos cadenas como salida (out1, out2).
  - out1 contendrá todos los caracteres presentes en la str1 pero NO
    estén presentes en str2.
  - out2 contendrá todos los caracteres presentes en la str2 pero NO
    estén presentes en str1.
'''

def delete_charac(str1, str2):
  
  str1 = str1.lower()
  str2 = str2.lower()
  out1 = ''
  out2 = ''
  
  for i in str1:
    if i not in str2:
      out1 = out1 + i 

  for i in str2:
    if i not in str1:
      out2 = out2 +i  

  print(out1.upper())
  print(out2.upper())
  
delete_charac('SaNtIaGo', 'cAmIlO')
