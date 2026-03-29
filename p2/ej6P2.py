posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

hashtags = {}

for elemento in posts: 
    oracion = elemento.split()
    for palabra in oracion:
        if palabra.startswith("#"): 
            if palabra in hashtags :
                hashtags [palabra] += 1
            else:
                 hashtags [palabra] = 1

lista_trending = []
contador_unicos = 0
contador_totales = 0

for elemento in hashtags: 
    contador_totales += 1
    if hashtags[elemento] > 1:
        lista_trending.append ((elemento, hashtags[elemento]))
    else:
        contador_unicos += 1

print ("Cantidad de hashtags totales: ", contador_totales)
print ("Cantidad de hashtags que aparecen una sola vez: ", contador_unicos)
print ("Hashtags trending (mas de una aparicion): ", lista_trending)