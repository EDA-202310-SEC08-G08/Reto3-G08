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
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
assert cf
from tabulate import tabulate
import traceback
import calendar
import matplotlib.pyplot as plt
from datetime import datetime as dt

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
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


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


def load_data(control, suffix):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data, firstlast = controller.load_data(control, f"siniestros/datos_siniestralidad{suffix}")
    return data, firstlast


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    año = int(input("Ingrese el año entre 2015 y 2022 para el que quiere ver los accidentes recientes:"))
    mes = input("Ingrese el mes (en letras) para el que quiere ver los accidentes recientes:").upper()
    localidad = input("Ingrese la localidad de Bogotá para la que quiere ver los accidentes recientes:").upper()
    
    top10tabla, size = controller.req_5(año, mes, localidad, control)
    tam = size
    if size > 10:
        tam = 10
    print('\n####################################################################')
    print(f'Hay {size} accidentes ocurridos en la localidad de {localidad} en el mes de {mes} del año {año}.')
    print(f'Estos son los {tam} accidentes menos recientes:')
    
    print(top10tabla)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    año = int(input("Ingrese el año entre 2015 y 2022 para el que quiere ver los accidentes recientes:"))
    mes = int(input("Ingrese el mes (en números) para el que quiere ver los accidentes recientes:"))
    dias = calendar.monthrange(año, mes)[1]
    
    accidentes = controller.req_7(año, mes, control)
    
    columns = ['CODIGO_ACCIDENTE',
               'DIA_OCURRENCIA_ACC',
               'DIRECCION',
               'GRAVEDAD',
               'CLASE_ACC',
               'LOCALIDAD',
               'FECHA_HORA_ACC',
               'LATITUD',
               'LONGITUD'
               ]
    
    
    print('\n####################################################################')
    print(f'Accidentes más temprano y tardíos para el mes de {controller.mes_letras(mes)} de {año}.')
    
    data = [0]*24 
    labels = ['']*24
    for i in range(24):
        data[i] = 0
        labels[i] = str(i)+':00:00'
    tot_acc = 0
    
    for dia in range(1, dias+1):
        tot_acc += len(om.get(accidentes, dia)['value'])
        if len(om.get(accidentes, dia)['value']) > 0:
            print('\n')
            print(f'Accidentes del día {año}/{mes}/{dia}:')
            firstlast = lt.newList()
            lt.addLast(firstlast, om.get(accidentes, dia)['value'][0])
            lt.addLast(firstlast, om.get(accidentes, dia)['value'][-1])
            print(controller.tablify(firstlast, columns))
            
            for accidente in om.get(accidentes, dia)['value']:
                hora = dt.strptime(accidente["FECHA_HORA_ACC"], '%Y/%m/%d %H:%M:%S+%f').hour
                data[hora]+=1
                

    plt.hist(range(24), bins=range(24), weights=data, width=0.8)

    plt.xticks(range(len(labels)), labels, rotation='vertical')
    plt.tight_layout()

    plt.xlabel("Hora del dia")
    plt.ylabel("Número de accidentes")
    plt.title(f"Frequencia de {tot_acc} accidentes por hora del día \npara el mes de {controller.mes_letras(mes)} de {año}")

    plt.legend()
    plt.subplots_adjust(top=0.90)
    plt.subplots_adjust(bottom=0.25)
    plt.show()
    
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def printchooseCSV():
    print('\nIngrese la representación de los datos que quiere usar: ')
    print(' 1. -small')
    print(' 2. -5pct')
    print(' 3. -10pct')
    print(' 4. -20pct')
    print(' 5. -30pct')
    print(' 6. -50pct')
    print(' 7. -80pct')
    print(' 8. -large')

def fileChoose():
    """

    Da opciones al usuario para que escoja la representación de los datos de su preferencia

    Returns:

        El sufijo de la representación de los datos escogida
    """
    fileChoose = False
    while fileChoose == False:

        suffixFileChoose = input('Opción seleccionada: ')
        if int(suffixFileChoose[0]) == 1:
            suffix = '-small'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 2:
            suffix = '-5pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 3:
            suffix = '-10pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 4:
            suffix = '-20pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 5:
            suffix = '-30pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 6:
            suffix = '-50pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 7:
            suffix = '-80pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 8:
            suffix = '-large'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True

    return suffix


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
                printchooseCSV()
                suffix = fileChoose()
                print("Cargando información de los archivos ....\n")
                data, firstlast = load_data(control, suffix)
                tableFirst3, tableLast3 = controller.visual_charge_data(firstlast)
                
                print("---------------------------------------------------------------")
                print("Información de los accidentes cargados:")
                print(f"Total de accidentes: {om.size(control['model']['all_data'])}")
                print(f"Total de columnas cargadas: {len(control['model']['all_data']['root']['value'])}")
                print("---------------------------------------------------------------\n")
                
                print("Los primeros tres registros de accidentes cargados:")
                print(tableFirst3)
                print("\n")
                print("Los últimos tres registros de accidentes cargados:")
                print(tableLast3)
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                time1 = controller.get_time()
                print_req_4(control)
                time2 = controller.get_time()
                print(f"Tiempo de ejecución: {controller.delta_time(time1, time2)} ms.")

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                time1 = controller.get_time()
                print_req_7(control)
                time2 = controller.get_time()
                print(f"Tiempo de ejecución: {controller.delta_time(time1, time2)} ms.")

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
