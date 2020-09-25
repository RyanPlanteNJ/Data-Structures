"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
        # elif value >= self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            found = self.left.contains(target)
        if target >= self.value:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found


   # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while(current.right):
            current = current.right
        return current.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value is None:
            pass
        else:
            fn(self.value)
            if self.left is not None:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        def traverse(n):
            if n.left:
                traverse(n.left)
            print(n.value)
            if n.right:
                traverse(n.right)
        traverse(self)
        return



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)
        while queue.len() > 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            temp = stack.pop()
            print(temp.value)
            if temp.left:
                stack.push(temp.left)
            if temp.right:
                stack.push(temp.right)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass
    #
    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
