"""
La programación orientada a objetos es un paradigma de programación que nos permite organizar el código de
manera que se asemeje a como pensamos en la vida real. Así, pensamos en los problemas como un conjunto de
objetos que se relacionan entre sí. Estos objetos nos permiten agrupar un conjunto de variables y funciones
relacionadas en un mismo espacio de nombres, facilitando la abstracción de pensamiento y la modularización
del programa.
Cosas de lo más cotidianas pueden pensarse como un objeto, desde un gato o un auto. Cada uno de estos
objetos tiene ciertas características. Por ejemplo, para el caso de un gato podemos decir cual es su tamaño,
su color de pelo o su mestizaje. A estas características las llamamos atributos.
Por otro lado, cada objeto tiene una serie de comportamientos que lo distingue, por ejemplo en el caso de
gato podrían ser caminar o maullar. A estos comportamientos o funcionalidad propia de cada objeto los
llamaremos métodos.
Definición Objeto: Un objeto es un ente que consta de identidad, estado y de un comportamiento.

La clase es la plantilla de los objetos.
"""

class Point:
    """Representación de un punto en un plano cartesiano 2D"""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
"""
Al crear la clase Point, hemos creado un nuevo tipo de datos, también llamado Point. Los miembros de este
tipo se llaman también instancias del tipo o bien objetos del tipo. El proceso de crear una nueva instancia
de un tipo se llama instanciación.
Nota Por convención, nombraremos a las clases utilizando la primera letra en mayúscula, de forma de poder
distinguirlas rápidamente.
"""
# Elmétodo constructor __init__ es un método especial que es invocado cuando un objeto es creado.

mi_punto = Point(3, 4)

"""
El siguiente método, __str__ devuelve una representación como string de un objeto de tipo Point. Si la
clase provee este método, sobrecarga el comportamiento por defecto de la función built-in str 3
"""

print(mi_punto.x)


# Ejemplo clasee
"""
class MyList(): 
    def __init__(self, any_list: list[int]) -> None:
        self.any_list : any_list

    def square(self) -> list[int]:
        return [ x * x for x in self.any_list ]
    
    def doble(self) -> list[int]:
        return [ x * 2 for x in self.square() ]
    
    def sum(self) -> int:
        return sum(self.doble())
    
my_list = MyList([1, 2, 3, 4, 5])

print(my_list.sum())

"""