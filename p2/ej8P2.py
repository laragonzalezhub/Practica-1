
def Cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for letra in mensaje:
        if letra.isalpha():  # si es una letra
            base = 'A' if letra.isupper() else 'a'
            # posición dentro del alfabeto (0 a 25)
            pos = (ord(letra) - ord(base) + desplazamiento) % 26
            resultado += chr(ord(base) + pos)
        else:
            resultado += letra  # deja espacios, números, signos igual
    return resultado

# Programa Principal
mensaje = input(f"Ingrese un mensaje: ")
desplazamiento = int(input(f"Ingrese el desplazamiento: "))

cifrado = Cifrar_mensaje(mensaje, desplazamiento)
print(f"Mensaje cifrado:{cifrado}")
print(f"Mensaje descifrado:{mensaje}")