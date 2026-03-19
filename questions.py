import random
words = {
     "redes sociales": ["instagram", "facebook", "snapchat", "twitter"],
     "programacion": ["python", "programa","variable","funcion","bucle","cadena","entero","lista"],
     "materias": ["gestion", "algoritmos", "matematica", "economia", "contabilidad"]
}



guessed = []
attempts = 6
puntos_totales = 0 

print("¡Bienvenido al Ahorcado!")
print()

print (f"Las categorias disponibles son: ", " , ".join(words.keys()))
categoria = input("elegi una categoria la categoria a jugar: ")
if categoria in words:
    word = random.choice (words[categoria])

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntos_totales += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        
        letter = input("Ingresá una letra: ")
        if len(letter)!= 1 or not letter.isalpha():
            print (f"Entrada no valida")
            continue
    
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntos_totales -=1
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntos_totales = 0

    print (f"el puntaje total que obtuviste es: {puntos_totales}")
else:
    print ("esa categoria no existe")