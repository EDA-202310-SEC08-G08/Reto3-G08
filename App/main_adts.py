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
from tabulate import tabulate
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf


class List:
    """
    A custom list class that can use different data structures and comparison functions.

    Attributes:
        list: The underlying list object from the lt module.
        datastructure: The type of data structure used for the list ("ARRAY_LIST" or "SINGLE_LINKED").
        cmpfunction: The comparison function used to sort or search the list elements.
        sorted: A boolean flag indicating whether the list is sorted or not.
        elements: A reference to the list elements (either an array or a node).
    """

    def __init__(self, datastructure="ARRAY_LIST", cmpfunction=None, adt=None, sorted=False):
        """
        Initializes a List object with the given parameters.

        Args:
            datastructure (str): A string indicating the type of data structure to use for the list ("ARRAY_LIST" or "SINGLE_LINKED"). Defaults to "ARRAY_LIST".
            cmpfunction (function): A function that takes two elements as arguments and returns a negative number if the first element is less than the second, zero if they are equal, or a positive number if the first element is greater than the second. Defaults to None.
            adt (object): An existing list object from the lt module to use as the underlying list. Defaults to None.
            sorted (bool): A boolean flag indicating whether the list is sorted or not. Defaults to False.
        """
        if adt is not None:
            self.list = adt
            self.datastructure = adt["type"]
            self.cmpfunction = adt["cmpfunction"]
            self.sorted = sorted
            if self.datastructure == "ARRAY_LIST":
                self.elements = adt["elements"]
            else:
                self.elements = adt["first"]
        else:
            self.list = lt.newList(datastructure, cmpfunction)
            self.datastructure = datastructure
            self.cmpfunction = cmpfunction
            self.sorted = sorted
            if self.datastructure == "ARRAY_LIST":
                self.elements = self.list["elements"]
            else:
                self.elements = self.list["first"]

    def __str__(self) -> str:
        """
        Returns a string representation of the list.

        Returns:
            A string containing the list elements.
        """
        if self.datastructure == "ARRAY_LIST":
            return str(self.elements)
        else:
            return str(self.list["first"])

    def __len__(self) -> int:
        """
        Returns the number of elements in the list.

        Returns:
            An integer representing the size of the list.
        """
        return lt.size(self.list)

    def __iter__(self):
        """
        Returns an iterator over the list elements.

        Returns:
            An iterator object that can be used in a for loop or with next().
        """
        return lt.iterator(self.list)

    def __type__(self):
        """
        Returns a string describing the type of the list.

        Returns:
            A string containing the ADT name and the data structure name.
        """
        return f"ADT : list , Datastructure: {self.datastructure}"

    def addFirst(self, element):
        """
        Adds an element at the beginning of the list.

        Args:
            element: The element to be added to the list.

        Raises:
            Exception: If there is no space left in the list (only for array lists).
        """
        lt.addFirst(self.list, element)

    def addLast(self, element):
        """
        Adds an element at the end of the list.

        Args:
            element: The element to be added to the list.

        Raises:
            Exception: If there is no space left in the list (only for array lists).
        """
        lt.addLast(self.list, element)

    def isEmpty(self) -> bool:
        """
        Checks if the list is empty or not.

        Returns:
            True if the list has no elements, False otherwise.
        """
        return lt.isEmpty(self.list)

    def size(self) -> int:
        """
        Returns the number of elements in the list.

        Returns:
            An integer representing the size of the list.
        """
        return lt.size(self.list)

    def firstElement(self):
        """
        Returns the first element of the list.

        Returns:
            The element at the first position of the list, or None if the list is empty.
        """
        return lt.firstElement(self.list)

    def lastElement(self):
        """
        Returns the last element of the list.

        Returns:
            The element at the last position of the list, or None if the list is empty.
        """
        return lt.lastElement(self.list)

    def getElement(self, pos):
        """
        Returns the element at a given position of the list.

        Args:
            pos (int): An integer between 1 and the size of the list, indicating the position of the element to be returned.

        Returns:
            The element at the specified position of the list.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list).
        """
        return lt.getElement(self.list, pos)

    def deleteElement(self, pos):
        """
        Deletes and returns the element at a given position of the list.

        Args:
            pos (int): An integer between 1 and the size of the list, indicating the position of the element to be deleted.

        Returns:
            The element that was deleted from the list, or None if the position is invalid.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list).
        """
        return lt.deleteElement(self.list, pos)

    def removeFirst(self):
        """
        Removes and returns the first element of the list.

        Returns:
            The element that was removed from the list, or None if the list is empty.
        """
        return lt.removeFirst(self.list)

    def removeLast(self):
        """
        Removes and returns the last element of the list.

        Returns:
            The element that was removed from the list, or None if the list is empty.
        """
        return lt.removeLast(self.list)

    def insertElement(self, element, pos):
        """
        Inserts an element at a given position of the list.

        Args:
            element: The element to be inserted.
            pos (int): An integer between 1 and the size of the list + 1, indicating the position where the element will be inserted.

        Returns:
            True if the element was inserted successfully, False otherwise.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list + 1).
        """
        return lt.insertElement(self.list, element, pos)

    def isPresent(self, element):
        """
        Checks whether an element is present in the list.

        Args:
            element: The element to be searched for.

        Returns:
            True if the element is present in the list, False otherwise.
        """
        return lt.isPresent(self.list, element)

    def exchange(self, pos1, pos2):
        """
        Exchanges the elements at two positions in the list.

        Args:
            pos1 (int): The position of the first element to be exchanged.
            pos2 (int): The position of the second element to be exchanged.

        Raises:
            IndexError: If either position is out of range (less than 1 or greater than the size of the list).
        """
        return lt.exchange(self.list, pos1, pos2)

    def changeInfo(self, pos, element):
        """
        Changes the value of an element in the list.

        Args:
            pos (int): The position of the element to be changed.
            element: The new value of the element.

        Raises:
            IndexError: If the position is out of range (less than 1 or greater than the size of the list).
        """
        return

    def subList(self, pos1, numElements):
        """
        Returns a new list that contains a portion of the original list.
        Args:
            pos1: the initial position of the sublist.
            numElements: the number of elements of the sublist.
        Returns:
            A new List object representing the sublist.
        """
        sub_list = lt.subList(self.list, pos1, numElements)

        sub_list = List(adt=sub_list)

        return sub_list

    def iterator(self):
        """
        Return the iterator for the list.
        """
        return lt.iterator(self.list)

    def sort(self, sort_criteria=None):
        """
        Sort the list.
        Args:
            sort_criteria: the criteria used to sort the list
        Returns:
            The sorted list or an error message if no sort criteria is specified.
        """
        if sort_criteria is None:
            return "No se ha especificado un criterio de ordenamiento"

        sorted_list = merg.sort(self.list, sort_criteria)

        self.sorted = True

        return sorted_list

    def isSorted(func):
        """
        Decorator that checks if the list is sorted before running a search method.
        Args:
            func: the function being decorated
        Returns:
            The decorated function.
        """

        def decorator(self, *args):

            if self.sorted:

                return func(self, *args)

            else:

                return "La lista no esta ordenada"

        return decorator

    @isSorted
    def linealSearch(self, element):
        """
        Perform a linear search on the list.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the element if found, None otherwise.
        """
        pos = None
        while pos == None:
            for list_element in self.list:
                if lt.getElement(self.list, pos) == element:
                    pos = pos
                    break
            element += 1
        return pos

    @isSorted
    def binarySearch(self, element):
        """
        Perform a binary search on the list.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the element if found, -1 otherwise.
        """
        # inicializar i en el inicio de la lista
        i = 0
        # inicializar f en el final de la lista
        f = lt.size(self.list)
        # inicializar pos en -1 para indicar que no se ha encontrado el elemento
        pos = -1
        # inicializar found en False
        found = False
        # mientras i sea menor o igual que f y found sea False
        while i <= f and not found:
            # calcular la posicion de la mitad entre i y f
            m = (i + f) // 2
            # si el elemento en la posicion m es igual al elemento buscado
            if lt.getElement(self.list, m) == element:
                # asignar m a pos
                pos = m
                # asignar True a found
                found = True
            # si el elemento en la posicion m es mayor que el elemento buscado
            elif lt.getElement(self.list, m) > element:
                # asignar m - 1 a f
                f = m - 1
            # si el elemento en la posicion m es menor que el elemento buscado
            else:
                # asignar m + 1 a i
                i = m + 1
        # retornar pos
        return pos

    @isSorted
    def binarySearchMin(self, element):
        """
        Find the minimum index of an element in a sorted list using binary search.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the first element in the list if there are duplicates or the element itself if there are no duplicates.
        """
        # Initialize variables
        m = 0
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        # Loop until the element is found or the list is empty
        while i <= f and not found:
            # Calculate the middle index
            m = (i + f) // 2
            # If the element is found, set the position and return
            if lt.getElement(self.list, m) == element:
                pos = m
                found = True
            # If the element is greater than the middle element, change the lower bound
            elif lt.getElement(self.list, m) > element:
                f = m - 1
            # If the element is less than the middle element, change the upper bound
            else:
                i = m + 1
        # If the element is found, find the minimum position
        if found == True:
            while lt.getElement(self.list, pos - 1) == element:
                pos -= 1
        # If the element is not found, find the position where the element should be inserted
        elif lt.getElement(self.list, m) > element:
            pos = m
            while lt.getElement(self.list, pos - 1) > element:
                pos -= 1
        return pos

    @isSorted
    def binarySearchMax(self, element):
        """
        Find the maximum index of an element in a sorted list using binary search.
        Args:
            element: the element to look for in the list.
        Returns:
            The index of the last element in the list if there are duplicates or the element itself if there are no duplicates.
        """
        m = 0
        i = 0
        f = lt.size(self.list)
        pos = -1
        found = False
        while i <= f and not found:
            m = (i + f) // 2
            # Compare the middle element with the given element
            if lt.getElement(self.list, m) == element:
                pos = m
                found = True
            # If the middle element is greater than the given element, then the element can only be present in the left subarray
            elif lt.getElement(self.list, m) > element:
                f = m - 1
            # If the middle element is smaller than the given element, then the element can only be present in the right subarray
            else:
                i = m + 1
        # If the element is found in the list, then we search for the last element in the list
        if found == True:
            while lt.getElement(self.list, pos + 1) == element:
                pos += 1
        # If the element is not in the list, then the position of the element is the position of the last smaller element
        elif lt.getElement(self.list, m) < element:
            pos = m
            while lt.getElement(self.list, pos + 1) > element:
                pos += 1
        return pos


