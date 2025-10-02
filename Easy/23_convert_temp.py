"""
Crea una función que transforme grados Celsius en Fahrenheit
y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°"
  y su unidad ("C" o "F").
- En caso contrario retornará un error.
"""


def convert_temp(temp: str) -> str:
    # 1. Validar que contenga "°"
    if "°" not in temp:
        return "Error: Wrong format"

    # 2. Encontrar posición de "°"
    índice = temp.index("°")

    # 3. Extraer número y unidad
    numero = temp[:índice]
    unidad = temp[índice+1:]

    # 4. Validar unidad
    if unidad not in ["C", "F"]:
        return "Error: Invalid unit temperature"

    # 5. Convertir número a float
    try:
        numero = float(numero)
    except ValueError:
        return "Invalid value"
        # 6. Aplicar fórmula según la unidad
    if unidad == "C":
        result = round((numero*9/5)+32, 2)
        return f"{temp} es igual a {result}°F"

    else:
        result = round((numero-32)*5/9, 2)
        return f"{temp} es igual a {result}°C"


print(convert_temp("25°C"))    # → "77.0°F" ✓
print(convert_temp("77°F"))    # → "25.0°C" ✓
print(convert_temp("0°C"))     # → "32.0°F" ✓
print(convert_temp("100°C"))   # → "212.0°F" ✓
# → "-40.0°F" ✓ (punto donde ambas escalas coinciden)
print(convert_temp("-40°C"))
print(convert_temp("25C"))     # → "Error: Wrong format" ✓
print(convert_temp("25°"))     # → "Error: Invalid unit temperature" ✓
print(convert_temp("25°K"))    # → "Error: Invalid unit temperature" ✓
print(convert_temp("abc°C"))   # → "Invalid value" ✓
