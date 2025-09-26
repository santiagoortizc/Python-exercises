"""
Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""
def area_poligono(poligono):
    if poligono["tipo"] == "triangulo":
        return (poligono["base"] * poligono["altura"]) / 2
    elif poligono["tipo"] == "cuadrado":
        return poligono["lado"] ** 2
    elif poligono["tipo"] == "rectangulo":
        return poligono["base"] * poligono["altura"]
    else:
        return "Tipo de polígono no soportado"

# Ejemplos de uso
triangulo = {"tipo": "triangulo", "base": 3, "altura": 5}
rectangulo = {"tipo": "rectangulo", "base": 6, "altura": 7}
cuadrado = {"tipo": "cuadrado", "lado": 8}
pentagono = {"tipo": "pentagono", "lado": 8}

print(f"Área del triángulo: {area_poligono(triangulo)}")
print(f"Área del rectángulo: {area_poligono(rectangulo)}")
print(f"Área del cuadrado: {area_poligono(cuadrado)}")
print(f"Área del pentagono: {area_poligono(pentagono)}")