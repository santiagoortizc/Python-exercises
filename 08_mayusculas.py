'''
 Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

#def capitalizar(cadena) :
#  cadena = cadena.split()
#  for i in range(len(cadena)):
#    cadena[i] = cadena[i].capitalize()
#  return ' '.join(cadena)
#
#def capitalizar(cadena):
#    palabras = cadena.split()
#    resultado = []
#    for palabra in palabras:
#        if len(palabra) > 0:
#            mayus = palabra[0].upper() + palabra[1:]
#            resultado.append(mayus)
#    return ' '.join(resultado)
#
#print(capitalizar('hola mundo'))  

def capitalizar_palabras(texto):
  """
  Función que recibe un string y convierte la primera letra de cada palabra a mayúscula.
  No utiliza métodos built-in como title() o capitalize() para conversión general,
  pero usa upper()/lower() para casos especiales del español (acentos, ñ, etc.).

  Args:
      texto (str): El string a procesar

  Returns:
      str: El string con la primera letra de cada palabra en mayúscula
  """
  if not texto:
    return texto

  resultado = ""
  nueva_palabra = True

  for caracter in texto:
    # Si es un espacio o símbolo de puntuación, la siguiente letra será inicio de palabra
    if caracter == ' ' or not caracter.isalnum():
      resultado += caracter
      nueva_palabra = True
    else:
      # Si es el inicio de una nueva palabra y es una letra
      if nueva_palabra and caracter.isalpha():
        # Convertir a mayúscula manualmente usando códigos ASCII
        if 'a' <= caracter <= 'z':
          resultado += chr(ord(caracter) - 32)  # Convertir a mayúscula
        # Caso especial para caracteres del español (acentos, ñ, etc.)
        elif caracter.islower():
          resultado += caracter.upper()  # Función built-in para casos especiales
        else:
          resultado += caracter
        nueva_palabra = False
      else:
        # Convertir a minúscula manualmente usando códigos ASCII
        if 'A' <= caracter <= 'Z':
          resultado += chr(ord(caracter) + 32)  # Convertir a minúscula
        # Caso especial para caracteres del español (acentos, ñ, etc.)
        elif caracter.isupper():
          resultado += caracter.lower()  # Función built-in para casos especiales
        else:
          resultado += caracter

  return resultado 


# Función de prueba
def pruebas():
  """Función para probar la funcionalidad"""
  casos_prueba = [
    "hola mundo",
    "esto es una PRUEBA",
    "   espacios   al   inicio   y   final   ",
    "123 números y letras",
    "símbolos!@# y puntuación.",
    "múltiples    espacios",
    "",
    "a",
    "MAYÚSCULAS",
    "CamelCase y PascalCase",
    "niño pequeño",
    "NIÑO PEQUEÑO",
    "josé maría",
    "JOSÉ MARÍA",
    "años pasión corazón",
    "AÑOS PASIÓN CORAZÓN"
  ]
    
  print("Pruebas de la función capitalizar_palabras:")
  print("-" * 50)
    
  for caso in casos_prueba:
    resultado = capitalizar_palabras(caso)
    print(f"Entrada:   '{caso}'")
    print(f"Resultado: '{resultado}'")
    print()

# Ejecutar las pruebas
if __name__ == "__main__":
  pruebas()