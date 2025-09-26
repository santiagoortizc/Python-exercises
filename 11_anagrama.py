
"""
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word1, word2):
  """
  Retorna verdadero o falso (bool) según sean o no anagramas.
  """
  
  if word1.lower() == word2.lower():
    return False  
      
  return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("Anagrama","Anagrama"))
print(is_anagram("aMoR","rOmA"))
print(is_anagram("cAmiLO","SanTIago"))



palabras_prueba = [
    ("restino", "soterrin"),  
    ("riesgo", "griose"),       
    ("saco", "cosa"),         
    ("ramo", "mora"),         
    ("nube", "buen"),         
    ("fila", "fali"),         
    ("Anagrama","Anagrama"),
    ("aMoR","rOmA"),
    ("cAmiLO","SanTIago")       
]

print("\nResultados del juego:")
for palabra1, palabra2 in palabras_prueba:
    resultado = is_anagram(palabra1, palabra2)
    print(f"'{palabra1}' y '{palabra2}': {resultado}")