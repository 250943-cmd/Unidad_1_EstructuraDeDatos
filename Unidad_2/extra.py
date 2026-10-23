pila = ["Plato 1", "Plato 2", "Plato 3", "Plato 4"]

print(pila) 

while pila:
    elemento_retirado = pila.pop()
    print(f"Se retiró: {elemento_retirado}")

print("¡La pila está completamente vacía!")
