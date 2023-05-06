from particula  import Particula
import json
from algoritmos import *

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

    def sort_id(self):
       self.__particulas.sort(key=lambda particula: particula.id)
    def sort_distancia(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)
    def sort_velocidad(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)
    def __str__(self):
       
        return '\n'.join(str(particula) for particula in self.__particulas)

    def puntos_cercanos(self):
        puntos = []
        for p in self.__particulas:
        #Pasar a lista de tuplas para el algoritmo y agregar los colores
            p1 = (p.origen_x,p.origen_y,p.red,p.green,p.blue)
            p2 = (p.destino_x,p.destino_y,p.red,p.green,p.blue)
            puntos.append(p1)
            puntos.append(p2)
        res = puntos_mas_cercanos(puntos)
        return res
    def __len__(self):
        return(
            len(self.__particulas)
        )
    def __iter__(self):
        self.count=0
        return self
    def __next__ (self):
        if self.count < len(self.__particulas):
            conjunto=self.__particulas[self.count]
            self.count += 1
            return conjunto
        else:
            raise StopIteration
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
                return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
            
        except:
            return 0
    
        