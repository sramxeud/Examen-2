import numpy as np
import random

# Definimos la matriz de adyacencia
graph = np.array([
    [0, 7, 9, 8, 20],
    [7, 0, 10, 4, 11],
    [9, 10, 0, 15, 5],
    [8, 4, 15, 0, 17],
    [20, 11, 5, 17, 0]
])

# Función para calcular la distancia total de una ruta


def calcular_distancia(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        # graph[ruta[i]][ruta[i+1]] distancia entre los nodos de un grafo
        distancia_total += graph[ruta[i]][ruta[i+1]]
    # Regresar al inicio #ruta[-1] accede al último elemento de una lista
    distancia_total += graph[ruta[-1]][ruta[0]]
    return distancia_total

# Función para generar una población inicial


def generar_poblacion(tamaño_poblacion):
    # genera [0,4,1,2,3] o [0,3,4,2,1] o etc
    # _ variable
    return [[0] + random.sample(range(1, 5), 4) for _ in range(tamaño_poblacion)]


# Función para seleccionar los padres para la reproducción
def seleccionar_padres(poblacion):
    # Calculamos la aptitud de cada individuo (la distancia total de la ruta)
    aptitudes = [calcular_distancia(individuo) for individuo in poblacion]
    # ramdom.choices Seleccionamos dos padres de manera proporcional a su aptitud (los individuos con menor distancia tienen mayor probabilidad)
    padres = random.choices(poblacion, weights=aptitudes, k=2)
    return padres

# Función para realizar el cruce


def cruce(padre1, padre2):
    # Seleccionamos un punto de cruce al azar
    punto_cruce = random.randint(1, len(padre1) - 1)
    # Creamos los hijos intercambiando las partes de los padres después del punto de cruce
    hijo1 = padre1[:punto_cruce] + \
        [gen for gen in padre2 if gen not in padre1[:punto_cruce]]
    hijo2 = padre2[:punto_cruce] + \
        [gen for gen in padre1 if gen not in padre2[:punto_cruce]]
    return hijo1, hijo2

# Función para realizar la mutación


def mutacion(individuo):
    # Intercambiamos dos genes al azar
    i, j = random.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]

# Función para ejecutar el algoritmo genético


def algoritmo_genetico(tamaño_poblacion, generaciones):
    # Generamos la población inicial
    poblacion = generar_poblacion(tamaño_poblacion)

    for _ in range(generaciones):
        # Seleccionamos los padres y realizamos el cruce
        padre1, padre2 = seleccionar_padres(poblacion)
        hijo1, hijo2 = cruce(padre1, padre2)

        # Realizamos la mutación con una pequeña probabilidad
        if random.random() < 0.1:
            mutacion(hijo1)
        if random.random() < 0.1:
            mutacion(hijo2)

        # Añadimos los hijos a la población
        poblacion += [hijo1, hijo2]

        # Eliminamos los dos individuos menos aptos
        poblacion.sort(key=calcular_distancia)
        poblacion = poblacion[:tamaño_poblacion]

    # Devolvemos el individuo más apto de la población final
    return poblacion[0]


# Ejecutamos el algoritmo genético
mejor_ruta = algoritmo_genetico(100, 100)
print(
    f"La mejor ruta encontrada es {mejor_ruta} con una distancia total de {calcular_distancia(mejor_ruta)}")
