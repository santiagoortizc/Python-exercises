'''
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def invertir_cadena(cadena):
    invertida = ''
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

print(invertir_cadena('Hola mundo')) 
print(invertir_cadena('Santiago')) 
print(invertir_cadena('Python')) 
print(invertir_cadena('Invertir')) 
print(invertir_cadena('Cadena')) 
