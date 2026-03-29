peso = float(input ("Ingrese el peso de su paquete"))
destino = input ("Ingrese zona de destino(local/regional/nacional): ")

if destino not in ["local", "regional", "nacional"]:
    print("Zona no válida. Las zonas disponibles son: local, regional, nacional")

else: 
    if peso <= 1: 
        if destino == "local": 
           costo = 500
        elif destino == "regional": 
            costo = 1000
        else:
            costo = 2000
    elif peso <= 5: 
        if destino == "local":
            costo = 1000
        elif destino == "regional":
            costo = 2500
        else: 
            costo = 4500
    else: 
        if destino == "local":
            costo = 2000
        elif destino == "regional": 
            costo = 5000
        else: 
            costo = 8000
        
    print (f"El costo del envio es: ${costo}") 