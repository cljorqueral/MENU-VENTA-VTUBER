import datetime
import os
from crud import *
from fechas import *
from aperturacierre import *
from discriminador import *
os.system("cls")
#ASUMIR PRECIOS EN DOLARES
print("""
 ______   _____   ______   _________  ________  ____    ____       _        ______   ________   ____   ____  ________  ____  _____  _________     _       ______   
.' ____ \ |_   _|.' ____ \ |  _   _  ||_   __  ||_   \  /   _|     / \      |_   _ `.|_   __  | |_  _| |_  _||_   __  ||_   \|_   _||  _   _  |   / \    .' ____ \  
| (___ \_|  | |  | (___ \_||_/ | | \_|  | |_ \_|  |   \/   |      / _ \       | | `. \ | |_ \_|   \ \   / /    | |_ \_|  |   \ | |  |_/ | | \_|  / _ \   | (___ \_| 
 _.____`.   | |   _.____`.     | |      |  _| _   | |\  /| |     / ___ \      | |  | | |  _| _     \ \ / /     |  _| _   | |\ \| |      | |     / ___ \   _.____`.  
| \____) | _| |_ | \____) |   _| |_    _| |__/ | _| |_\/_| |_  _/ /   \ \_   _| |_.' /_| |__/ |     \ ' /     _| |__/ | _| |_\   |_    _| |_  _/ /   \ \_| \____) | 
 \______.'|_____| \______.'  |_____|  |________||_____||_____||____| |____| |______.'|________|      \_/     |________||_____|\____|  |_____||____| |____|\______.' 
                                                                                                                                                                    
""") #se usa un print con el ascii pregenerado, para evitar conflictos en dispositivos que no tengan preinstalado pyfiglet
os.system("pause")
FECHA_HOY=datetime.now()

