"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from prettytable import PrettyTable as ptbl
from datetime import datetime as dt

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "all_data": None,
    }

    data_structs["all_data"] = om.newMap(comparefunction=cmp_by_id)

    return data_structs


def cmp_by_id(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1 > data_2:
        return 1
    elif data_1 < data_2:
        return -1
    else:
        return 0

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    om.put(data_structs["all_data"], data["CODIGO_ACCIDENTE"], data)

    return data_structs


# Funciones para creacion de datos

def new_data(info):
    """
    Crea una nueva estructura para modelar los datos
    """
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(año, mes, localidad, data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    
    acc = lt.newList()
    
    for accidente in lt.iterator(om.valueSet(data_structs)):
        if int(accidente['ANO_OCURRENCIA_ACC']) == año and accidente["MES_OCURRENCIA_ACC"] == mes and accidente["LOCALIDAD"] == localidad:
            lt.addLast(acc, accidente)
            
    merg.sort(acc, req_5_sort_criteria)
    
    size = lt.size(acc)
    if size > 10:
        acc = lt.subList(acc, 0, 10)
        
    columns = ['CODIGO_ACCIDENTE',
               'DIA_OCURRENCIA_ACC',
               'DIRECCION',
               'GRAVEDAD',
               'CLASE_ACC',
               'FECHA_HORA_ACC',
               'LATITUD',
               'LONGITUD'
               ]
    
    return tablify(acc, columns), size
            
   
   
def req_5_sort_criteria(data1, data2):
    
    
    if dt.strptime(data1["FECHA_HORA_ACC"], '%Y/%m/%d %H:%M:%S+%f') > dt.strptime(data2['FECHA_HORA_ACC'], '%Y/%m/%d %H:%M:%S+%f'):
        return True
    else:
        return False         


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def FirstandLast(list, count, columns):

    table1 = ptbl()
    table2 = ptbl()
    size = len(list)
    table1.field_names = columns
    table1.max_width = 35
    table2.field_names = columns
    table2.max_width = 35
    
    first = list[:count]
    last = list[-count:]

    for i in range(0, count):

        data = first[i]
        rows = []

        for n in range(0, len(columns)):
            rows.append(data[columns[n]])
        table1.add_row(rows)
        table1.hrules = True

    for i in range(0, count):

        data = last[i]
        rows = []

        for n in range(0, len(columns)):
            rows.append(data[columns[n]])
        table2.add_row(rows)
        table2.hrules = True

    return table1, table2

def tablify(list, columns):

    table = ptbl()
    size = lt.size(list)
    table.field_names = columns
    table.max_width = 35

    for i in range(1, size+1):

        data = lt.getElement(list, i)
        rows = []

        for n in range(0, len(columns)):
            rows.append(data[columns[n]])
        table.add_row(rows)
        table.hrules = True

    return table