import numpy as np

# Función para calcular la distancia total de una ruta


def calcular_distancia(ruta, distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancias[ruta[i]][ruta[i+1]]
    distancia_total += distancias[ruta[-1]][ruta[0]]  # Regresar al inicio
    return distancia_total

# Función para generar un vecino


def generar_vecino(ruta):
    # Escoger dos ciudades al azar
    i, j = np.random.choice(len(ruta), 2, replace=False)
    vecino = ruta.copy()
    # Intercambiar las dos ciudades
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino

# Función de búsqueda local


def busqueda_local(distancias):
    num_ciudades = len(distancias)
    ruta_actual = list(range(num_ciudades))  # Ruta inicial (0, 1, 2, ..., n-1)
    mejor_distancia = calcular_distancia(ruta_actual, distancias)

    while True:
        for i in range(100):  # Generar 100 vecinos
            vecino = generar_vecino(ruta_actual)
            distancia_vecino = calcular_distancia(vecino, distancias)
            if distancia_vecino < mejor_distancia:  # Si el vecino es mejor, actualizar la ruta actual
                ruta_actual, mejor_distancia = vecino, distancia_vecino
                break
        else:  # Si ninguno de los vecinos es mejor, terminar
            break

    return ruta_actual, mejor_distancia


# Matriz de distancias (por ejemplo, distancias euclidianas entre ciudades)
distancias = np.random.rand(10, 10)
distancias = (distancias + distancias.T) / 2  # La matriz debe ser simétrica

print(distancias)

ruta, distancia = busqueda_local(distancias)
print(
    f"La mejor ruta encontrada es {ruta} con una distancia total de {distancia}")
