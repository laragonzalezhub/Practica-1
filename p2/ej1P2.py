text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way 
to do it.
Although that way may not be obvious at first unless you're 
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good 
idea.
Namespaces are one honking great idea -- let's do more of 
those!"""

#cuanto cantidad de lineas separada por punto
lineas = text.split(".")
cant_lineas = len (lineas)
print (f"cantidad de lineas: {cant_lineas}")

#cuento cantidad de palabras totales
palabras = text.split(" ")
cant_palabras = len (palabras)
print (f"cantidad de palabras: {cant_palabras}")

#calculo promedio
promedio = cant_palabras/cant_lineas
print (f"el promedio de palabras por linea es: {promedio}")

#lineas por encima del promedio 
#lineas_superiores = [linea for linea in lineas if len(linea.split ()) > promedio]
#for l in lineas_superiores:
#   print (l)

for elemento in lineas:
    if len(elemento.split()) > promedio:
        print (elemento)

