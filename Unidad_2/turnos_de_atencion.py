import time
from collections import deque

# 2. Inicia la cola
cola_turnos = deque()

# 3. Registrar turnos (Encolar - FIFO)
cola_turnos.append("Turno A01 - ISIDRO ORTIZ RAMIREZ")
cola_turnos.append("Turno A02 - GUADALUPE PEREZ DIAZ")
cola_turnos.append("Turno A03 - JUANA LAZCANO RODRIGUEZ")

# 4. Mostrar turnos emitidos
print("Turnos emitidos en la fila del banco:")
for turno in cola_turnos:
    print(f" - {turno}")

print("\nIniciando atención en ventanilla\n")

# 5. Procesar la atención (Desencolar)
while cola_turnos:
    # Remueve al primer cliente en llegar
    cliente_actual = cola_turnos.popleft()
    
    print(f"Llamando a ventanilla: {cliente_actual}")
    # Simula el tiempo de atención (1 segundo)
    time.sleep(1)
    print(f"Atención finalizada: {cliente_actual}")
    
    # Muestra la cantidad de clientes restantes
    print(f"(Clientes restantes en la fila: {len(cola_turnos)})\n")

print("Se han atendido todos los turnos. Fila vacía.")
