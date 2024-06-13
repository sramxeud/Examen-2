from sklearn import datasets
import numpy as np

# Definimos la función de activación (usaremos la función escalón)


def funcion_escalon(x):
    return np.where(x >= 0, 1, 0)

# Derivada de la función escalón


def derivada_funcion_escalon(x):
    return np.where(x != 0, 0, 0)


# Inicializamos los pesos de manera aleatoria
pesos1 = 2 * np.random.random((4, 4)) - 1
pesos2 = 2 * np.random.random((4, 1)) - 1

# Tasa de aprendizaje
tasa_aprendizaje = 0.2

# Cargamos el dataset iris
iris = datasets.load_iris()
X = iris.data[:, :4]  # tomamos solo las primeras 4 características
y = iris.target.reshape(-1, 1)  # convertimos a un vector columna

# Normalizamos los datos
X = X / np.amax(X, axis=0)
y = y / np.amax(y, axis=0)

# Entrenamos la red neuronal
epocas = 0
for i in range(20000):  # puedes ajustar el número de iteraciones
    # Propagación hacia adelante
    capa_entrada = X
    capa_oculta = funcion_escalon(np.dot(capa_entrada, pesos1))
    salidas = funcion_escalon(np.dot(capa_oculta, pesos2))

    # Cálculo del error
    error = y - salidas

    # Propagación hacia atrás (ajuste de los pesos)
    ajustes1 = error * derivada_funcion_escalon(salidas)
    pesos2 += np.dot(capa_oculta.T, ajustes1)
    ajustes2 = np.dot(ajustes1, pesos2.T) * \
        derivada_funcion_escalon(capa_oculta)
    pesos1 += np.dot(capa_entrada.T, ajustes2)

    # Contamos las épocas
    epocas += 1

    # Podemos agregar una condición de parada temprana si el error es lo suficientemente pequeño
    if np.mean(error**2) < 0.01:
        break

print(f"La red neuronal requirió {epocas} épocas para entrenarse.")
