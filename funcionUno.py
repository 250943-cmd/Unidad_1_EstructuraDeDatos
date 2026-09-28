import datetime
def saludar():
    print("Hola, Bienvenidos")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H","%M","%S")
    print(f"La hora actual es:{hora_actual}")
    mostrar_hora()

    import datetime

def decir_la_fecha():
    # No necesita datos externos, obtiene la fecha por sí misma
    fecha_hoy = datetime.date.today()
    print(f"Hoy es: {fecha_hoy}")

# Llamada a la función (paréntesis vacíos)
decir_la_fecha()

import random

def mostrar_numero_suerte():
    # Elige un número aleatorio entre 1 y 100 por sí sola
    numero = random.randint(1, 100)
    print(f"Tu número de la suerte de hoy es: {numero}")

# Al llamarla, los paréntesis van vacíos
mostrar_numero_suerte()



#Now() consulta el reloj o la hora del SO
#Strftime convertir la fecha y hora en texto, usando el formato establecido
#f-string la letra f indica a python que procese el texto
#e inserte las variables dentro de las llaves
#{hora_actual} se toma el valor almacenado en la variable de la hora_actual
#y lo reemplaza ahí mismo
