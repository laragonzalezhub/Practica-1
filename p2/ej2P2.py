playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

def segundos (duration):
    m,s = map (int, duration.split (":"))
    return m * 60 + s

segundos_totales = sum(segundos(song["duration"]) for song in playlist)
minutes = segundos_totales // 60
seconds = segundos_totales % 60

#busqueda de cancion mas corta y larga 
mayor= playlist [0]
menor = playlist [0]

for song in playlist:
    if segundos(song["duration"]) > segundos (mayor ["duration"]):
        mayor = song
    if  segundos (song ["duration"]) < segundos (menor ["duration"]):
        menor = song

print (f"La duracion total es: {minutes}m {seconds}s")
print (f"Cancion mas larga: {mayor["title"]}, ({mayor ["duration"]})")
print (f"Cancion mas corta: {menor ["title"]}, ({menor ["duration"]})")