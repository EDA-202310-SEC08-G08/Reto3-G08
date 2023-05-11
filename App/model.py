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


import calendar
from datetime import datetime as dt
from prettytable import PrettyTable as ptbl
import config as cf
import main_adts as adt
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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de Objetos
#Testing New Things 

class Accident():

    def __init__(self, data):
        self.formulario = data["FORMULARIO"]
        self.codigo_accidente = data["CODIGO_ACCIDENTE"]
        self.fecha_ocurrencia = dt.strptime(
            data["FECHA_OCURRENCIA_ACC"], '%Y/%m/%d')
        self.hora_ocurrencia = dt.strptime(
            data["HORA_OCURRENCIA_ACC"], '%H:%M:%S')
        self.dia_ocurrencia = data["DIA_OCURRENCIA_ACC"]
        self.mes_ocurrencia = data["MES_OCURRENCIA_ACC"]
        self.ano_ocurrencia = data["ANO_OCURRENCIA_ACC"]
        self.direccion = data["DIRECCION"]
        self.gravedad = data["GRAVEDAD"]
        self.clase = data["CLASE_ACC"]
        self.localidad = data["LOCALIDAD"]
        self.fecha_hora = dt.strptime(
            data["FECHA_HORA_ACC"][:-3], '%Y/%m/%d %H:%M:%S')
        self.latitud = data["LATITUD"]
        self.longitud = data["LONGITUD"]


class GroupClass():

    def __init__(self, clase):
        self.clase = clase
        self.accidents = 0
        self.all_data = adt.List(
            datastructure='ARRAY_LIST', cmpfunction=compareDates)
        self.map_accidents = adt.OrderedMap(
            omaptype='RBT', comparefunction=compareDates)


class Day():

    def __init__(self, day):
        self.day = day
        self.accidents = 0
        self.map_accidents = adt.OrderedMap(
            omaptype='RBT', comparefunction=compareDates)


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
    data_structs["map_accidents"] = adt.HashMap(
        maptype="PROBING", loadfactor=0.5, cmpfunction=cmp_by_class, numelements=7)  # type: ignore

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
    # TODO: Crear la función para agregar elementos a una lista

    om.put(data_structs["all_data"], data["CODIGO_ACCIDENTE"], data)
    addAccident(data_structs, data)

    return data_structs


def addAccident(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    accident = Accident(data)
    map_accidents = data_structs["map_accidents"]
    if map_accidents.contains(accident.clase):
        group = map_accidents.get(accident.clase)
        group = me.getValue(group)
        group.accidents += 1
        group.all_data.addLast(accident)
        addDay(group, accident)
    else:
        group = GroupClass(accident.clase)
        group.accidents += 1
        addDay(group, accident)
        map_accidents.put(accident.clase, group)

    return data_structs


def addDay(group: GroupClass, data: Accident):
    """
    Función para agregar nuevos elementos a la lista
    """

    if group.map_accidents.contains(data.fecha_ocurrencia):
        day = group.map_accidents.get(data.fecha_ocurrencia)
        day = me.getValue(day)
        day.accidents += 1
        day.map_accidents.put(data.hora_ocurrencia, data)
    else:
        day = Day(data.fecha_ocurrencia)
        day.accidents += 1
        day.map_accidents.put(data.hora_ocurrencia, data)
        group.map_accidents.put(data.fecha_ocurrencia, day)

    return group

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
    # TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    # TODO: Crear la función para obtener el tamaño de una lista
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


def req_3(data_structs, calle, clase_accidente):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3

    heap_solution = mpq.newMinPQ(cmpfunction=compareDatesHeap)
    list_solution = adt.List(datastructure='ARRAY_LIST',
                             cmpfunction=compareDatesHeap)
    map_class = data_structs["map_accidents"]
    iterable_data = map_class.get(clase_accidente)
    iterable_data = me.getValue(iterable_data)
    iterable_data = iterable_data.all_data

    for accident in iterable_data:
        if calle in accident.direccion:
            mpq.insert(heap_solution, accident)
    numelements = mpq.size(heap_solution)
    for i in range(3):
        accident = mpq.delMin(heap_solution)
        list_solution.addLast(accident)

    return list_solution, numelements


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


def req_7_sort_criteria(data1, data2):
    return not req_5_sort_criteria(data1, data2)


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(año, mes, data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    acc = lt.newList()
    dias = calendar.monthrange(año, mes)[1]
    accs = om.newMap()

    for accidente in lt.iterator(om.valueSet(data_structs)):
        if int(accidente['ANO_OCURRENCIA_ACC']) == año and accidente["MES_OCURRENCIA_ACC"] == mes_letras(mes):
            lt.addLast(acc, accidente)

    merg.sort(acc, req_7_sort_criteria)

    for dia in range(1, dias+1):
        aux = []
        for accidente in lt.iterator(acc):
            a, b, day = accidente['FECHA_OCURRENCIA_ACC'].split("/")
            day = int(day)
            if day == dia:
                aux.append(accidente)
        om.put(accs, dia, aux)

    return accs


def mes_letras(mes):
    months = ['ENERO',
              'FEBRERO',
              'MARZO',
              'AVRIL',
              'MAYO',
              'JUNIO',
              'JULIO',
              'AGOSTO',
              'SEPTIEMBRE',
              'OCTUBRE',
              'NOVIEMBRE',
              'DICIEMBRE']
    return months[mes-1]


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compareDates(date1, date2):
    """
    Función que compara dos fechas
    """
    if date1 == date2:
        return 0
    elif date1 > date2:
        return 1
    else:
        return -1


def compareDatesHeap(acc1: Accident, acc2: Accident):

    return acc1.fecha_hora < acc2.fecha_hora


def cmp_by_class(class1, class2):
    class_entry = me.getKey(class2)
    if class_entry == class1:
        return 0
    elif class1 > class_entry:
        return 1
    else:
        return -1


# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    # TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    # TODO: Crear función de ordenamiento
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
