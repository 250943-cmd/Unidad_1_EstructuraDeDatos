# 1. Función sin parámetros y sin retorno
def mostrar_encabezado_escuela():
    """Imprime el nombre de la institución y el título del reporte."""
    print("========================================")
    print("             INSTITUTO X                ")
    print("UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DE JUAREZ        ")
    print("========================================")

# 2. Función sin parámetros con retorno
def obtener_nota_minima_aprobatoria():
    """Retorna la nota mínima necesaria para aprobar el curso."""
    return 6.0

# 3. Función con 1 parámetro
def evaluar_rendimiento(nota_final):
    """Retorna una categoría descriptiva basada en la nota final."""
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    else:  # De 9.5 a 10
        return "Excelente"

# 4. Función con 2 parámetros
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    """Calcula la nota final con 70% exámenes y 30% tareas, redondeada a 1 decimal."""
    nota_final = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(nota_final, 1)

# 5. Función con 3 parámetros e integración
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    """Integra las funciones anteriores para calcular e imprimir la boleta del alumno."""
    # Llamadas a las funciones previas
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    
    # Determinar si necesita examen extraordinario
    necesita_extraordinario = "Sí" if nota_final < nota_minima else "No"
    
    # Impresión del desglose
    mostrar_encabezado_escuela()
    print(f" Alumno:       {nombre_alumno}")
    print(f" Nota Exámenes: {nota_examenes}")
    print(f" Nota Tareas:   {nota_tareas}")
    print(f" Nota Final:    {nota_final}")
    print(f" Estado:        {estado}")
    print(f" ¿Requiere Extraordinario?: {necesita_extraordinario}")
    print("========================================\n")


#  EJEMPLOS DE PRUEBA 
# Caso 1: Alumno Excelente (No requiere extraordinario)
generar_boleta("Carlos Mendoza", 9.8, 9.5)

# Caso 2: Alumno Aprobado (No requiere extraordinario)
generar_boleta("Ana Gómez", 7.5, 8.0)

# Caso 3: Alumno Reprobado pero por encima de la nota mínima (No requiere extraordinario)
# Su promedio da 6.5 (Está reprobado según la escala, pero es mayor o igual a la mínima de 6.0)
generar_boleta("Luis Pérez", 6.0, 7.5)

# Caso 4: Alumno Reprobado por debajo de la nota mínima (Requiere extraordinario)
generar_boleta("Sofía Castro", 5.0, 5.5)



escribir un programa en pytnon  que gestione una lista de nombres medianteoperaciones de incersion ,busqueda por indice y estraccion de sublistas utilizando sicling crea una lista inicial 
crea una lista llamada estudiantes que contenga los nombres ana,carlos y diana 
imprime la lista  original en pantalla 
insercion de elementos 
agraga al final de la lsista ala estudiante elena  utilizando (.append())
inserta ala estudiante beatriz en la posicion  con indice 1 usando el metodo  .insert() muestra en pantalla  la lista actualizada  tras ambas incersiones 
busquedas y acceso por indice 