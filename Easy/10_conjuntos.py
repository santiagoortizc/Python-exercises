'''
Crea una función que reciba dos array, un booleano y retorne un array.
 - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

'''

def common(array1, array2, boolean=True):
  """
  - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
  - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
  """
  common = []
  not_common = []
  
  for i in array1:
    
    if i in array2:
      common.append(i)
    else:
      not_common.append(i)  

  for i in array2:
    if i not in array1:
      not_common.append(i)  
  
  if boolean:
    return f'Elemento comunes: {common}'
  else:
    return f'Elemento No comunes: {not_common}'
  
print(common([8,'d',1,'e',5,'a',3,'b'], ['b',0,'f',8,'d',6,'c',1], True))
print(common([8,'d',1,'e',5,'a',3,'b'], ['b',0,'f',8,'d',6,'c',1], False))

