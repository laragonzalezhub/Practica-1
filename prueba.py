import random

#modificacion tres
words = {
"programacion": ["python","programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
"verduras": ["lechuga", "zanahoria", "tomate", "repollo", "zapallo"],
"animales":["perro", "gato", "caballo", "vaca", "oveja" ]
}
#


print("¡Bienvenido al Ahorcado!")
print()

cantidad = int(input ("elegi la cantidad de rondas que queres jugar"))
for i in range (0,cantidad):
    guessed = []
    attempts = 6

    #modificcacion 2
    punto=0
#
          
    #modificacion tres
    print(f"categorias disponibles: ", ", ".join(words.keys()))
    categoria= input ("elegi una categoria")

    # modificaccion 4

    palabra = random.sample(words[categoria], len(words[categoria]))
    p = random.choice(palabra)
    #


    while attempts > 0:
          # Mostrar progreso: letras adivinadas y guiones para las que faltan
          progress = ""
          for letter in p:
                if letter in guessed:
                        progress += letter + " "
                else:
                        progress += "_ "
          print(progress)
          # Verificar si el jugador ya adivinó la palabra completa
          if "_" not in progress:
                print("¡Ganaste!")
                # modificcacion 2
                punto += 6
                #
                break

          print(f"Intentos restantes: {attempts}")
          print(f"Letras usadas: {', '.join(guessed)}")
        
          letter = input("Ingresá una letra: ")

    #primera modificacion 

          if len(letter)!= 1 or not letter.isalpha():
                print (f"entrada no valida")
                continue
    ##   
    
          if letter in guessed:
                print("Ya usaste esa letra.")
          elif letter in p:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
          else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")

    # modificcacion 2
                punto -= 1
    #

          print()
    else:
          print(f"¡Perdiste! La palabra era: {p}")
    # modificcacion 2
          punto = 0
    print (f"el puntaje es {punto}")
    #