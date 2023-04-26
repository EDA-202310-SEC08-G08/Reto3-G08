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
 """

import config as cf
import model
import time
import csv
import tracemalloc
from DISClib.ADT import orderedmap as om


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_data_structs()
    


# Funciones para la carga de datosom
def load_data(control, filename):
    """
    Carga los datos del reto
    """
    path = cf.data_dir +f"siniestros/datos_siniestralidad-{filename}.csv"
    file=csv.DictReader(open(path, encoding="utf-8"))
    for siniestro in file:
        load_fecha(control["fechas"], siniestro)
        

def load_fecha(arbol, siniestro:dict):
    llave=siniestro.get("FECHA_OCURRENCIA_ACC").replace(" ","")+" "+siniestro.get("HORA_OCURRENCIA_ACC").replace(" ","")+" "+siniestro.get("DIRECCION")
    om.put(arbol, llave, siniestro)



# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, inicio, fin):
    """
    Retorna el resultado del requerimiento 1
    """
    return model.req_1(control["fechas"], inicio, fin)


def req_2(control,interv1, interv2, inicio, fin):
    """
    Retorna el resultado del requerimiento 2
    """
    return model.req_2(control["fechas"], interv1, interv2, inicio, fin)



def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control, inicio, fin, gravedad):
    """
    Retorna el resultado del requerimiento 4
    """
    return model.req_4(control["fechas"], inicio, fin, gravedad)


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control, interv1, interv2, lat, long, rad, n_acc):
    """
    Retorna el resultado del requerimiento 6
    """
    return model.req_6(control["fechas"], interv1, interv2, lat, long, rad, n_acc)


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
