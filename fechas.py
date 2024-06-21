from datetime import datetime
import os
def mostrar_folio(venta): #muestra la venta
    print(f"FOLIO: {venta[0]} FECHA: {venta[1]} ID PRODUCTO: {venta[2]} CANTIDAD: {venta[3]} PRECIO TOTAL: {venta[4]}")

def verificar_fecha(fecha):
    fecha=fecha.strip()
    if len(fecha)!=10: return False #cantidad de letras
    listafechas=fecha.split("-")
    try:
        dia=int(listafechas[0])
        mes=int(listafechas[1])
        anio=int(listafechas[2])
    except ValueError: return False #maneja error de str a int
    if len(listafechas)!=3: return False
    if not 0<dia<=31: return False #dia
    if not 0<mes<=12: return False #mes
    if not 2000<anio: return False #año
    if mes==2:
        if anio%4==0:
            if dia>29: return False #bisiesto
        if dia>28: return False #febrero
    return True

def intervalo_ventas(listaventas, fecha_inicio, fecha_fin): #crea una lista de las ventas entre cada fecha
    filtro = []
    total=0
    if verificar_fecha(fecha_inicio) and verificar_fecha(fecha_fin):
        for venta in listaventas:
            fecha_venta=datetime.strptime(venta[1],'%d-%m-%Y')
            inicio=datetime.strptime(fecha_inicio,'%d-%m-%Y')
            final=datetime.strptime(fecha_fin,'%d-%m-%Y')
            if inicio <= fecha_venta <= final:
                filtro.append(venta)
        for mostrar in filtro: #las muestra usando la funcion de arriba
            mostrar_folio(mostrar)
            total=total+mostrar[4]
        print("TOTAL VENDIDO=",total) #termina mostrando el total vendido
    else: print("ERROR EN LA FECHA")



def fechafija(listaventas, fecha): #se busca en fecha exacta, comprueba si lo ingresado es equivalente a lo guardado y muestra
    total=0
    if verificar_fecha(fecha):
        for venta in listaventas:
            if venta[1]==fecha:
                mostrar_folio(venta)
                total=total+venta[4]
        print("TOTAL VENDIDO=",total)
    else: print("ERROR EN LA FECHA")


def todas_fechas(listaventas): #muestra todos los folios guardados, no hace ninguna discriminacion
    total=0
    for venta in listaventas:
        mostrar_folio(venta)
        total=total+venta[4]
    print("TOTAL VENDIDO=",total)