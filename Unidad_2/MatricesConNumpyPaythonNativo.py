import numpy as np

print("===================== NumPy =====================")
matriz_A = np.array([[10, 15], [20, 5]])
matriz_B = np.array([[5, 12], [15, 8]])
total_productos = matriz_A + matriz_B

precio = 50
ingreso_total = total_productos * precio

print("Total de productos vendidos (Sábado + Domingo):")
print(total_productos)
print("\nIngreso total en pesos (a 50 pesos por producto):")
print(ingreso_total)


print("===================== NATIVO =====================")

matriz_A = [[10, 15], ]

matriz_B = [[5, 12], ]

total_productos = []
for i in range(len(matriz_A)):
    fila = []
    for j in range(len(matriz_A[i])):
        fila.append(matriz_A[i][j] + matriz_B[i][j])
    total_productos.append(fila)

precio = 50
ingreso_total = []
for i in range(len(total_productos)):
    fila = []
    for j in range(len(total_productos[i])):
        fila.append(total_productos[i][j] * precio)
    ingreso_total.append(fila)

print("Total de productos vendidos (Sábado + Domingo):")
print(total_productos)
print("\nIngreso total en pesos (a 50 pesos por producto):")
print(ingreso_total)


