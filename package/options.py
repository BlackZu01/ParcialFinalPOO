from abc import ABC, abstractmethod
from .user import User

class Options(ABC):
    ''''
    Esta clase abstracta lo que va a realizar es definir 3 metodos abstractos que seran muy importantes en la clase principal
    '''
    @abstractmethod
    def time_stand(self, user: User, option: int):
        ''''
        transforma en minutos el tiempo ingresado por el usuario
        '''
        ...
    @abstractmethod
    def check_bill(self, user: User):
        ''''
        Retorna el cheque total que tiene que cancelar el usuario
        '''
        ...
    @abstractmethod
    def generateParking(self):
        ''''
        Genera al parqueadero
        '''
        ...