class Bill:
    def __init__(self, type_auto: str):
        '''
        [+] La clase que simula la factura
        type_auto: tipo de auto del usuario
        '''
        self.type_car = type_auto
    
    @property
    def charge_bill(self):
        ''''
        Cuanto dinero cobrabra dependiendo del tipo de auto
        $ 1 si es compact
        $ 2 si es suv
        $ 3 si es van
        '''
        if self.type_car == 'compact':
            return 1
        if self.type_car == 'suv':
            return 2
        if self.type_car== 'van':
            return 3