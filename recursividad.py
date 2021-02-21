# factorial recursividad

def factorial(n):
    """Calcula en factorial de n

    n int > 0
    return n!
    """
    print(n)
    if n == 1:
        return 1
        
    return n * factorial(n - 1)

n = int(input('Escriba un entero: '))
print(factorial(n))