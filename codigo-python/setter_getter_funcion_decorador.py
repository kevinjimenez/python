def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper()

def zumbido():
	print("Buzzzzzz")

## sin el simbolo del decorador '@'
zumbido = funcion_decoradora(zumbido)

## usando el simbolo del decorador '@'
@funcion_decoradora
def zumbido2():
	print("Buzzzzzz")

### SETTER AND GETTER

#### Clase sin getter and setter
class Millas:


    def __init__(self, distancia = 0):
        self.distancia = distancia
    

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

avion = Millas()
avion.distancia = 200
print(avion.convertir_a_kilometros())



#### Clase con getter and setter
class Millas_2:


    def __init__(self, distancia = 0):
        self._distancia = distancia
    

    def convertir_a_kilometros(self):
        return (self._distancia * 1.609344)

    
    ## Metodo getter
    def obtener_distancia(self):
        return self._distancia

    ## Metodo getter
    def definir_distancia(self, distancia):
        if distancia < 0:
            raise ValueError('No es posible convertir distancias menores a 0.')
        self._distancia = distancia

avion = Millas_2()
avion.definir_distancia(120)
print(avion.convertir_a_kilometros())

## Funcion property

class Millas_3:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# Función para eliminar el atributo _distancia
	def eliminar_distancia(self):
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto 
avion = Millas_3()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
## print(avion.distancia)
# Llamada al método getter
# Llamada al método setter
# 200

## Funcion property con decorador '@'

class Millas_4:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto 
avion = Millas_4()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
print(avion.distancia)
# Llamada al método getter
# Llamada al método setter
# 200


