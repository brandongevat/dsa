# Singularly linked list implementation in Python
import sys
sys.path.append('../')
from config.config import bcolors   

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
    def __str__(self):
        return str(self.dataval)

class SLinkedList:
    head = None

    def __init__(self):
        self.head = None
    
    def __str__(self):
        tmp = self.head
        retval = ""
        while (tmp != None):
            retval += str(tmp.dataval) + " -> "
            tmp = tmp.nextval
        retval += "None"
        return retval
    
    def addTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.nextval:
            last = last.nextval
        last.nextval = new_node

    def addHead(self, data):
        new_node = Node(data)
        new_node.nextval = self.head
        self.head = new_node

    def removeTail(self):
        if self.head is None:
            print(f"\n{bcolors.WARNING}List is empty{bcolors.ENDC}\n")
            return
        if self.head.nextval is None:
            self.head = None
            return
        last = self.head
        while last.nextval.nextval:
            last = last.nextval
        last.nextval = None

    def removeHead(self):
        if self.head is None:
            print(f"\n{bcolors.WARNING}List is empty{bcolors.ENDC}\n")
            return
        self.head = self.head.nextval

    def remove(self, data):
        if self.head is None:
            print(f"\n{bcolors.WARNING}List is empty{bcolors.ENDC}\n")
            return
        if self.head.dataval == data:
            self.head = self.head.nextval
            return
        last = self.head
        while last.nextval:
            if last.nextval.dataval == data:
                last.nextval = last.nextval.nextval
                return
            last = last.nextval

    def search(self, data):
        if self.head is None:
            print(f"\n{bcolors.WARNING}List is empty{bcolors.ENDC}\n")
            return
        tmp = self.head
        while tmp:
            if tmp.dataval == data:
                return True
            tmp = tmp.nextval
        return False
    
    def reverse(self):
        if self.head is None:
            print(f"\n{bcolors.WARNING}List is empty{bcolors.ENDC}\n")
            return
        prev = None
        current = self.head
        while current is not None:
            next = current.nextval
            current.nextval = prev
            prev = current
            current = next
        self.head = prev