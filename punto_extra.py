print ("Tabla de posiciones - torneo de futbol")
def mostrar_menu(): 
    print ("--- Menú del Torneo ---")
    print ("1. Agregar equipo")
    print ("2. Guardar resultado")
    print ("3. Mostrar tabla de posiciones")
    print ("4. Salir")



def agregar_equipo (nombre):
    if nombre not in tabla:
        tabla [nombre] = {
            "PJ": 0, "PG": 0, "PP": 0,
            "GF": 0 , "GC": 0, "Pts": 0
        }
        print (f"Equipo '{nombre}' agregado a la tabla")
    else:
        print ("Este equipo ya esta registrado")

def guardar_resultado (tabla):
    local = input("Equipo local: ")
    visitante = input("Equipo visitante: ")
    glocal = input("Goles local: ")
    gvisitante = input("Goles visitante: ")

    #actualizo partidos 
    tabla [local]["PJ"] +=1
    tabla [visitante]["PJ"] +=1

    #guardo goles
    tabla [local]["GF"] +=glocal
    tabla [local]["GC"] += gvisitante
    tabla [visitante]["GC"] += glocal
    tabla [visitante]["GF"] +=gvisitante

    #actualizo resultados 
    if glocal > gvisitante:
        tabla[local]["PG"] +=1
        tabla [local]["Pts"] += 3
        tabla [visitante]["PP"]+=1
    elif glocal < gvisitante:
        tabla [visitante]["PG"]+=1
        tabla [visitante]["Pts"]+= 3
        tabla [local]["PP"] +=1
    else:
        tabla [local]["Pts"]+= 1
        tabla [visitante]["Pts"]+= 1

def mostrar_tabla(tabla): 
    print ("TABLA DE POSICIONES")
    ordenado_por_valor = sorted(tabla.items(), key=lambda item: item[1], reverse =True)
    for nombre, Pts in ordenado_por_valor:
        print (f"{nombre}: {Pts}")

def eliminar_equipo (nombre):
    if nombre in tabla:
        del tabla[nombre]
        print (f"equipo eliminado con exito")
    else:
        print(f"no existe el equipo")

#Programa principal 

tabla = {}
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_equipo(input("Nombre del equipo"))
    elif opcion == "2":
        guardar_resultado(tabla)
    elif opcion == "3":
        mostrar_tabla(tabla)
    elif opcion == "4":
        eliminar_equipo((input("Nombre del equipo a eliminar")))
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")




    


