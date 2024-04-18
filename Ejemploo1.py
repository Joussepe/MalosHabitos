# Definición de variables con nombres más descriptivos
valor_x = 10
valor_y = 5

# Cálculo de la suma de valor_x y valor_y
suma_xy = valor_x + valor_y

# Definición de la función para calcular el producto
def calcular_producto(factor_1, factor_2):
    """Esta función toma dos números y devuelve su producto."""
    producto = factor_1 * factor_2
    return producto

# Llamada a la función para calcular el producto con los valores de valor_x y suma_xy
resultado = calcular_producto(valor_x, suma_xy)

# Impresión del resultado con un mensaje más descriptivo
print("El resultado del producto es:", resultado)