class Stack:
    def __init__(self, datastructure="DOUBLE_LINKED") -> object:
        """
        Initializes a new stack instance, with an internal storage data structure of the specified type.

        Args:
        datastructure (str): The type of data structure to use for internal storage. Default is "DOUBLE_LINKED"
            (a doubly-linked list data structure).
        """
        self.stack = st.newStack(datastructure)
        self.datastructure = datastructure

    def __str__(self) -> str:
        """
        Returns a string representation of the elements in the stack.

        Returns:
        str: A string representation of the elements in the stack.
        """
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def __len__(self) -> int:
        """
        Returns the number of elements in the stack.

        Returns:
        int: The number of elements in the stack.
        """
        return st.size(self.stack)

    def __type__(self) -> str:
        """
        Returns a string representation of the stack's abstract data type (ADT) and internal storage data structure.

        Returns:
        str: A string representation of the stack's ADT and internal storage data structure.
        """
        return f"ADT : stack , Datastructure: {self.datastructure}"

    def elements(self) -> str:
        """
        Returns a string representation of the elements in the stack.

        Returns:
        str: A string representation of the elements in the stack.
        """
        if self.datastructure == "ARRAY_LIST":
            return str(self.stack["elements"])
        else:
            return str(self.stack["first"])

    def push(self, element):
        """
        Adds an element to the top of the stack.

        Args:
        element: The element to add to the stack.
        """
        st.push(self.stack, element)

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
        The element at the top of the stack.
        """
        return st.pop(self.stack)

    def isEmpty(self) -> bool | None:
        """
        Returns a boolean indicating whether the stack is empty or not.

        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return st.isEmpty(self.stack)

    def top(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
        The element at the top of the stack.
        """
        return st.top(self.stack)

    def size(self) -> int|None:
        """
        Returns the number of elements in the stack.

        Returns:
        int: The number of elements in the stack.
        """
        return st.size(self.stack)


class Queue:

    def __init__(self, datastructure):
        """
        Initializes a new queue instance, with an internal storage data structure of the specified type.

        Args:
        datastructure (str): The type of data structure to use for internal storage.
            (e.g. "ARRAY_LIST" for an array list data structure, "DOUBLE_LINKED" for a doubly-linked list data structure)
        """
        self.queue = qu.newQueue(datastructure)
        self.datastructure = datastructure

    def __str__(self) -> str:
        """
        Returns a string representation of the elements in the queue.

        Returns:
        str: A string representation of the elements in the queue.
        """
        if self.datastructure == "ARRAY_LIST":
            return str(self.queue["elements"])
        else:
            return str(self.queue["first"])

    def __len__(self) -> int:
        """
        Returns the number of elements in the queue.

        Returns:
        int: The number of elements in the queue.
        """
        return qu.size(self.queue)

    def __type__(self) -> str:
        """
        Returns a string representation of the queue's abstract data type (ADT) and internal storage data structure.

        Returns:
        str: A string representation of the queue's ADT and internal storage data structure.
        """
        return f"ADT : queue , Datastructure: {self.datastructure}"

    def elements(self) -> str:
        """
        Returns a string representation of the elements in the queue.

        Returns:
        str: A string representation of the elements in the queue.
        """
        if self.datastructure == "ARRAY_LIST":
            return str(self.queue["elements"])
        else:
            return str(self.queue["first"])

    def enqueue(self, element):
        """
        Adds an element to the back of the queue.

        Args:
        element: The element to add to the back of the queue.
        """
        qu.enqueue(self.queue, element)

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
        The element at the front of the queue.
        """
        return qu.dequeue(self.queue)

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
        The element at the front of the queue.
        """
        return qu.peek(self.queue)

    def isEmpty(self) -> bool | None:
        """
        Returns a boolean indicating whether the queue is empty or not.

        Returns:
        bool: True if the queue is empty, False otherwise.
        """
        return qu.isEmpty(self.queue)

    def size(self) -> int | None:
        """
        Returns the number of elements in the queue.

        Returns:
        int: The number of elements in the queue.
        """
        return qu.size(self.queue)


class HashMap:

    def __init__(self, numelements=17, maptype="CHAINING", loadfactor=4.0, cmpfunction=None):
        """
        Initializes the HashMap object, creating the map with the specified parameters.

        Args:
        numelements (int): number of elements in the map. Default is 17.
        maptype (str): the type of map to create, either 'CHAINING' (default) or 'LP'.
        loadfactor (float): the maximum load factor (elements/size) allowed. Default is 4.0.
        cmpfunction : a function used for comparing keys. None by default.

        Returns:
        None

        Attributes:
        map: the map data structure instance
        maptype: the type of map created
        loadfactor: the maximum load factor allowed
        cmpfunction: the function used for comparing keys
        """
        self.map = mp.newMap(numelements=numelements, maptype=maptype,
                             loadfactor=loadfactor, cmpfunction=cmpfunction)
        self.maptype = maptype
        self.loadfactor = loadfactor
        self.cmpfunction = cmpfunction

    def __str__(self) -> str:
        """
        Returns a string representation of the keys in the map.
        """
        return str(mp.keySet(self.map))

    def __len__(self) -> int:
        """
        Returns the number of entries in the map.
        """
        return mp.size(self.map)

    def type(self) -> str:
        """
        Returns a string representation of the ADT and datastructure.

        Returns:
        str: The string representation.
        """
        return f"ADT : map , Datastructure: {self.maptype}"

    def put(self, key, value):
        """
        Puts a key-value pair into the map.

        Parameters:
        key (str): The key to add to the map.
        value (object): The value associated with the key.

        """
        mp.put(self.map, key, value)

    def get(self, key):
        """
        Gets the value associated with the given key.

        Parameters:
        key (str): The key to search for in the map.

        Returns:
        object: The value associated with the key.
        """
        return mp.get(self.map, key)

    def remove(self, key):
        """
        Removes the key-value pair with the given key from the map.

        :param key: key of the pair to be removed
        :return: True if pair was removed successfully, False if the given key did not exist in the map
        """

        return mp.remove(self.map, key)

    def contains(self, key):
        """
        Returns True if the key is in the map, False otherwise.

        Parameters:
        key (str): The key to search for in the map.

        Returns:
        bool: True if the key is in the map, False otherwise.
        """
        return mp.contains(self.map, key)

    def isEmpty(self) -> bool:
        """
        Checks if the map object is empty.

        Returns:
        - bool: True if the map is empty, else it returns False.
        """
        return mp.isEmpty(self.map)

    def size(self) -> int:
        """
        Returns the size of the map object.

        Returns:
        - int: the size of the map object.
        """
        return mp.size(self.map)

    def keySet(self):
        """
        Gets a set of keys from the map object and returns it as a List object.

        Returns:
        - List: A List object that contains a set of keys of the map object.
        """
        keySet = mp.keySet(self.map)
        return List(adt=keySet)

    def valueSet(self):
        """
        Gets a collection of values from the map object and returns it as a List object.

        Returns:
        - List: A List object that contains a collection of values of the map object.
        """
        valueSet = mp.valueSet(self.map)
        return List(adt=valueSet)


class OrderedMap:
    """
    This class provides methods for working with ordered map data structures.

    Attributes:
    - omaptype (str): a string that represents the ordered map data structure used.
    - comparefunction (function): a user-defined function that can be used to compare keys.
    - map (OrderedMap): an OrderedMap object that represents the ordered map data structure.
    """

    def __init__(self, omaptype="RBT", comparefunction=None):
        """
        Initializes a new instance of the OrderedMap class.

        Args:
        - omaptype (str): a string that represents the ordered map data structure used.
        - comparefunction (function): a user-defined function that can be used to compare keys.
        """
        self.map = om.newMap(omaptype, comparefunction)
        self.omaptype = omaptype
        self.comparefunction = comparefunction

    def __str__(self) -> str:
        """
        Returns a string with a list of the keys in the ordered map.

        Returns:
        str: A string with a list of keys in the ordered map.
        """
        keys = om.keySet(self.map)
        keyList = List(adt=keys)
        return keyList.__str__()

    def __len__(self) -> int:
        """
        Returns the number of elements in the ordered map.

        Returns:
        int: The number of elements in the ordered map.
        """
        return om.size(self.map)

    def type(self) -> str:
        """
        Returns a string with the type of ordered map data structure used.

        Returns:
        str: A string with the type of ordered map data structure used.
        """
        return f"ADT : ordered map , Datastructure: {self.omaptype}"

    def put(self, key, value):
        """
        Inserts a key-value pair into the ordered map.

        Parameters:
        - key (str): The key to be inserted.
        - value: The value associated with the key to be inserted.
        """
        om.put(self.map, key, value)

    def get(self, key):
        """
        Gets the value associated with a key in the ordered map.

        Parameters:
        - key (str): The key to search for in the ordered map.

        Returns:
        Any: The value associated with the key searched, or None if the key does not exist.
        """
        return om.get(self.map, key)

    def remove(self, key):
        """
        Removes a key-value pair from the ordered map.

        Parameters:
        - key (str): The key to be removed.

        Returns:
        Any: The value associated with the key removed, or None if the key does not exist.
        """
        return om.remove(self.map, key)

    def contains(self, key):
        """
        Checks if a given key exists in the ordered map.

        Parameters:
        - key (str): The key to search for in the ordered map.

        Returns:
        bool: True if the key exists in the map, False otherwise.
        """
        return om.contains(self.map, key)

    def size(self) -> int:
        """
        Returns the number of elements in the ordered map.

        Returns:
        int: The number of elements in the ordered map.
        """
        return om.size(self.map)

    def isEmpty(self) -> bool:
        """
        Checks if the ordered map is empty.

        Returns:
        bool: True if the map is empty, else False.
        """
        return om.isEmpty(self.map)

    def keySet(self):
        """
        Returns a list of all keys in the map.

        Returns:
        List: A list of all keys in the map.

        """
        keySet = om.keySet(self.map)
        return List(adt=keySet)

    def valueSet(self):
        """
        Returns a list of all values in the map.

        Returns:
        List: A list of all values in the map.

        """
        valueSet = om.valueSet(self.map)
        return List(adt=valueSet)

    def minKey(self):
        """
        Returns the smallest key in the map.

        Returns:
        The smallest key in the map.

        """
        return om.minKey(self.map)

    def maxKey(self):
        """
        Returns the largest key in the map.

        Returns:
        The largest key in the map.

        """
        return om.maxKey(self.map)

    def deleteMin(self):
        """
        Deletes the entry with the smallest key in the map.

        Returns:
        The deleted entry.

        """
        return om.deleteMin(self.map)

    def deleteMax(self):
        """
        Deletes the entry with the largest key in the map.

        Returns:
        The deleted entry.

        """
        return om.deleteMax(self.map)

    def floor(self, key):
        """
        Returns the largest key in the map less than or equal to the given key.

        Args:
        key: The key to compare against.

        Returns:
        The largest key in the map less than or equal to the given key.

        """
        return om.floor(self.map, key)

    def ceiling(self, key):
        """
        Returns the smallest key in the map greater than or equal to the given key.

        Args:
        key: The key to compare against.

        Returns:
        The smallest key in the map greater than or equal to the given key.

        """
        return om.ceiling(self.map, key)

    def select(self, k):
        """
        Returns the next key to the k-th smallest key in the table.

        Args:
            map: The symbol table.
            pos: The k-th smallest key.
        Returns:
            The key that is the smallest and greater than or equal to key.
        Raises:
            Exception
        """

        return om.select(self.map, k)

    def rank(self, key) -> int:
        """
        Returns the number of keys in the table that are strictly less than the given key.
        Args:
            map: The symbol table.
            key: The key to compare.
        Returns:
            The number of keys in the table that are strictly less than the given key.
        Raises:
            Exception
        """

        return om.rank(self.map, key)

    def height(self) -> int:
        """
        Returns the height of the map.

        Returns:
        The height of the map.

        """
        return om.height(self.map)

    def keys(self, key1, key2):
        """
        Returns a list of all keys in the map between key1 and key2.

        Args:
        key1: The first key in the range.
        key2: The second key in the range.

        Returns:
        A list of all keys in the map between key1 and key2.

        """
        return List(adt=om.keys(self.map, key1, key2))

    def values(self, key1, key2):
        """
        Returns a list of all values in the map between key1 and key2.

        Args:
        key1: The first key in the range.
        key2: The second key in the range.

        Returns:
        A list of all values in the map between key1 and key2.

        """
        return List(adt=om.values(self.map, key1, key2))
