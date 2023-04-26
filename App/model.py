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
import haversine
import datetime as dt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""
lat_base=0
long_base=0

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog=  {
        "fechas":om.newMap(comparefunction=delta_time)
    }
    return catalog


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
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


def req_1(data_structs, inicio, fin):
    """
    Función que soluciona el requerimiento 1
    """
    return  organizar(om.values(data_structs, inicio, fin), cmp_req1)


def req_2(data_structs, interv1, interv2, inicio, fin):
    """
    Función que soluciona el requerimiento 2
    """
    hora1=dt.datetime.strptime(inicio, '%H:%M')
    hora2=dt.datetime.strptime(fin, '%H:%M')
    lst = lt.newList()
    for value in lt.iterator( om.values(data_structs, interv1, interv2)):
        if hora1 < dt.datetime.strptime(value.get("HORA_OCURRENCIA_ACC"), '%H:%M:%S') < hora2:
            lt.addLast(lst, value)
    return organizar(lst, cmp_req1)


def req_3(data_structs, inicio, fin):
    """
    Función que soluciona el requerimiento 3
    """
    pass


def req_4(data_structs, inicio, fin, gravedad):
    """ 
    Función que soluciona el requerimiento 4
    """
    lst = lt.newList()
    for value in lt.iterator( om.values(data_structs, inicio, fin)):
        if gravedad in value.get("GRAVEDAD"):
            lt.addLast(lst, value)
    return lt.subList(organizar(lst, cmp_req1), 1, 5)



def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs, interv1, interv2, lat, long, rad, n_acc):
    """
    Función que soluciona el requerimiento 6
    """
    lst_interv=om.values(data_structs, interv1, interv2)
    ajustarlat_long(lat, long)
    lst= lt.newList()
    for value in lt.iterator(lst_interv):
        if haversine.haversine((float(value.get("LATITUD")),float(value.get("LONGITUD"))), (lat_base, long_base)) <= rad:
            print(haversine.haversine((float(value.get("LATITUD")),float(value.get("LONGITUD"))), (lat_base, long_base)))
            lt.addLast(lst, value)
    return lt.subList( organizar(lst, cmp_req6), 1, n_acc)


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


def ajustarlat_long(lat, long):
    globals()["lat_base"]=lat
    globals()["long_base"]=long

def organizar(lst, cmp):
    """
    Función encargada de ordenar la lista con los datos
    """
    return merg.sort(lst, cmp)


#cmp functions


def cmp_req1(obj1, obj2):
    if delta_time(obj1.get("FECHA_OCURRENCIA_ACC")+" "+obj1.get("HORA_OCURRENCIA_ACC"), obj2.get("FECHA_OCURRENCIA_ACC")+" "+obj2.get("HORA_OCURRENCIA_ACC")) == 1:
        return True
    else: return False

def cmp_req6(obj1, obj2):
    hav1=haversine.haversine((float(obj1.get("LATITUD")),float(obj1.get("LONGITUD"))), (lat_base, long_base))
    hav2=haversine.haversine((float(obj2.get("LATITUD")),float(obj2.get("LONGITUD"))), (lat_base, long_base))
    if hav1 < hav2:
        return True
    else:
        return False

def delta_time(time1:str, time2:str):
    date1, dir1 = separar_fecha_dir(time1)
    date2, dir2 = separar_fecha_dir(time2)
    datee1 = dt.datetime.strptime(date1, '%Y/%m/%d %H:%M:%S')
    datee2 = dt.datetime.strptime(date2, '%Y/%m/%d %H:%M:%S')
    if datee1 > datee2:
        return 1
    elif datee2 == datee1:
        if dir1 > dir2:
            return 1
        elif dir1 == dir2:
            return 0
        else:
            return -1
    else:
        return -1
    
def separar_fecha_dir(time):
    partes = time.split()
    fecha_hora = " ".join(partes[:2]) 
    direccion = " ".join(partes[2:])  
    
    return fecha_hora, direccion