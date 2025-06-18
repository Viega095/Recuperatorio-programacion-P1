from input import *
import random

def mostrar_menu():
    print("----- MENÚ PRINCIPAL -----")
    print("1. >> Cargar nombres de los participantes")
    print("2. >> Cargar puntuaciones de los jurados")
    print("3. Mostrar puntuaciones y promedios")
    print("4. Promedios mayores a 4")
    print("5. Promedios mayores a 7")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Buscar participante por nombre")
    print("9. Top 3 participantes")
    print("10. Participantes ordenados alfabéticamente")
    print("11. Mostrar ganador")
    print("12. Desempatar")
    print("0. Salir")
    
#GENERAL
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
    #Creamos la matriz solicitada por el programador (nosotros seria)
    return matriz

#1
def cargar_nombres(Lista:list) -> bool:
    for i in range(len(Lista)):
        while True:
            nombre_nuevo = input("Cual nombre desea agregar? ")
            #Se le pregunta que nombre quiere agregar
            if validar_str(nombre_nuevo):
                #Lo verifica y lo reemplaza en la lista creada
                Lista[i][0] = nombre_nuevo
                break
            else:
                #Si da error la verificacion lo solicita de nuevo
                print("Reintentalo de nuevo.")
    return True
#2
def cargar_puntajes(lista:list) -> bool:
    for f in range(len(lista)):
        #Aca recorre la lista de los concursantes y sus puntajes
        print(f"Puntaje de: {lista[f][0]}") #el nombre
        for c in range(1, 4):
            while True:
                #se le solicita el numero
                puntaje = input(f"Puntaje del juez {c}: ")
                #lo verifica si es numero
                if validar_numeros(puntaje):
                    puntaje = int(puntaje)
                    if (0 <= puntaje <= 10):
                        #Verifica si esta entre 0-10 y si esta bien lo reemplaza en la lista
                        lista[f][c] = puntaje
                        break
                    else:
                        #Si el numero es mayo o menor ser le imprime el mensaje
                        print("El numero tiene  que esta entre 0-10")
                else:
                    #Si dio error y no puso un numero se le pide de nuevo
                    print("Reintentelo de nuevo.")
                    
    return True
                    
#3            
def cargar_informacion(Lista:list) -> any:
    for f in range(len(Lista)):
        #Recorre toda la lista
        print(f"Concursante: {Lista[f][0]}")
        #Aca imprime el nombre del concursante
        for c in range(1, 4):
            print(f"JUEZ {c}: {Lista[f][c]}")
            #imprime a los juecez  y su puntuacion del concursante
        print(f"Con su promedio de: {(Lista[f][1] + Lista[f][2] + Lista[f][3]) / 3}")
        #Muestra el promedio
#4 y 5    

def promedio_mayor_que(participantes:list ,minimo:int):
    #Una bandera por si no hay promedios en el rango estrablecido
    no_hay = True
    for i in range(len(participantes)):
        #Recorre la lista y crea su promedio
        promedio = (participantes[i][1] + participantes[i][2] + participantes[i][3]) / 3
        if promedio >= minimo :
            #Verifica si el promedio es igual o mayor al minimo solicitado y si es asi se desactiva la bandera puesta anteriormente
            no_hay = False
            #Y muestra al usuario que supero este promedio
            print(f"El participante {participantes[i][0]} tiene promedio mayor con: {promedio}")
    if no_hay:
        #verifica si la bandera sigue en true y muestra el print
        print(f"Perdon no hubo un promedio mayora {minimo}")
            

#6
def promedio_por_jurado(Votaciones:list):
    #Guardamos las variables en las que tenemos que sumar (antes de que de error)
    votos_jurado1 = 0
    votos_jurado2 = 0
    votos_jurado3 = 0
    for i in range(len(Votaciones)):
        #Suma x columna de cada puntuacion de cada concursante
        votos_jurado1 += Votaciones[i][1] 
        votos_jurado2 += Votaciones[i][2] 
        votos_jurado3 += Votaciones[i][3] 
    #Y hace ell promedio y lo printea    
    print(f"Promedio de JUEZ 1: {votos_jurado1 / len(Votaciones)}")
    print(f"Promedio de JUEZ 2: {votos_jurado2 / len(Votaciones)}")
    print(f"Promedio de JUEZ 3: {votos_jurado3 / len(Votaciones)}")
    
#7
def jurado_estricto(Votaciones:list):
    #Hace lo mismo que la anterior funcion solo que vamos a tener muchos puntos
    votos_jurado1 = 0
    votos_jurado2 = 0
    votos_jurado3 = 0
    for i in range(len(Votaciones)):
        #Suma x columna de cada puntuacion de cada concursante
        votos_jurado1 += Votaciones[i][1] 
        votos_jurado2 += Votaciones[i][2] 
        votos_jurado3 += Votaciones[i][3] 
    
    #Guardamos la primera variable como minimo y lo comparamos con los demas
    minimo = votos_jurado1
    if votos_jurado2 < minimo:
        minimo = votos_jurado2 #Si alguno de estos es mennor lo reemplaza en el minimo
    if votos_jurado3 < minimo:
        minimo = votos_jurado3
    
    #Creamos una variable para agregarle(no modificarla porque no se puede, es inmutable)
    mensaje = "El jurado mas estricto es:"
    
    if votos_jurado1 == minimo:
        mensaje += " - Juez 1"
    if votos_jurado2 == minimo:  #Agregamos el mensaje del promedio minimo que dio
        mensaje += " - Juez 2"
    if votos_jurado3 == minimo:
        mensaje += " - Juez 3"
    print(mensaje) #Printeamos el mensaje
    
