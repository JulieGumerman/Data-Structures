import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #If binary tree is empty, new value is self.value
        if self.value == None:
            self.value = value
        elif value < self.value:
            #If value is less than self.value, find spot to left
            while self.left != None:
                if self.left < value:
                    self.left = value
                else:
                    pass
                    #keep going left until you find it
        
        elif value > self.value:
            #If value is greater than self.value, find spot to right
            while self.right != None:
                if self.right > value:
                    self.right = value
                else: 
                    #keep going right until you find it

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass
        #if target is less than self.value, go left
        #if target is greater than self.value, go right

    # Return the maximum value found in the tree
    def get_max(self):
        pass
        #return the thing on the rightiest right

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass
        #go down both directions simultaneously until each has been touched

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
