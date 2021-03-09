class Lavadora:


    def __init__(self):
        pass


    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()


    def _llenar_tanque_agua(self, temperatura):
        print(f'llenado el tanque con agua en la temperatura {temperatura}')
    

    def _anadir_jabon(self):
        print(f'AÑADIR JABON')

    def _lavar(self):
        print(f'Lavar')

    def _centrifugar(self):
        print(f'Centrifujar')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()