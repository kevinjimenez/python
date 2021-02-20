## docuemntacion de codigo es la especificacion
def suma(a, b):
    """Suma dos valores a,b

    param int a cualquier entero
    param int b cualquier entero
    return sumatoria de a y b
    """
    total = a + b
    return total

def a(cualquier_parametro):
    """Descripcion de lo que realiza la nuestra funcion

    cualquier_parametro int cualquier entero
    return cualquier_parametro + 5
    """
    return cualquier_parametro + 5

## nos permite ver la doc de la funcion con doc string
help(a)