#8    
def buscar_participante(Nombres:list):
    while True:
        #Preguntamos cual nombre quiere buscar
        buscar_nombre = input("Cual nombre desea buscar en la lista? ").lower()
        if validar_str(buscar_nombre):
            #Validamos primero la respuesta
            for i in range(len(Nombres)):
                #Se busca el nombre del participante en minuscula y verifica toda la lista
                if Nombres[i][0].lower() == buscar_nombre:
                    #Mostramos la informacion del concursante
                    print(f"Se encontro el nombre de {buscar_nombre}")
                    print(f"Juez 1: {Nombres[i][1]}")
                    print(f"Juez 2: {Nombres[i][2]}")
                    print(f"Juez 3: {Nombres[i][3]}")
                    break
            else:
                #Si no se encuentra la persona en toda la lista se printea:
                print("No se  encontro a esa persona.")
                break
        else:
            #Si dio algun error la verificacion printea:
            print("Escribio mal el nombre o hubo un error")
            break
#9 y 11
def top_numero(participantes:list, numero:int):
    #Creamos una matriz que guarde le nombre del participante y su promedio 
    promedios = crear_matriz(len(participantes), 2, None)
    #Recorremos la lista y los guardamos en cada fila y columna que estrablecemos
    for i in range(len(promedios)):
        promedios[i][0] = participantes[i][0]
        promedios[i][1] = ((participantes[i][1] + participantes[i][2] + participantes[i][3]) / 3)
    
    for i in range(len(promedios) - 1):
        #Recorremos la lista en busca del maximo y guardamos el primero para verificar con las otras variables y ver cual es el maximo
        maximo = i
        for j in range(i + 1, len(promedios)):
            #Verifica si el primer promedio que establecimos es el maximo o no
            if promedios[j][1] > promedios[maximo][1]:
                #Si hay otro mayor reemplzamos el maximo con el nuevo encontrado
                maximo = j
        #Reemplzamamos el  primer promedio (Con su promedio y nombre) por el nuevo encontrado y lo guarda con el primero
        auxiliar = promedios[i]
        promedios[i] = promedios[maximo]
        promedios[maximo] = auxiliar
    #Despues de ordenar en altos y bajos printea el top seleccionado
    print(f"---El Top {numero} ---")
    for i in range (0, numero):
        #Printea cada usuario o el usuario que se establecio al inicio
        print(f"Nombre: {promedios[i][0]}, Con promedio: {promedios[i][1]}")
        
#10     
def ordenar_alfabeticamente(participantes:list):
    for i in range(len(participantes)): #Recorre la lista entera x1
        for j in range(len(participantes)): #Recorre la lista entera x2
            if participantes[i][0] < participantes[j][0]:
                #Verifica el participante de la a-z y si es true lo reemplaza 
                auxiliar = participantes[i]
                participantes[i] = participantes[j]
                participantes[j] = auxiliar
    #Printea todos los nombres ordenados quedaron en la lista
    print("Los nombres ordenados quedaron:")
    for i in range(len(participantes)):
        #Corre la lista entera con cada informacion  del concursante
        print(f"Nombre del concursante: {participantes[i][0]}")
        print(f"Puntaje 1: {participantes[i][1]}")
        print(f"Puntaje 2: {participantes[i][2]}")
        print(f"Puntaje 3: {participantes[i][3]}")
        print(f"Con su promedio de: {(participantes[i][1] + participantes[i][2] + participantes[i][3]) / 3}")
     
#12                
def desempatar(participantes:list):
    #Creamos matriz para guardar promedios (robados del #9)
    promedios = crear_matriz(len(participantes), 2, None)
    
    for i in range(len(promedios)):
        #Guarda lo mismo del 9 (nombres y promedios)
        promedios[i][0] = participantes[i][0] 
        promedios[i][1] = (participantes[i][1] + participantes[i][2] + participantes[i][3]) / 3
        
    for i in range(len(promedios)):
        #recorre la lista
        for j in range(i + 1, len(promedios)):
            #Verifica en la lista entera si el promedio es igual y se hace un random
            if promedios[i][1] == promedios[j][1]:
                #Printea que hay un empate si lo encuentra
                print("Hubo un empate!!")
                print(f"Entre el usuario {promedios[i][0]} y {promedios[j][0]}") #Muestra los usuarios qiue estan en empate
                #Creamos una variable random que eliga random 1 o 2
                desempate = random.randint(1, 2)
                if desempate == 1:
                    #Si la variable es 1 gana el primer concursante
                    print(f"Gana el concursante: {promedios[i][0]}")
                    return True
                else:
                    #Si la variable es 2 gana el segundo concursante
                    print(f"Gana el concursante: {promedios[j][0]}")
                    return True
    #Si no encuentra ningun empate Se printea que no hay
    print("No hubo un empate!")
    return False
    
                
    