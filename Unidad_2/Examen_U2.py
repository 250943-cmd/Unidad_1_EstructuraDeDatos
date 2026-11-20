def diagonal_principal(matriz, indice=0):
    if indice == len(matriz):
        return 0
    return matriz[indice][indice] + diagonal_principal(matriz, indice + 1)

matriz =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

resultado = diagonal_principal(matriz)
print(f"La suma de la diagonal principal es {resultado}")
