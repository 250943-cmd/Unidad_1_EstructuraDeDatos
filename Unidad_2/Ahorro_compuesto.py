def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if not depositos:
        return 0.0
    
    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    return (saldo_anterior + depositos[-1]) * (1 + tasa_interes)

depositos_anuales = [1000, 2000, 1500]
tasa = 0.05

resultado = calcular_saldo_final(depositos_anuales, tasa)
print(f"Saldo final acumulado: {resultado}") 
