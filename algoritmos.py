import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    x = (x_2 - x_1) **2
    y = (y_2 - y_1) **2
    distancia = math.sqrt(x + y)
    return distancia
