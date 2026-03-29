import random

entrada = input ("Ingrese una lista de nombres de participantes (separados por comas): ").lower()
nombres = entrada.split(",")

if len(nombres) < 3: 
    print ("Debe haber al menos 3 participantes")
    exit()

if len (nombres) != len(set(nombres)): 
    print ("Hay nombres duplicados ")
else: 
    asignados = nombres [:] 
    while True: 
        random.shuffle (asignados)
        if all (n != a for n,a in zip (nombres,asignados)):
            break

    print ("Asignacion de amigo invisible: ")
    for n,a in zip (nombres,asignados):
        print (f"{n} → {a}")
