from aperturacierre import *
def crear(nombre_archivo):
    lista=abrirlista(nombre_archivo) #crea un producto y lo retorna para guardarlo
    lista.append(crear2(lista)) #agarra la lista existente, le agrega el nuevo dato y la cierra
    cerrarlista(nombre_archivo, lista)
    return lista #retorna la misma lista para uso en el programa
def crear2(lista): #funcion que retorna una lista, es auxiliar de crear()
    sw=0 
    while sw==0:
        sw=1
        while True: # se asume inicio correcto
            id=input("Ingrese el ID del producto: ")
            if len(id)!=4: print("EL ID DEBE SER UNA CADENA DE 4 CARACTERES")
            else:break
        for item in lista:
            if item[0] == id:
                print("ID YA EXISTENTE")
                sw=0 #en caso de existir, vuelve a 0 y repite
                break
    while True:
        tipo=input("Ingrese el tipo de Modelo (2D/3D): ")
        if tipo== "2D" or tipo== "3D":
            break
        else: print("INGRESE UNA OPCION VALIDA")
    
    producto=input("Ingrese el tipo de producto (Modelo/Manos/Assets): ")
    while True:
        unidad=input("Ingrese el tipo de precio (Precio por unidad o precio fijo): ")
        if unidad == "unidad" or unidad == "precio fijo":
            break
        else: print("INGRESE UNA OPCION VALIDA")
    while True:
        try:
            precio=int(input("Ingrese el precio del producto: "))
            stock=int(input("Ingrese stock del producto: "))
            if precio<0 or stock<0: print("UNO DE LOS VALORES ES MENOR QUE 0, INTENTE NUEVAMENTE")
            else: break 
        except ValueError: print("VALOR DEBE SER UN ENTERO")
    return [id,tipo,producto,unidad,precio,stock]

def buscar(nombre_archivo): #se usa nombre_archivo en la invocacion, pero solo se usa con "productos.txt"
    lista=abrirlista(nombre_archivo) #busca algo en la lista, no retorna nada solo muestra
    id=input("Ingrese el id del producto: ")
    sw=0
    for a in lista:
        if a[0]== id:
            sw=1
            print("ID ENCONTRADO")
            print(a[0],"",a[1],"",a[2],"",a[3],"",a[4],"",a[5])
    if sw==0: print("NO ENCONTRADO")

def actualizar(nombre_archivo):
    lista=abrirlista(nombre_archivo) #busca un producto en la lista, al encontrarlo pide los nuevos valores y retorna la lista actualizada
    c=0
    sw=0
    id=input("Ingrese el id del producto: ")
    for c in range(len(lista)): #se busca el id con un contador, para asi tener registro de la posicion del producto a modificar
        if lista[c][0] == id:
            sw=1
            print("ID ENCONTRADO")
            print(lista[c][0],"",lista[c][1],"",lista[c][2],"",lista[c][3],"",lista[c][4], "",lista[c][5])
            lista[c]=crear2(lista)
            
            """lista[c][0]=input("Ingrese el ID del producto: ")
            lista[c][1]=input("Ingrese el tipo de Modelo (2D/3D): ")
            lista[c][2]=input("Ingrese el tipo de producto (Modelo/Manos/Assets): ")
            lista[c][3]=input("Ingrese el tipo de precio (Precio por unidad o precio fijo): ")
            lista[c][4]=int(input("Ingrese el precio del producto: "))
            lista[c][5]=int(input("Ingrese el stock del producto: "))"""
    if sw==0: print("NO ENCONTRADO")
    elif sw==1:
        cerrarlista(nombre_archivo, lista)
    return lista
def borrar(nombre_archivo):
    lista=abrirlista(nombre_archivo) #se borra un producto basandose en el id indicado
    opcion=input("INGRESE ID A ELIMINAR: ")
    i=0
    for i in range(len(lista)): #se busca con un for para encontrar el valor i de la posicion y borrar ese mismo valor
        if lista[i][0]==opcion:
            del lista[i] #se usa del por funcionalidad
            break
    cerrarlista(nombre_archivo, lista)
    return lista
def listar(nombre_archivo): #se usa nombre_archivo pero solo se usa solo en "productos.txt"
    print("ID-TIPO-PRODUCTO-METODO DE VENTA-PRECIO-STOCK")
    lista=abrirlista(nombre_archivo) #abre el archivo de la lista y lo muestra por cada item existente
    for i in lista:
        print(i[0],"",i[1],"",i[2],"",i[3],"",i[4],"",i[5])