nombre_archivo="productos.txt"
"""ListaOpciones=abrirlista(nombre_archivo)"""
nombre_archivoventas="ventas.txt"
"""ventas=abrirlista(nombre_archivoventas)
folio=ventas[-1][0]+1"""
ListaOpciones=[]
ventas=[]
folio=10000
archivoscargados=False
while True: # ciclo principal de opciones
    try:
        opcion=int(input("""
SISTEMA DE VENTAS
1- VENDER
2- REPORTES
3- MANTENEDORES
4- Administracion
5- SALIR
Elija su opcion: 
"""))
        match opcion: #linea principal de opciones de rango 1-4
            case 1:
                os.system("cls")
                while True: #ciclo secundario de opciones, se queda en modo ventas hasta que usuario salga
                    opcionventa=input("""
1-2D
2-3D
3-SALIR
Elija su opcion:
""")
                    if opcionventa=="1":
                        os.system("cls")
                        preciofinal=900
                        lista2D=listar2D(ListaOpciones)
                        while True: #ciclo tercierio de opciones, se queda aqui hasta efectuar venta o se salga manualmente
                            print("ID-TIPO-PRODUCTO-METODO DE VENTA-PRECIO-STOCK")
                            for i in lista2D:
                                print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
                            print("SALIR : -1")
                            try:
                                opcion2D=input("Ingrese la opcion que desee agregar a su carrito: ")
                                if opcion2D==-1:
                                    break
                                sw=0
                                i=0
                                cantidad=1
                                for i in range(len(lista2D)): #revision de si producto existe en la lista
                                    if lista2D[i][0]==opcion2D:
                                        sw=1
                                        if lista2D[i][3]=="unidad":
                                            cantidad=int(input(f"Ingrese cantidad de: {lista2D[i][2]} que desea agregar a su carrito: "))
                                            break
                                        else:
                                            print(f"Producto {lista2D[i][2]} agregado al carrito")
                                            break
                                    i+=1
                                if sw==0: # si no existe, se vuelve al inicio del ciclo y se pide nuevamente al usuario un id
                                    print("NO ENCONTRADO")
                                    os.system("pause")
                                if sw==1:
                                    while True:
                                        if (lista2D[i][5]-cantidad)<0: #si cantidad excede a stock se vuelve a inicio de la venta
                                            print("ERROR - FUERA DE STOCK")
                                            os.system("pause")
                                            break
                                        confirmacion=input((f"Desea comprar {cantidad} de {lista2D[i][2]}? si/no: "))
                                        if confirmacion.lower()=="si" or confirmacion.lower()=="s": #si todo salio bien hasta ahora, se calcula precio y se agrega folio a la lista ventas
                                            preciofinal=preciofinal+cantidad*lista2D[i][4]
                                            vendido=[folio, FECHA_HOY.strftime("%d-%m-%Y"), lista2D[i][0], cantidad, preciofinal]
                                            ventas.append(vendido)
                                            agregaraarchivo(nombre_archivoventas, vendido)
                                            folio=folio+1
                                            for j in range(len(ListaOpciones)): #se retira el stock de la lista principal
                                                if ListaOpciones[j][0]==lista2D[i][0]:
                                                    ListaOpciones[j][5]=ListaOpciones[j][5]-cantidad
                                            break
                                        elif confirmacion.lower()=="no" or confirmacion.lower()=="n":
                                            break
                                        else: print("Ingrese una opcion valida")
                            except ValueError:
                                print("Valor debe ser un entero")


                    elif opcionventa=="2": #mismo metodo que en opcionventa 1, aca usando 3D en vez de 2D
                        os.system("cls")
                        preciofinal=700
                        lista3D=listar3D(ListaOpciones)
                        while True:
                            print("ID-TIPO-PRODUCTO-METODO DE VENTA-PRECIO-STOCK")
                            for i in lista3D:
                                print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
                            print("SALIR : -1")
                            try:
                                opcion3D=input("Ingrese la opcion que desee agregar a su carrito: ")
                                if opcion3D==-1:
                                    break
                                sw=0
                                i=0
                                cantidad=1
                                for i in range(len(lista3D)):
                                    if lista3D[i][0]==opcion3D:
                                        sw=1
                                        if lista3D[i][3]=="unidad":
                                            cantidad=int(input(f"Ingrese cantidad de: {lista3D[i][2]} que desea agregar a su carrito: "))
                                            break
                                        else:
                                            print(f"Producto {lista3D[i][2]} agregado al carrito")
                                            break
                                    i+=1
                                if sw==0: print("NO ENCONTRADO")
                                if sw==1:
                                    while True:
                                        if (lista3D[i][5]-cantidad)<0:
                                            print("ERROR - FUERA DE STOCK")
                                            break
                                        confirmacion=input((f"Desea comprar {cantidad} de {lista3D[i][2]}? si/no: "))
                                        if confirmacion.lower()=="si" or confirmacion.lower()=="s":
                                            preciofinal=preciofinal+cantidad*lista3D[i][4]
                                            vendido=[folio, FECHA_HOY.strftime("%d-%m-%Y"), lista2D[i][0], cantidad, preciofinal]
                                            ventas.append(vendido)
                                            agregaraarchivo(nombre_archivoventas, vendido)
                                            folio=folio+1
                                            for j in range(len(ListaOpciones)):
                                                if ListaOpciones[j][0]==lista3D[i][0]:
                                                    ListaOpciones[j][5]=ListaOpciones[j][5]-cantidad
                                            break
                                        elif confirmacion.lower()=="no" or confirmacion.lower()=="n":
                                            break
                                        else: print("Ingrese una opcion valida")
                            except ValueError:
                                print ("Valor debe ser un entero")

                    elif opcionventa=="3":
                        break
                    else:
                        print("OPCION INVALIDA")
                        os.system("pause")


            case 2: #REPORTES usando lista ventas generada por ventas.txt o las ventas de esta sesion
                os.system("cls")
                print("1- REPORTE POR FECHA")
                print("2- REPORTE POR INTERVALO DE FECHAS")
                print("3- REPORTE TOTAL")
                print("4- SALIR")
                try:
                    op2=int(input("Ingrese su opcion: "))
                    match op2:
                        case 1: 
                            fecha=input("INGRESE LA FECHA EN FORMATO DD-MM-AAAA: ")
                            fechafija(ventas, fecha)
                            os.system("pause")
                        case 2: 
                            fecha1=input("INGRESE LA FECHA INICIO EN FORMA DD-MM-AAAA: ")
                            fecha2=input("INGRESE LA FECHA FINAL EN FORMA DD-MM-AAAA: ")
                            intervalo_ventas(ventas,fecha1,fecha2)
                            os.system("pause")
                        case 3: 
                            todas_fechas(ventas)
                            os.system("pause")
                        case 4: 
                            break
                except ValueError:
                                print("Valor debe ser un entero")
            case 3: #menu CRUD
                os.system("cls")
                try:
                    opcion=int(input("""
1- Crear producto
2- Buscar
3- Actualizar
4- Borrar
5- Listar
6- Salir
Elija su opcion: 
        """))
                    match opcion:
                        case 1:
                            os.system("cls")
                            ListaOpciones=crear(nombre_archivo)
                            os.system("pause")
                        case 2:
                            os.system("cls")
                            buscar(nombre_archivo)
                            os.system("pause")
                        case 3:
                            os.system("cls")
                            ListaOpciones=actualizar(nombre_archivo)
                            os.system("pause")
                        case 4:
                            os.system("cls")
                            ListaOpciones=borrar(nombre_archivo)
                            os.system("pause")
                        case 5:
                            os.system("cls")
                            listar(nombre_archivo)
                            os.system("pause")
                        case 6:
                            break
                except ValueError:
                    print ("Valor debe ser un entero")
            case 4:
                op3=int(input("""
1- CARGAR DATOS
2- RESPALDAR DATOS
3- SALIR
Elija su opcion: 
"""))
                match op3:
                    case 1:
                        if not archivoscargados:
                            ListaOpciones=abrirlista(nombre_archivo)
                            ventas=abrirlista(nombre_archivoventas)
                            try: folio=ventas[-1][0]+1
                            except: folio=10000
                            print("ARCHIVOS CARGADOS")
                            archivoscargados=True
                            os.system("pause")
                        else:
                            print("Los archivos ya estan cargados")
                    case 2:
                        cerrarlista(nombre_archivo, ListaOpciones)
                        cerrarlista(nombre_archivoventas, ventas)
                        print("ARCHIVOS GUARDADOS")
                        os.system("pause")
                    case 3: continue
            case 5: #al salir manualmente del programa se guarda en su archivo correspondiente la lista que manejaba sus datos
               os.system("cls")
               cerrarlista(nombre_archivo, ListaOpciones)
               cerrarlista(nombre_archivoventas, ventas)
               break

            case default: #se agrega caso default parar fuera de rango, ahorrando un chequeo con if de la opcion
                os.system("cls")
                print("Opcion fuera de rango")
                os.system("pause")
    except ValueError:
        print ("Valor debe ser un entero")
            
#lista productos en caso de error manejando el programa
"""[1, '2D', 'assets', 'unidad', 5]
[2, '3D', 'assets', 'unidad', 10]
[3, '2D', 'manos', 'fijo', 200]
[4, '3D', 'manos', 'fijo', 400]
[5, '2D', 'expresiones', 'unidad', 50]
[6, '3D', 'expresiones', 'unidad', 150]
[7, '2D', 'peinados', 'unidad', 100]
[8, '3D', 'peinados', 'unidad', 250]
[9, '2D', 'traje', 'unidad', 500]
[10, '3D', 'traje', 'unidad', 1000]
"""