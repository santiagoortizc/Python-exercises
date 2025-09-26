"""
/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */
"""

def draw_square(size):
  for i in range(size):
      print('*'*size)

def draw_triangle(height):
  for i in range(1, height+1):
    print(' *'*i)

def draw_rectangle(height, width):
  for i in range(height):
    print('*'*width)

figure = input("Ingrese la figura a dibujar Cuadrado (c), Triangulo (t) o Rectangulo (r): ").upper()

if figure == "C":
    size = int(input('Ingrese el tamano del lado( o altura para el rectangulo): '))        
    draw_square(size)
elif figure == "T":
    height = int(input("Ingresa la altura del triángulo: "))
    draw_triangle(height)
elif figure == "R":
    height = int(input("Ingresa la altura del rectángulo: "))
    width = int(input("Ingresa el ancho del rectángulo: "))
    draw_rectangle(height, width)
else:
      print("Figura no reconocida.")


