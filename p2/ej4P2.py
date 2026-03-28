email = input ("Ingrese un email")
valido= True

if email.count("@") != 1:
    valido= False
else: 
    #divido para ver que hay de cada lado 
    parte_primera, parte_segunda = email.split ("@")

    #al menos un caracter antes de @

    if len(parte_primera) < 1:
        valido = False

    if "." not in parte_segunda: 
     valido = False

    if email.startswith ("@") or email.endswith ("@"):
        valido = False
    if email.startswith (".") or email.endswith ("."):
        valido = False

    ultima_parte = parte_segunda.split (".")[-1]
    if len (ultima_parte) < 2:
       valido = False

if valido: 
   print ("Email valido")
else: 
   print ("Email no valido")