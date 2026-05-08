from abc import ABC, abstractmethod

class Sala(ABC):
    def __init__(self):
        self._id: int

class Sala_Individual(Sala):
    pass

class Sala_Grupo(Sala):
    pass

class Sala_Laboratorio(Sala):
    pass