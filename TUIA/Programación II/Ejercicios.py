# Ejercicio 1 y 2
"""
    1. Escriba una función recursiva repite_hola que reciba como parámetro un número entero n y
escriba por pantalla n veces el mensaje "Hola". Invóquela con distintos valores de n.
    2. Escriba otra función repite_hola que reciba como parámetro un número entero n y devuelva la
cadena formada por n concatenaciones de "Hola". Invóquela con distintos valores de n.
"""

""" A)
def repite_hola(n: int, msj: str) -> str :
    if n == 0 or n < 0: #Caso Base
        return 0
    print(msj + ' ') # Caso recursivo
    return repite_hola(n-1, msj) #En la llamada a la función tenemos la convergencia a base

repite_hola(1, "hola")
"""
""" B)
def repite_saludo(n: int, msj: str) -> str :
    if n == 0 or n < 0: #Caso Base
        return msj
    msj += " " + msj # Caso recursivo
    return repite_saludo(n-1, msj) #En la llamada a la función tenemos la convergencia a base

print(repite_saludo(3, "hola"))

"""

# Ejercicio 3
"""
    1. Piense cuál sería el resultado de la expresión misterio(5) y luego compruebe su hipótesis
ejecutándola.
    2. Explique con sus palabras qué hace misterio(a) para cualquier a, sea positivo, negativo o 0.


def misterio(a: int) -> int:
    if a == 0:
        return a
    return 1 + misterio(a - 1)

print(misterio(5))

    # Si es positivo devuelve el número, si es 0 también y si es negativo se rompe
    # por nunca converger en un caso base

"""

# Ejercicio 4
""" Considere la siguiente función recursiva:

def f(n: int, d: int) -> None:
    if n > 1:
        if n % d == 0:
            print(d)
            f(n//d, d)
        else:
            f(n, d + 1)

f(30,2)

    # 1. ¿Qué muestra por pantalla la llamada f(30, 2)? Intente deducirlo sin ejecutar el código.
    # 2. A nivel general, ¿qué muestra por pantalla la llamada f(x, 2) para un x cualquiera?
    # 3. Implemente una función iterativa equivalente.
    # 1. La función devuelve todos los divisores enteros del primer número, comenzando por el segundo
    # 3.

def f(n: int, d: int) -> None:
    for i in range(n):
        if n % d == 0:
            print(d)
            n = n // d
        else:
            d += 1

f(30,2)
"""

# Ejercicio 5
""" #Considere el siguiente código: 

def mystery(a: int, b: int) -> int:
    if (b == 0):
        return a
    return mystery(2 * a, b - 1)


result = mystery(7, 3)
print(result)


1. ¿Qué muestra por pantalla este código? Intente deducirlo sin ejecutar el código.
2. ¿Cuántas veces se llama recursivamente mystery en este código?
3. A nivel general, ¿qué muestra por pantalla la llamada f(x, 3) para un x cualquiera? ¿Qué
muestra por pantalla la llamada f(x, y) para x, y cualesquiera?

1. Este código muestra en pantalla el resultado de múltiplicar y veces al primer número y sus sucesivas duplas
"""

# Ejercicio 6
""" 
Escriba una función recursiva que tome un numero natural n e imprima todos los números desde n
hasta 1.
"""
"""
def naturales(n: int) -> str :
    if n == 1:
        print(n)
        return 0
    else:
        print(n)
        return naturales (n-1)
    
naturales(3)
"""



# Ejercicio 7
"""
Convierta la siguiente función recursiva a una iterativa :

def recursiva(t: int, k: int) -> int:
    if t >= 100:
        return k
    else:
        return recursiva(t + k, k + 1)

print(recursiva(5,2))


def iterativa(t: int, k: int) -> int:
    while t < 100 :
        t += k
        k += 1
    return k


print(iterativa(5,2))

"""

# Ejercicio 8
"""
Escriba una función recursiva que calcule el n-ésimo número triangular (el número 1 + 2 + 3 + ... + n).
"""
"""
def triangular(n: int)  -> int:
    """
    # Esta función calcula el n-ésimo número triangular
"""
    if n == 0:
        return n
    return n + triangular(n-1)

print(triangular(5))

"""

# Ejercicio 9
"""
Escriba una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que
tiene.
"""
"""
def digitos(n: int) -> int:
    if abs(n) < 10:
        return 1
    return 1 + digitos(n // 10)

print(digitos(-400))

"""
