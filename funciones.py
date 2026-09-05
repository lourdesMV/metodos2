import numpy as np

# Tamaño del fantoma
N = 8

# Fantoma original como matriz de 8 × 8
X_fantoma = np.array([
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.8, 0.3, 0.3, 0.3, 0.0, 0.0],
    [0.0, 0.8, 0.8, 0.8, 0.3, 0.3, 0.3, 0.0],
    [0.0, 0.3, 0.8, 0.3, 0.3, 0.3, 0.3, 0.0],
    [0.0, 0.3, 0.3, 0.3, 0.3, 0.5, 0.3, 0.0],
    [0.0, 0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.3, 0.3, 0.3, 0.5, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
], dtype=float)

# Fantoma vectorizado
xfantoma = X_fantoma.reshape(-1)

def mascara_rayo(n, direccion, s):
    """
    La función devuelve una imagen binaria que indica por dónde pasa un rayo
    """
    alpha, beta = direccion
    M = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            if alpha * i + beta * j == s:
                M[i, j] = 1

    return M


def matriz_proyeccion(n, direcciones):
    """
    la función construye la matriz de proyección para un conjunto de direcciones y devuelve también la información correspondiente a cada rayo.
    """
    filas_A = []
    rayos = []

    for alpha, beta in direcciones:
        valores_s = {
            alpha * i + beta * j
            for i in range(n)
            for j in range(n)
        }

        for s in sorted(valores_s):
            M = mascara_rayo(n, (alpha, beta), s)
            filas_A.append(M.flatten())
            rayos.append(((alpha, beta), s))

    A = np.array(filas_A, dtype=int)

    return A, rayos