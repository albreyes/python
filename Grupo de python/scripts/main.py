from arbol import Arbol

arbol = Arbol("Luis")
arbol.agregar("María José")
arbol.agregar("Maggie")
arbol.agregar("Leon")
arbol.agregar("Cuphead")
arbol.agregar("Aloy")
arbol.agregar("Jack")
nombre = input("Ingresa algo para agregar al árbol: ")
arbol.agregar(nombre)
arbol.preorden()
arbol.inorden()
arbol.postorden()
# Búsqueda
busqueda = input("Busca algo en el árbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")
    # Aquí tienes en "nodo" toda la información del nodo. Tanto su izquierda, derecha, dato y otros atributos que le hayas agregado