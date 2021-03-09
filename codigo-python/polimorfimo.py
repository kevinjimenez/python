class Persona:


    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('ando caminando')


class Ciclista(Persona):


    def __init__(self, nombre):
        super().__init__(nombre)

    
    def avanza(self):
        print('ando moviendome en bici')

def main():
    persona = Persona('kevin')
    persona.avanza()

    ciclista = Ciclista('alisson')
    ciclista.avanza()


if __name__ == '__main__':
    main()