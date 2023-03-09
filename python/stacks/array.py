# Array implementation of the Stack data structure
import sys
sys.path.append('../')
from config.config import bcolors

class Stack:
    top = -1
    arr = []
    size = 0

    def __init__(self, size):
        self.size = size
        self.arr = [None] * size

    def isEmpty(self):
        return self.top == -1

    def push(self, data):
        if self.top == self.size - 1:
            print(f"\n{bcolors.WARNING}Stack Overflow{bcolors.ENDC}\n")
        else:
            self.top += 1
            self.arr[self.top] = data

    def pop(self):  
        if self.isEmpty():
            print(f"\n{bcolors.WARNING}Stack Underflow{bcolors.ENDC}\n")
        else:
            retval = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return retval
    
    def peek(self):
        if self.isEmpty():
            print(f"\n{bcolors.WARNING}Stack is empty{bcolors.ENDC}\n")
        else:
            print(self.arr[self.top])
    
    def display(self):
        if self.isEmpty():
            print(f"{bcolors.WARNING}Stack is empty{bcolors.ENDC}")
        else:
            for i in range(self.top, -1, -1):
                print(self.arr[i])
