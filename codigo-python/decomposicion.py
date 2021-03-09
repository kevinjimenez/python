class Automovil:


    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo' 
        self._motor = Motor(4) #None ## None => no tiene valor, similar a un null


    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(30)
            self._estado = 'rapidisimo'
        else:
            self._motor.inyecta_gasolina(10)
            self._estado = 'fresh !'


class Motor:


    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0


    def inyecta_gasolina(self, cantidad):
        pass