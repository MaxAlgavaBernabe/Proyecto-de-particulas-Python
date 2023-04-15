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


lista = ListaParticulas()
particula1 = Particula(1, 2, 2, 4, 4, 10, 3, 2, 1)
particula2 = Particula(2, 2, 2, 4, 4, 50, 5, 6, 2)
lista.agregarInicio(particula1)
lista.agregarFinal(particula2)
lista.mostrar()
