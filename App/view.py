"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller as ctrl
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
import datetime
import calendar
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    return ctrl.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, size):
    """
    Carga los datos
    """
    return ctrl.load_data(control, size)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass
def convertir_mes_nombre_a_numero(mes_nombre):
    meses = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }
    return meses[mes_nombre.lower()]

def print_req_1(control, inicio, fin):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    ini=inicio
    fi=fin
    inicio+=" 00:00:00 a"
    fin+=" 23:59:59 z"
    lst = ctrl.req_1(control, inicio, fin)
    print(f"Hay {lt.size(lst)} accidentes registrados entre {ini} y {fi}")
    lstTabulate = []
    headers=["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC","LOCALIDAD","FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
    for sinis in lt.iterator(lst):
        lstTabulate.append([sinis[headers[i]] for i in range(len(headers))])
    print(tabulate(lstTabulate, headers=headers, tablefmt='grid',  numalign="right", stralign="right"))


def print_req_2(control,inicio, fin, mes:str, anio):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    if not mes.isnumeric():
        mes = convertir_mes_nombre_a_numero(mes)
    fecha = datetime.datetime(int(anio), int(mes), 1)
    ultimo_dia = calendar.monthrange(fecha.year, fecha.month)[1]
    interv1=f"{anio}/{mes}/1 {inicio}:00 a"
    interv2=f"{anio}/{mes}/{ultimo_dia} {fin}:59 z"
    lst = ctrl.req_2(control, interv1, interv2, inicio, fin)
    print(f"Hay {lt.size(lst)} accidentes en el intervalo de horas dado {inicio}:00 a {fin}:00 en el año {anio} y en el mes {mes}.")
    lstTabulate = []
    headers=["CODIGO_ACCIDENTE", "HORA_OCURRENCIA_ACC","FECHA_OCURRENCIA_ACC", "DIA_OCURRENCIA_ACC","LOCALIDAD", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LATITUD", "LONGITUD"]
    for sinis in lt.iterator(lst):
        lstTabulate.append([sinis[headers[i]] for i in range(len(headers))])
    print(tabulate(lstTabulate, headers=headers, tablefmt='grid',  numalign="right", stralign="right"))

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, inicio, fin, gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    ini=inicio
    fi=fin
    inicio+=" 00:00:00 a"
    fin+=" 23:59:59 z"
    lst = ctrl.req_4(control, inicio, fin, gravedad)
    print(f"Hay {lt.size(lst)} accidentes registrados entre las fechas {ini} 00:00:00 y {fi} 23:59:59")
    lstTabulate = []
    headers=["CODIGO_ACCIDENTE", "FECHA_HORA_ACC","DIA_OCURRENCIA_ACC", "LOCALIDAD","DIRECCION",  "CLASE_ACC","LATITUD", "LONGITUD"]
    for sinis in lt.iterator(lst):
        lstTabulate.append([sinis[headers[i]] for i in range(len(headers))])
    print(tabulate(lstTabulate, headers=headers, tablefmt='grid',  numalign="right", stralign="right"))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control, mes, anio, lat, long, rad, n_acc):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    if not mes.isnumeric():
        mes = convertir_mes_nombre_a_numero(mes)
    fecha = datetime.datetime(int(anio), int(mes), 1)
    ultimo_dia = calendar.monthrange(fecha.year, fecha.month)[1]
    interv1=f"{anio}/{mes}/1 00:00:00 a"
    interv2=f"{anio}/{mes}/{ultimo_dia} 23:59:59 z"
    lst = ctrl.req_6(control, interv1, interv2, float(lat), float(long), float(rad), int(n_acc))
    print(f"Los {lt.size(lst)} accidentes más cercanos al punto ({lat}, {long}) dentro de un radio de {rad} km para el mes de {mes} de {anio}.")
    lstTabulate = []
    headers=["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD","CLASE_ACC", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
    for sinis in lt.iterator(lst):
        lstTabulate.append([sinis[headers[i]] for i in range(len(headers))])
    print(tabulate(lstTabulate, headers=headers, tablefmt='grid',  numalign="right", stralign="right"))

def print_loader(control):
    keys = om.valueSet(control["fechas"])
    headers=["FECHA_OCURRENCIA_ACC", "FECHA_HORA_ACC", "LOCALIDAD", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LATITUD", "LONGITUD"]
    print("Total accidentes:", om.size(control["fechas"]))
    print("Total de columnas cargadas: 15")

    if lt.size(keys) < 6:
        lst=[]
        for i in lt.iterator(keys):
            lst.append([i[headers[j]] for j in range(len(headers))])
        print(tabulate(lst, headers=headers, tablefmt='grid',  numalign="right", stralign="right"))
    else:
        primeros = lt.subList(keys, 1, 3) 
        lst_prim = []
        for siniestro in lt.iterator(primeros):
            lst_prim.append([siniestro[headers[j]] for j in range(len(headers))])
        print("Los primeros tres registros de accidentes cargados fueron: ")
        print(tabulate(lst_prim, headers=headers, tablefmt='grid',  numalign="right", stralign="right"))
        ultimos = lt.subList(keys, lt.size(keys)-3, 3 )
        lst_ult = []
        for siniestro in lt.iterator(ultimos):
            lst_ult.append([siniestro[headers[j]] for j in range(len(headers))])
        print("Los últimos tres registros de accidentes cargados fueron: ")
        print(tabulate(lst_ult, headers=headers, tablefmt='grid'))

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def select(selection:str, lista:list)->(str):
    if selection.isdigit() and int(selection) >=1 and int(selection)<=len(lista):
        sizes=dict(enumerate(lista))
        return sizes[int(selection)-1]
    elif not selection.isdigit() and selection in lista:
        return selection

def print_sizes()->None:
    print("""
Digite uno de los siguientes tamaños:
1)small
2)5pct
3)10pct
4)20pct
5)30pct
6)50pct
7)80pct
8)large
""")

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                time1 = ctrl.get_time()
                print("Cargando información de los archivos ....\n")
                print_sizes()
                t_archivo=input("Digite el tamaño deseado: ").replace(" ","")
                size=select(t_archivo, ["small", "5pct","10pct","20pct", "30pct","50pct","80pct", "large"])
                if size is None:
                    print("Por favor escoga un tamaño válido")
                data = load_data(control, size)
                print_loader(control)
                time2 = ctrl.get_time()
                print(f"Tiempo de ejecución: {ctrl.delta_time(time1, time2)} ms.")
            elif int(inputs) == 2:
                time1 = ctrl.get_time() 
                print("Ingrese los intervalos en el formato año/mes/dia")
                inicio = input("Ingrese el intervalo de inicio: ").replace(" ", "")
                fin = input("Ingrese el intervalo final: ").replace(" ","")
                print_req_1(control, inicio, fin)
                time2 = ctrl.get_time()
                print(f"Tiempo de ejecución: {ctrl.delta_time(time1, time2)} ms.")
            elif int(inputs) == 3:
                time1 = ctrl.get_time()
                print("Ingrese los intervalos en el formato hora:minuto")
                inicio = input("Ingrese el intervalo de inicio: ").replace(" ", "")
                fin = input("Ingrese el intervalo final: ").replace(" ","")
                mes = input("Ingrese el mes deseado: ").replace(" ","")
                anio = input("Ingrese el año deseado: ").replace(" ","")
                print_req_2(control, inicio, fin, mes, anio)
                time2 = ctrl.get_time()
                print(f"Tiempo de ejecución: {ctrl.delta_time(time1, time2)} ms.")
            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                time1 = ctrl.get_time()
                print("Ingrese los intervalos en el formato año/mes/dia")
                inicio = input("Ingrese el intervalo de inicio: ").replace(" ", "")
                fin = input("Ingrese el intervalo final: ").replace(" ","")
                gravedad = input("Ingrese la gravedad del accidente: ").upper()
                print_req_4(control, inicio, fin, gravedad)
                time2 = ctrl.get_time()
                print(f"Tiempo de ejecución: {ctrl.delta_time(time1, time2)} ms.")

            elif int(inputs) == 6:
                print_req_5(control)
                pass

            elif int(inputs) == 7:
                time1 = ctrl.get_time()
                mes = input("Ingrese el mes deseado: ").replace(" ","")
                anio = input("Ingrese el año deseado: ").replace(" ","")
                lat = input("Ingrese la latitud: ").replace(" ","")
                long = input("Ingrese la longitud: ").replace(" ","")
                rad = input("Ingrese el radio de area en km: ").replace(" ","")
                n_acc = input("Ingrese el numero de accidentes que desea obtener: ").replace(" ","")
                print_req_6(control, mes, anio, lat, long, rad, n_acc)
                time2 = ctrl.get_time()
                print(f"Tiempo de ejecución: {ctrl.delta_time(time1, time2)} ms.")
            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)
 
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)

