"""
-> Los tipos de datos definidos en unidades anteriores son tipos de datos
concretos. Por ejemplo: Point (punto) se definio como un par ordenado
de flotantes; Rectangle (rect ́angulo) se definio como un punto y dos
flotantes.

-> Otra forma de definir tipos de datos es mediante sus operaciones:
enumerandolas e indicando su comportamiento (es decir, cual es su
resultado esperado).

-> Esta manera de definir datos se conoce como Tipos Abstractos de
Datos o TADs (o tipo de datos abstracto, ambas provienen de la
traduccion del t ́ermino en ingl ́es abstract data type).
"""

"""
-> Un tipo abstracto de datos o TAD es:
    -> Una colección de datos
    -> Acompañada de un conjunto de operaciones para manipularlos,
    de forma tal que que queden ocultas la representación interna
    del nuevo tipo y la implementación de las operaciones, para 
    todas las unidades de programa que lo utilice

-> Por qué son útiles?
    -> LOs programas que los usan hacen referencia a las operaicones
    que tienen, no a la representación, y por lo tanto ese programa
    sigue funcionando si se cambia la representación.
    -> Simplifican el desarrollo de algoritmos utilizando las 
    operaciones del tipo abstracto de dato, sin importar como las
    mismas son implementadas.
    -> Dado que una operación puede ser implementada de diferentes
    formas en un TAD, resulta útil escribir algoritmos que puedan
    ser utilizados en cualquiera de sus posibles implementaciones.
    -> Algunos TADs utilizados con frecuencia, son implementados 
    en librerías estándares de manera que puedan ser utilizados
    por cualquier programador.
    -> Las operaciones de los TADs proveen una especia de lenguaje
    de alto nivel para discutir y especificar otros algoritmos.
-> Dentro del ciclo de vuda de un TAD hay dos fases:
    -> La programación del TAD: en la cual se elige una
    representación, y luego se programa cada unode los métodos sobre
    esa representación.
    -> La construcción de los programas que lo usan: en esa fase no
    será relevante para el programador que utiliza el TAD cómo está
    implementado, sino únicamente los métodos que posee.

"""

"""
1. Pila (Stack)
Una pila es una estructura de datos que sigue el principio
LIFO (Last In, First Out), es decir, el último elemento que 
se agrega es el primero en salir.

Operaciones básicas:
Push: Agregar un elemento a la pila.
Pop: Eliminar el último elemento agregado.
Peek o Top: Ver el elemento en la cima sin eliminarlo.
isEmpty: Comprobar si la pila está vacía.
"""

#PILA
class cola:
    def __init__(self):
        self.datos = []
        self.len = 0
        self.sumatoria = 0

    def push(self , elemento) -> None:
        self.datos.append(elemento)
        self.len = len(self.datos)
        self.sumatoria += elemento

    def pop(self) -> int:
        ret = self.datos.pop()
        self.sumatoria -= ret
        self.len = len(self.datos)
        return ret
    
    def promedio(self):
        return self.sumatoria/self.len

"""    
2. Cola (Queue)
Una cola es una estructura de datos que sigue el principio 
FIFO (First In, First Out), es decir, el primer elemento que 
se agrega es el primero en salir.

Operaciones básicas:
Enqueue: Agregar un elemento a la cola.
Dequeue: Eliminar el primer elemento agregado.
Front: Ver el primer elemento sin eliminarlo.
isEmpty: Comprobar si la cola está vacía.
"""





#COLA:
class cola:
    def __init__(self):
        self.datos = []
        self.len = 0
        self.sumatoria = 0

    def push(self , elemento) -> None:
        self.datos.append(elemento)
        self.len = len(self.datos)
        self.sumatoria += elemento

    def pop(self) -> int:
        ret = self.datos.pop(0)
        self.sumatoria -= ret
        self.len = len(self.datos)
        return ret
    
    def promedio(self):
        return self.sumatoria/self.len
    





class Pila:
    def __init__(self):
        self.items = []  # Usamos una lista para almacenar los elementos
        self.length = 0  # Atributo para almacenar el tamaño de la pila
    
    def isEmpty(self):
        return self.length == 0  # Si length es 0, la pila está vacía
    
    def push(self, item):
        self.items.append(item)  # Agrega un elemento a la cima de la pila
        self.length += 1  # Incrementa el tamaño
    
    def pop(self):
        if not self.isEmpty():
            self.length -= 1  # Decrementa el tamaño
            return self.items.pop()  # Elimina y devuelve el último elemento
        else:
            raise IndexError("pop from empty stack")  # Lanza error si la pila está vacía
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]  # Devuelve el último elemento sin eliminarlo
        else:
            raise IndexError("peek from empty stack")  # Lanza error si la pila está vacía
    
    def size(self):
        return self.length  # Devuelve el tamaño de la pila (en lugar de usar len)


# Crear una pila
pila = Pila()

# Agregar elementos
pila.push(1)
pila.push(2)
pila.push(3)

# Ver el último elemento
print(pila.peek())  # 3

# Eliminar el último elemento
pila.pop()
print(pila.peek())  # 2

# Verificar si la pila está vacía
print(pila.isEmpty())  # False

# Obtener el tamaño de la pila
print(pila.size())  # 2
