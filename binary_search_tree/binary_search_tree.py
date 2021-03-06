import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    #A node and a tree are the same! How meta is that?!?!
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.value is None:
        #     self.value = BinarySearchTree(value)
        # else:
        #     #go right if value is bigger than self.value
        #     if self.value < value:
        #         #insert if there's nothing on the right
        #         if self.right is None:
        #             self.right = BinarySearchTree(value)
        #         else: 
        #             return self.right.insert(value)
        # #go left if value is less than self.value
        #     else:
        #         if self.left is None:
        #             self.left = BinarySearchTree(value)
        #         else:
        #             return self.left.insert(value)



        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == None:
            return False
        elif self.value == target:
            return True
        #if target is less than self.value, go left
        elif self.value > target and self.left != None:
            return self.left.contains(target)
        #if target is greater than self.value, go right
        elif self.value < target and self.right != None: 
            return self.right.contains(target)
        else:
            return False        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()
        #return the thing on the rightiest right

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        #go down both directions simultaneously until each has been touched

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #left, root, right
        if node != None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)


            


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        
        while q.size != 0:
            current = q.dequeue()
            print(current.value)
            if current.right != None:
                q.enqueue(current.right)
            if current.left != None:
                q.enqueue(current.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)

        while s.size != 0:
            current = s.pop()
            print(current.value)
            if current.left != None:
                s.push(current.left)
            if current.right != None:
                s.push(current.right)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        #root, left, right
        #root
        #left subtree
        #right subtree
        if node != None:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        #left, right, root
        if node != None:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)

