from particula  import Particula
from algoritmos import distancia_euclidiana

class ListaParticulas:
    def __init__(self):
        self.__particulas = []

    def agregarInicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregarFinal(self, particula: Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    def __str__(self):
       
        return '\n'.join(str(particula) for particula in self.__particulas)


