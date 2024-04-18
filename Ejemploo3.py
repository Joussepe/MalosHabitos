def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo utilizando su base y altura."""
    area_rectangulo = base * altura
    return area_rectangulo

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo utilizando su base y altura."""
    area_triangulo = 0.5 * base * altura
    return area_triangulo

def principal():
    """Función principal que calcula y muestra el área de un rectángulo y un triángulo."""
    largo_rectangulo = 4
    ancho_rectangulo = 6
    area_rectangulo = calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    base_triangulo = 5
    altura_triangulo = 8
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

if __name__ == "__main__":
    principal()