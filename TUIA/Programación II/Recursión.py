# Repaso de sintaxis básicas:
    # Crear una función y llamarla:
#def mi_funcion(lista: str) -> str: # Este es el nombre y adentro del () van los parámetros. Minúsculas y _ para separar palabras SIEMPRE. Los parámetros y lo que devuelve la función se expresan en los tipos de datos de esta manera      
#    """ !Dentro de este espacio se explica que hace la función como parte de la 
#    documentación de la misma, muy importante !"""
#    result = lista + " sumamos esto" #El código que ejecuta la función
#    return result #Lo que devuelve la función

#x = "hola" # Definimos una variable

#print(mi_funcion(x))

""" Una función es más reutilizable si devuelve un resultado (utilizando return)
en lugar de imprimirlo (utilizando print). Análogamente, una función es más reutilizable
si recibe parámetros en lugar de leer datos mediante la función input. """

# Recursión

"""Definición recursión: La recursión es una técnica para programar computadoras que involucra
el uso de procedimientos, subrutinas, funciones o algoritmos que se llaman a sí mismos hasta 
que se alcance una condición de finalización."""

"""Cualquier función recursiva tiene dos secciones de código claramente divididas:
    -> Por un lado, tiene que existir siempre una condición en la que la función retorna
        sin volver a llamarse. Es muy importante porque de lo contrario, la función se
        llamaría de manera indefinida. A este se lo llama caso base de la recursión.
    -> Por otro lado tenemos la sección en la que la función se llama a sí misma, con alguna
        variación en sus argumentos. A esto se lo llama caso recursivo de la recursión."""

    # Ejemplo del factorial
def factorial ( n : int ) -> int :
    """ Precondici ón: n entero >= 0. Devuelve : n!"""
    if n == 0:
        return 1
    return n * factorial ( n - 1)

# Ejercicio Escribir una función recursiva que sume los elementos de una lista en Python.
#def sumar ( lista : list [ int ]) -> int :
#    if len ( lista ) == 0:
#        return 0
#    return lista [0] + sumar ( lista [1:]) # Quita un elemento de la lista!!
