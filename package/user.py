from .auto import Auto

class User:
    def __init__(self, option: int, time_standing: int, car: Auto):
        '''
        El usuario recibe por parametros
        option: La opcion de tiempo que desea dejar su automovil en el parqueadero
        time_standing: Por cuanto tiempo lo piensa dejar
        car: El automovil que va a dejar
        '''
        self.option = option
        self.time_standing = time_standing
        self.type_car = car.type_car

