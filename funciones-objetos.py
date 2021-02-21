## Argumentos de otras funciones

def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, nums):
    resultados = []
    for numero in nums:
        resultado = f(numero)
        resultados.append(resultado)
    print(resultados)

nums = [1,2,3]
aplicar_operacion(multiplicar_por_dos, nums)
aplicar_operacion(sumar_dos, nums)

## Funciones en expresiones     
## (LAMBDA) => lambda <vars>: <expresion>

sumar = lambda x, y: x + y
print(sumar(3,4))

## Funciones en estructuras de datos

def aplicar_operacion2(num):
    operaciones = [abs, float]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    return resultado

print(aplicar_operacion2(-2))