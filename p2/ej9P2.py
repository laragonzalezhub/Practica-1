students = [
{"name": " Ana García ", "grade": "8", "status":
"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":
"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":
"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez ", "grade": None, "status":
"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":
"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":
"desaprobado"},
{"name": " ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":
"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":
"Aprobado"},
{"name": " sofía torres ", "grade": "8", "status":
"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":
"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":
"ausente"},
{"name": "roberto díaz", "grade": "", "status":
"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":
"aprobado"},
{"name": " laura méndez", "grade": "8", "status":
"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":
"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":
"Desaprobado"},
]

lista_limpia = []

def borrar_nombres(students):
    for elemento in students: 
       nombre = elemento ["name"]
       if nombre is not None: 
           nombre = nombre.strip()
           if nombre == "":
               continue
           lista_limpia.append(elemento)
    return lista_limpia 

def borrar_notas (students):
    lista_limpia = []
    for elemento in students:
        nota = elemento ["grade"]
        if nota is None or nota == "":
            continue 
        if not nota.isdigit (): #si no es num, lo descarto 
            continue
        elemento ["grade"] = int(nota)
        lista_limpia.append (elemento)
    return lista_limpia


def normalizar (students): 
    lista_normalizada = []
    for elemento in students : 
        nombre = elemento ["name"].strip().title()
        elemento["name"] = nombre 

        estado = elemento["status"].strip().title()
        elemento ["status"] = estado

        lista_normalizada.append(elemento)
    return lista_normalizada 

def eliminar_duplicados (students):
    diccionario = {}
    for elemento in students: 
        nombre = elemento ["name"]
        nota = elemento ["grade"]
        estado = elemento ["status"]

        #si no esta, lo agrego.  De lo contrario, comparo notas
        if nombre not in diccionario: 
            diccionario[nombre] = elemento 
        else: 
            if nota > diccionario[nombre]["grade"]:
                diccionario[nombre] = elemento

    #convierto dic a lista 
    return list(diccionario.values())

def ordenar (students): 
    return sorted (students, key = lambda x: x["name"])

#programa principal 

lista1 = borrar_nombres (students)
lista2 = borrar_notas (lista1)
lista3 = normalizar (lista2)
lista4 = eliminar_duplicados (lista3)
lista_final = ordenar (lista4)

print("Nombre Nota Estado")
print("------------------------------------------")
for r in lista_final:
    print(r["name"], r["grade"], r["status"])
print("Total de alumnos válidos:", len(lista_final))
