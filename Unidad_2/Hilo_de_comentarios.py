def maxima_profundidad(comentarios: list) -> int:
    if not comentarios:
        return 0
    
    profundidad_max = 0
    
    for elem in comentarios:
        if isinstance(elem, list):
            profundidad_actual = 1 + maxima_profundidad(elem)
        else:
            profundidad_actual = 1
            
        if profundidad_actual > profundidad_max:
            profundidad_max = profundidad_actual
            
    return profundidad_max

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
resultado = maxima_profundidad(hilo)
print(f"RESULTADO 3: {resultado}")
