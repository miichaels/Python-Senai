from abc import ABC, abstractclassmethod

class Filmes(ABC):
    nome = None
    base = None


    @abstractclassmethod
    def r_diaria(self):
        pass