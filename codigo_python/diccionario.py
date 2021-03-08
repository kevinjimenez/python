def run():
    ## estructura de llaves y valores
    ## para acceder a los valores se lo realiza mediante las llaves
    mi_diccionario = {
        'llave1': 112_23_344, ## para numero grandes se puede separar por guiones bajos
        'llave2': 2,
        'llave3': 3
    }
    # print(mi_diccionario['llave1'])

    poblacion_paises = {
        'Argentina': 112_23_344, ## para numero grandes se puede separar por guiones bajos
        'Brasil': 2232323,
        'Colombia': 312312312
    }

    # print(poblacion_paises['Argentina'])

    # for pais in poblacion_paises.keys(): ## keys imprime las llaves
    #     print(pais)

    # for pais in poblacion_paises.values(): ## values imprime los valores
    #     print(pais)

    # for pais in poblacion_paises.items(): ## items imprime las llaves y valores
    #     print(pais)
    #     # print(type(pais))

    for pais, poblacion in poblacion_paises.items(): ## items imprime las llaves y valores
        print(f'{pais} - {poblacion}')        
        # print(type(pais))
        # print(type(poblacion))



if __name__ == '__main__':
    run()