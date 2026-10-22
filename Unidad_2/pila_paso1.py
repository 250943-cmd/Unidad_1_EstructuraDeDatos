
pila_platos = []

print("--- Paso 2: Apilar 10 elementos (Push) ---")
for i in range(1, 11):
    plato = f"Plato {i}"
    pila_platos.append(plato)
    print(f"Apilado: {plato}")

print("\n--- Paso 3: Consultar el elemento en la Cima (Top / Peek) ---")
if pila_platos:
    cima = pila_platos[-1]
    print(f"El elemento en la cima es: {cima}")

print("\n--- Paso 4: Desapilar 4 elementos (Pop) ---")
for _ in range(4):
    plato_retirado = pila_platos.pop()
    print(f"Desapilado: {plato_retirado}")

print("\n--- Paso 5: Consultar Tamaño (Size) y Estado Vacío (Empty) ---")
tamaño = len(pila_platos)
esta_vacia = len(pila_platos) == 0

print(f"Elementos restantes en la pila: {tamaño}")
print(f"¿La pila está vacía?: {esta_vacia}")
print(f"Estado actual de la pila: {pila_platos}")

print("\n--- EXTRA Paso 6: Vaciar la pila por completo ---")
while len(pila_platos) > 0:
    plato_retirado = pila_platos.pop()
    print(f"Vaciando... Se retiró: {plato_retirado}")

print(f"\n¿La pila está vacía al final?: {len(pila_platos) == 0}")
