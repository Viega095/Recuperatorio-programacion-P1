from Funciones import *
import os

def main():
    participantes = crear_matriz(5,4,None)
    cargado_nombres = False
    cargado_puntajes = False
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system("cls")
            cargado_nombres = cargar_nombres(participantes)
            
            if cargado_nombres:
                print("Se cargaron correctamente! y son:")
                for i in range(len(participantes)):
                    print(f"Nombre {i+1} = {participantes[i][0]}")
            else:
                print("Hubo un error reintentelo")
                
        elif opcion == "2":
            os.system("cls")
            cargado_puntajes = cargar_puntajes(participantes)
        
        elif opcion == "0":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
        
        if (cargado_nombres == False) or (cargado_puntajes == False):
            
            print("No se cargaron los nombres o los puntajes aun..")
            input("Precione un boton...")
            os.system("cls")
            
        else:    
            if opcion == "3":
                os.system("cls")
                cargar_informacion(participantes)
                        
            elif opcion == "4":
                os.system("cls")
                promedio_mayor_que(participantes, 4)
            elif opcion == "5":
                os.system("cls")    
                promedio_mayor_que(participantes, 7)
                
            elif opcion == "6":
                os.system("cls")
                promedio_por_jurado(participantes)
                
            elif opcion == "7":
                os.system("cls")
                jurado_estricto(participantes)
                
            elif opcion == "8":
                os.system("cls")
                buscar_participante(participantes)
                
            elif opcion == "9":
                os.system("cls")
                top_numero(participantes, 3)
                
            elif opcion == "10":
                os.system("cls")
                ordenar_alfabeticamente(participantes)
                
            elif opcion == "11":
                os.system("cls")
                top_numero(participantes, 1)
                
            elif opcion == "12":
                os.system("cls")
                desempatar(participantes)
                
            else:
                print("Opción inválida. Intente nuevamente.")

            input("Precione un boton...")
            os.system("cls")   
    
main()