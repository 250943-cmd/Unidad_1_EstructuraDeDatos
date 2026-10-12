# 1. Creación de la lista inicial
print("========================================")
estudiantes = ["Ana", "Carlos", "Diana"]
print("--- Lista  ---")
print(f"Lista inicial de estudiantes:{estudiantes}\n")
print("========================================")

estudiantes.append("Elena")
estudiantes.insert(1, "Beatriz")

print("--- Lista Actualizada ---")
print(f"Lista tras las inserciones: {estudiantes}\n")
print("========================================")


print("--- Búsqueda por Índice ---")
indice_buscar = 0
if indice_buscar < len(estudiantes):
    print(f"El estudiante en el índice {indice_buscar} es: {estudiantes[indice_buscar]}")
else:
    print(f"El índice {indice_buscar} está fuera de rango.")



indice_buscar = 2
if indice_buscar < len(estudiantes):
    print(f"El estudiante en el índice {indice_buscar} es: {estudiantes[indice_buscar]}")
else:
    print(f"El índice {indice_buscar} está fuera de rango.")

print(f"En el indice  3  se encuentra: {estudiantes[3]}\n")
print("========================================")

print("--- Extracción de Sublistas (Slicing) ---")

sublista_inicio = estudiantes[0:3]
print(f"Primeros tres estudiantes: {sublista_inicio}")

sublista_final = estudiantes[2:]
print(f"Estudiantes desde el índice 2 hasta el final: {sublista_final}")
print("========================================")


