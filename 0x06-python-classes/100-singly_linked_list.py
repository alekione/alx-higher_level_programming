#!/usr/bin/python3
""" Node class definition """


class Node:
    """ create a node with
    attributes for data and next_node
    """

    def __init__(self, data, next_node=None):
        """ initialize object fields/variables """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """ return data object data value """
        return self.__data

    @property
    def next_node(self):
        """ return the next_node """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ sets a value of data """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ sets a value for the next_node """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" singlylinkedlist object class """


class SinglyLinkedList:
    """ class attributes """

    def __init__(self):
        """ initialize class fields """
        self.__head = None

    def sorted_insert(self, value):
        """ add a node in the list """
        node = Node(value)
        head = self.__head
        if self.__head is None:
            self.__head = node
        elif head.data >= value:
            node.next_node = self.__head
            self.__head = node
        else:
            while head.next_node is not None:
                if head.next_node.data >= value:
                    break
                head = head.next_node
            node.next_node = head.next_node
            head.next_node = node

    def __str__(self):
        """ string representation of the linked list
        This is useful during printing
        """
        string = ""
        head = self.__head
        while head is not None:
            string += str(head.data)
            if head.next_node is not None:
                string += "\n"
            head = head.next_node
        return string
