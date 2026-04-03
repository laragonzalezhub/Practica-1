def puntaje_ronda (scores): 
    resultados = {}
    for participante, notas in scores.items(): 
        total = sum (notas.values())
        resultados[participante] = total
    return resultados

def buscar_ganador (resultados): 
    ganador = None
    mejor_puntaje = -1

    for participante, puntaje in resultados.items(): 
        if puntaje > mejor_puntaje: 
            mejor_puntaje = puntaje 
            ganador = participante
    return ganador, mejor_puntaje

def mostrar_ronda (num_ronda, ronda, acumulados, rondas_ganadas, mejor_ronda):
    print (f"Ronda: {num_ronda} - {ronda['theme']}: ")

    #calculo puntajes de esta ronda
    resultados = puntaje_ronda (ronda["scores"])

    #busco ganador de la ronda
    ganador, max_puntos = buscar_ganador (resultados)
    print (f"Ganador: {ganador} ({max_puntos} pts)")

    #actualizo acumulados
    for participante,puntaje in resultados.items():
        acumulados [participante] += puntaje
        if puntaje > mejor_ronda[participante]:
            mejor_ronda[participante] = puntaje
    rondas_ganadas [ganador] += 1

    #muestro tabla parcial
    print("Tabla parcial (ordenada por acumulado):")
    ordenados = sorted(acumulados.items(), key=lambda x: x[1], reverse=True)
    for participante, puntaje in ordenados:
        print(f"{participante:10} {puntaje}")
    print()



def mostrar_tabla_final (acumulados,rondas_ganadas, mejor_ronda, total_rondas): 
    print ("Tabla de posiciones final: ")
    print ("Cocinero  Puntaje   Rondas ganadas  Mejor ronda  Promedio")
    print ("-----------------------------------------------------------------")

    #ordeno de la manera pedida
    ordenados = sorted(acumulados.items(), key= lambda x:x[1], reverse= True)

    for participante,puntaje in ordenados: 
        promedio = puntaje / total_rondas
        print (f"{participante:10} {puntaje:6} {rondas_ganadas[participante]:13} {mejor_ronda[participante]:11} {promedio: }")