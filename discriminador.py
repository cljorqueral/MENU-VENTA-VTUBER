def listar2D(lista): # retorna lista solo de las ventas bajo el criterio: 2D
    listafinal=[]
    for a in lista:
        if a[1]=="2D":
            listafinal.append(a)
    return listafinal

def listar3D(lista): # retorna lista solo de las ventas bajo el criterio: 3D
    listafinal=[]
    for a in lista:
        if a[1]=="3D":
            listafinal.append(a)
    return listafinal