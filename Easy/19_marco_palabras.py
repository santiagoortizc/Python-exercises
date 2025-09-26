"""
Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
- ¿Qué te parece el reto? Se vería así:
  **********
  * ¿Qué   *
  * te     *
  * parece *
  * el     *
  * reto?  *
  **********
"""


def marco(phrase: str) -> str:
    words = phrase.split()
    longest = max(len(w) for w in words)
    result = []
    result.append("*"*(longest+4))
    for i in words:
        # ljust() justifica el texto de acuerdo a un acho
        result.append(f"* {i.ljust(longest)} *")
    result.append("*"*(longest+4))
    return "\n".join(result)


print(marco("¿Qué te parece el reto?"))
print(marco("Santiago Ortiz Carvajal"))
print(marco("Parangaricutirimucaro"))
