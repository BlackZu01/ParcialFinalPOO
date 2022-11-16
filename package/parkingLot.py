# Parking Lot excercise
from __future__ import annotations
from .options import Options
from .user import User
from .bill import Bill
import numpy as np

class ParkingLot(Options, User):
    def __init__(self):
        '''
        ParkingLot simula el parqueadero y el parqueadero lo definiremos como un diccionario cuyas keys serian el tipo de auto
        y los values la cantidad de espacios disponibles que tiene

        las variables que empiezan por pos_ es para definir los indices de las posiciones de cada uno de los espacios disponibles
        por tipo de auto
        '''
        self.parking = dict()
        self.time = 0
        self.pos_c, self.pos_s, self.pos_v = (0, 0, 0)
        self.pos_cf, self.pos_sf, self.pos_vf = (0, 0, 0)

    def time_stand(self, user: User, option: int):
        '''
        Tranforma en minutos el tiempo ingresado por el usuario
        '''
        self.user = user
        if option == 1:
            self.time = self.user.time_standing * 1440
        if option == 2:
            self.time = self.user.time_standing * 60
        if option == 3:
            self.time = self.user.time_standing
        return self.time

    def check_bill(self, user: User):
        '''
        Devuelve el precio total a pagar
        '''
        self.user = user
        self.charge_b = Bill(self.user.type_car.lower())
        self.initial_bill = self.charge_b.charge_bill
        return f'$ {str(self.time_stand(self.user, self.user.option) * self.initial_bill)}'

    def generateMatrix(self):
        '''
        Genera una matriz de 9 espacios para los espacios del parqueadero
        '''
        return np.zeros((3, 3), dtype = int)

    def generateParking(self):
        '''
        Genera nuestro parqueadero como se indico anteriormente en Options
        '''
        self.parking['Compact'] = self.generateMatrix()
        self.parking['SUV'] = self.generateMatrix()
        self.parking['Van'] = self.generateMatrix()
    
    def process(self, pos: int, pos_f: int):
        '''
        Incrementa los indices de las posiciones de la matriz donde se guardaran los espacios disponibles y ocupados
        '''
        self.pos_c += 1
        if pos == self.generateMatrix().shape[0]:
            pos = 0
            pos_f += 1
            if pos_f == self.generateMatrix().shape[1]:
                return 

    def assignParking(self, user: User, register: bool):
        '''
        Asigna el espacio disponible al usuario dependiendo del tipo de auto
        1 en caso tal de asignarlo sin haber hecho reserva
        5 en caso tal de que el usuario este reservando para el dia siguiente llevar el auto y dejarlo por el tiempo que especifico
        '''
        self.user = user
        try:
            if self.user.type_car.lower() == 'compact':
                if register == True:
                    self.parking['Compact'][self.pos_cf][self.pos_c] = 5
                else:
                    self.parking['Compact'][self.pos_cf][self.pos_c] = 1
                self.process(self.pos_c, self.pos_cf)
            if self.user.type_car.lower() == 'suv':
                if register == True:
                    self.parking['SUV'][self.pos_sf][self.pos_s] = 5
                else:
                    self.parking['SUV'][self.pos_sf][self.pos_s] = 1
                self.process(self.pos_s, self.pos_sf)
            if self.user.type_car.lower() == 'van':
                if register == True:    
                    self.parking['Van'][self.pos_vf][self.pos_v] = 5
                else:
                    self.parking['Van'][self.pos_vf][self.pos_v] = 1
                self.process(self.pos_v, self.pos_vf)
        except IndexError:
            print('There\'re no spaces available at the moment')


    def keepTracks(self):
        '''
        Muestra el número de espacios disponibles para cada tipo de auto
        '''
        print('Places availables for Compact cars {}'.format(9 - np.count_nonzero(self.parking['Compact'])))
        print('Places availables for SUV cars {}'.format(9 - np.count_nonzero(self.parking['SUV'])))
        print('Places availables for Van cars {}'.format(9 - np.count_nonzero(self.parking['Van'])))

    def showPark(self, matrix):
        ''''
        Muestra de manera bonita el parqueadero
        '''
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                print(matrix[i][j], end= '  ')
            print(' ')

    def showParkingLot(self):
        ''''
        Muestra el parqueadero visualmente mejor con ayuda del metodo showPark()
        '''
        print('\n\t[+] Parking places [+] \n')
        for key, value in self.parking.items():
            print(f'{key}:')
            self.showPark(self.parking[key])

