class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Creación de un nodo individual
nodo_singular = Nodo("Primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente) 


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Referencia inicial

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        
        # Caso 1: si la lista está vacía 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
            
        # Caso 2: recorrer hasta el último nodo que existe
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        # Conectar el último nodo con el nuevo nodo
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        elementos = []

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        # Sacamos el print del bucle while para que imprima la lista completa al final
        print(" -> ".join(elementos) + " -> None")


# Uso del programa
lista = ListaEnlazada()

# Insertar elementos a utilizar 
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")

lista.mostrar_lista()
