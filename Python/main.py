import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros del juego de la vida
N = 100  # Tamaño de la cuadrícula
generaciones = 100  # Número de generaciones para simular

# Función para inicializar la cuadrícula
def inicializar_tablero():
    tablero = np.random.randint(2, size=(N, N))
    return tablero

# Función para calcular el número de vecinos vivos
def vecinos_vivos(tablero, fila, columna):
    vecinos = 0
    for i in range(max(0, fila - 1), min(fila + 2, N)):
        for j in range(max(0, columna - 1), min(columna + 2, N)):
            if i == fila and j == columna:
                continue
            vecinos += tablero[i, j]
    return vecinos

# Función para actualizar la cuadrícula según las reglas del juego de la vida
def actualizar_tablero(tablero):
    nuevo_tablero = np.zeros_like(tablero)
    for fila in range(N):
        for columna in range(N):
            vecinos = vecinos_vivos(tablero, fila, columna)
            # Reglas del juego de la vida
            if tablero[fila, columna] == 1 and (vecinos < 2 or vecinos > 3):
                nuevo_tablero[fila, columna] = 0
            elif tablero[fila, columna] == 0 and vecinos == 3:
                nuevo_tablero[fila, columna] = 1
            else:
                nuevo_tablero[fila, columna] = tablero[fila, columna]
    return nuevo_tablero

# Función para animar el juego de la vida
def animar_juego(tablero):
    fig, ax = plt.subplots()
    img = ax.imshow(tablero, cmap='gray')

    def actualizar(frame):
        nonlocal tablero
        tablero = actualizar_tablero(tablero)
        img.set_array(tablero)
        return img,

    ani = animation.FuncAnimation(fig, actualizar, frames=generaciones, interval=100, blit=True)
    plt.show()

# Inicializar la cuadrícula
tablero = inicializar_tablero()

# Animar el juego de la vida
animar_juego(tablero)