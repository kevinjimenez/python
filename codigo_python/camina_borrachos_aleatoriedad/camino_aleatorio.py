from borracho import Borracho_Tradiccional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_intentos, tipo_de_borracho): ## tipo borracho es una funcion
    borracho = tipo_de_borracho(nombre='kevin') ## anostica
    origen = Coordenada(0,0)
    distancias = []

    ## _ significa q no se va usar la variable, si no solo realiza un recorrido de rango
    for _ in range(numero_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(tittle='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x,y, legend='distancia media')
    show(grafica)

def main(distancias_de_caminata, numero_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_de_borracho) 
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        ## tipo_de_borracho.__name__ => nos da el noombre de la clase
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    
    graficar(distancias_de_caminata, distancias_media_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata = [10,100,1000,10000]
    numero_intentos = 100
    
    main(distancias_de_caminata, numero_intentos, Borracho_Tradiccional) 
    ## param1, params2, recibe una clase
