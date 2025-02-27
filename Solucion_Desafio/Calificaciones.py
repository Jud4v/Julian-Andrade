def calcularPromedio(calificaciones): # creamos la función calcular promedio donde calificaciones las pediremos en la función principal.
    return sum(calificaciones) / len(calificaciones) # sum lo usamos para sumar todas las calificaciones y len para que nos de el número de calificaciones que hay 
# asi sacamos el promedio dividiendo la sumatoria de todas las calificaciones por el numero de estas.

def definirSituacion(promedio): # en esta funci''on determinamos el promedio.
    if promedio >= 60: # si el promedio es mayor o igual que 60 sera aprobado.
        return "Aprobado"
    elif 40 <= promedio < 60: # si este promedio es menor que 60  y mayor o igual a 40 estara en recuperación.
        return "En recuperación"
    else:
        return "Reprobado" # por ultimo si no esta en estos rangos sera reprobado.


print("Ingrese 5 calificaciones:") # imprimimos al usuario que ingrese 5 calificaciones.
calificaciones = [] #creamos un arreglo vacio para guardar las calificaciones.
    
for i in range(5): # creacion del for iniciado en 0 con un rango maximo de 5 
        while True: # creamos un while que nos permitira confirmar si el usuario agrega una nota valida.
            try:
                nota = int(input(f"Calificación {i+1}: "))
                if 0 <= nota <= 100:
                    calificaciones.append(nota)
                    break # salimos del bucle una vez la calificación es correcta.
                else:
                    print("Por favor, ingrese una calificación entre 0 y 100.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")
    
promedio = calcularPromedio(calificaciones) # valores dados por las funciones anteriores.
situacion = definirSituacion(promedio)
    
print(f"Promedio final: {promedio}") # imprimimos en pantalla el promedio de las calificaciones y la situacion.
print(f"Situación académica: {situacion}")