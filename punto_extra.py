print ("Tabla de posiciones - torneo de futbol")
def mostrar_menu(): 
    print ("--- Menú del Torneo ---")
    print ("1. Agregar equipo")
    print ("2. Guardar resultado")
    print ("3. Mostrar tabla de posiciones")
    print ("4. Salir")

tabla = {}

def agregar_equipo (nombre):
    if nombre not in tabla:
        tabla [nombre] = {
            "PJ": 0, "PG": 0, "PP": 0,
            "GF": 0 , "GC": 0, "Pts": 0
        }
        print (f"Equipo '{nombre}' agregado a la tabla")
    else:
        print ("Este equipo ya esta registrado")

def guardar_resultado (local,visitante,marcador):
    g_local, g_visitante = map(int, marcador.split("-"))

    #actualizo partidos
    tabla [local][¨PJ¨] += 1
    tabla [visitante]["PJ"]+= 1

    #act goles

    tabla[local]["GF"] += g_local
    tabla[local]["GC"] += g_visitante
    tabla[visitante]["GF"] += g_visitante
    tabla[visitante]["GC"] += g_local

    #act resultados
    if g_local > g_visitante:
        tabla[local]["PG"] += 1
        tabla[visitante]["PP"] += 1
        tabla [local]["Pts"] += 3
    elif g_local < g_visitante:
        tabla[visitante]["PG"] += 1
        tabla[local]["PP"] += 1
        tabla[visitante]["Pts"] += 3
    else:
        tabla[local]["PE"] += 1
        tabla [visitante]["PE"]+= 1
        tabla[local]["Pts"] += 1
        tabla[visitante]["Pts"] += 1

def mostrar_tabla ()
    print ("Tabla de posiciones")


