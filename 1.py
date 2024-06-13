from sklearn import datasets
import numpy as np

# Definimos la función de activación (usaremos la función sigmoide)


def sigmoide(x):
    # np.exp calcula el exponente de e
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide


def derivada_sigmoide(x):
    return x * (1 - x)


# Inicializamos los pesos de manera aleatoria
pesos = np.zeros((4, 1))
# pesos = 2 * np.random.random((4, 1)) - 1

# Tasa de aprendizaje
tasa_aprendizaje = 0.4

# Cargamos el dataset iris
iris = datasets.load_iris()

# Imprimir datos
# print(iris.data[:5])

X = iris.data[:, :4]  # tomamos solo las primeras 4 características
y = iris.target.reshape(-1, 1)  # convertimos a un vector columna

# Normalizamos los datos
X = X / np.amax(X, axis=0)
y = y / np.amax(y, axis=0)

# Entrenamos la red neuronal
epocas = 0
for i in range(40000):
    # Propagación hacia adelante
    capa_entrada = X
    salidas = sigmoide(np.dot(capa_entrada, pesos))

    # Cálculo del error
    error = y - salidas

    # Propagación hacia atrás (ajuste de los pesos)
    ajustes = error * derivada_sigmoide(salidas)
    pesos += np.dot(capa_entrada.T, ajustes)

    # Contamos las épocas
    epocas += 1

    # Podemos agregar una condición de parada temprana si el error es lo suficientemente pequeño
    if np.mean(error**2) < 0.02:
        break

print(f"La red neuronal requirió {epocas} épocas para entrenarse.")
