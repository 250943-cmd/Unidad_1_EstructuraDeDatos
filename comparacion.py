import matplotlib.pyplot as plt

datos = [42, 12, 88, 23, 7, 65, 34, 50]

# Algoritmo de inserción corregido
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if a[j] > clave:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = clave
    return a, comp

# Algoritmo de selección corregido
def seleccion(arr):
    a = arr.copy()
    comp = 0
    n = len(a)
    for i in range(n):
        min_idx = i  # Corrección: debe empezar en i, no en 1
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]  # Corrección del intercambio
    return a, comp

# Ejecutamos ambos algoritmos
lista_ordenada, comp_ins = insercion(datos)
_, comp_Sel = seleccion(datos)

# GRAFICACIÓN
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5))  # Corrección: subplots en plural

# Gráfico 1 inicial - lista desordenada
ax1.bar(range(len(datos)), datos, color='salmon')
ax1.set_title('1.-LISTA DESORDENADA')
ax1.set_ylabel('valor')

# Gráfico 2 lista ordenada
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='green')
ax2.set_title('2.-LISTA ORDENADA')

# Gráfico 3 - comparaciones realizadas
# Corrección: falta coma y los colores hexadecimales necesitan el símbolo '#'
ax3.bar(['insercion', 'seleccion'], [comp_ins, comp_Sel], color=["#2397EA", "#ac8059"])
ax3.set_title('3.-COMPARACIONES')
ax3.set_ylabel('cantidad')

plt.tight_layout()
plt.show()
