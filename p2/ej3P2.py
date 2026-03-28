review = """La película sigue a un grupo de astronautas que 
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo 
a través
de tormentas solares y fallos en el sistema de navegación. Al 
llegar
a Marte descubren que la base está abandonada y los 
suministros
destruidos. Torres decide sacrificar la nave nodriza para 
salvar
al equipo y logran volver a la Tierra en una cápsula de 
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje 
secreto."""

spoilers = input ("Ingrese una lista de palabras, separada con comas: ")
lista_spoilers = [word.strip() for word in spoilers.split(",")]

texto_nuevo= ""
review_lower = review.lower()

for palabra in review.split(" "):
    #saco comas, puntos, etc

    reemplazada = False 
    for word in lista_spoilers: 
       if palabra.lower() == word.lower():
            texto_nuevo += "*" * len (word) + " "
            reemplazada = True
            break
    if not reemplazada:
        texto_nuevo += palabra + " "

print (f"Reseña filtrada")
print (texto_nuevo)