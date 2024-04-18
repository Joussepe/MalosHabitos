def calcular_resultado(a, b, c):
    """Esta función calcula un resultado utilizando la fórmula: a * b + c."""
    resultado = a * b + c
    return resultado

def ejecutar_calculo():
    """Esta función principal ejecuta el cálculo utilizando valores específicos para a, b y c."""
    a = 5
    b = 3
    c = 7
    resultado = calcular_resultado(a, b, c)
    print("El resultado del cálculo es:", resultado)

ejecutar_calculo()