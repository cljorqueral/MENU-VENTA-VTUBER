"""def abrirlista(nombrearchivo):
    listafinal=[]
    with open(nombrearchivo, 'r') as archivo:
        for linea in archivo:
            listafinal.append(eval(linea.strip()))
    return listafinal

def cerrarlista(nombrearchivo, lista):
    with open(nombrearchivo, 'w') as archivo:
        for list in lista:
            archivo.write(str(list) + '\n')

def agregaraarchivo(nombrearchivo, lista):
    with open(nombrearchivo, 'a') as archivo:
        archivo.write(str(lista) + '\n')
"""


# funciones pero trabajando en forma 1,2,3,4,5 . sin eval

def abrirlista(nombrearchivo):
    listafinal=[]
    with open(nombrearchivo, 'r') as archivo:
        for linea in archivo:
            lineaaux=linea.split(",")
            if len(lineaaux)==6:
                for i in [4,5]:
                    lineaaux[i]=int(lineaaux[i])
            else:
                for i in [0,3,4]:
                    lineaaux[i]=int(lineaaux[i])
            listafinal.append(lineaaux)
    return listafinal

def cerrarlista(nombrearchivo, lista):
    i=0
    with open(nombrearchivo, 'w') as archivo:
        for list in lista:
            for c in range(len(list)):
                archivo.write(f"{list[c]}")
                if c!=len(list)-1:
                    archivo.write(",")
            i=i+1
            if i!=len(lista):
                archivo.write("\n")
            

def agregaraarchivo(nombrearchivo, lista):
    with open(nombrearchivo, 'a') as archivo:
        archivo.write("\n")
        for c in range(len(lista)):
            archivo.write(f"{lista[c]}")
            if c!=len(lista)-1:
                archivo.write(",")
