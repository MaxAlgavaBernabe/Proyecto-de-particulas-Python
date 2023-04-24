from particula  import Particula
import json

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
    
        