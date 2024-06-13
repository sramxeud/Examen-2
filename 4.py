import numpy as np
import math

# Definimos la función


def f(x):
    return x**2 - 10*x + 25

# Definimos una función para generar un vecino


def generar_vecino(x):
    return x + np.random.uniform(-1, 1)

# Definimos la función de recocido simulado


def recocido_simulado(temperatura_inicial, tasa_enfriamiento):
    # Inicializamos x de manera aleatoria
    x_actual = np.random.uniform(-10, 10)
    mejor_x, mejor_y = x_actual, f(x_actual)

    temperatura = temperatura_inicial
    # Condición de terminación (temperatura cercana a cero)
    while temperatura > 0.01:
        vecino = generar_vecino(x_actual)
        y_vecino = f(vecino)
        if y_vecino < mejor_y:  # Si el vecino es mejor, actualizar el mejor x
            mejor_x, mejor_y = vecino, y_vecino
        # Si el vecino es peor, aún podría ser aceptado con cierta probabilidad
        elif np.random.rand() < math.exp((f(x_actual) - y_vecino) / temperatura):
            x_actual = vecino
        temperatura *= tasa_enfriamiento  # Enfriar la temperatura

    return mejor_x, mejor_y


x, y = recocido_simulado(temperatura_inicial=1000, tasa_enfriamiento=0.995)
print(f"El mínimo encontrado es en x = {x} con un valor de y = {y}")
