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

from stack import Stack
from queue import Queue
import sys
sys.path.append('../stack')
sys.path.append('../queue')
print(sys.path)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare target value to node.value
        # If value > node.value:
        if value >= self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node there
                self.right = BSTNode(value)
            else:  # self.right is a BSTNode
                # Do the same thing (aka recurse)
                # Insert value into node.right
                # right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value <= self.value:
            # Go Left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else:
                # Do the same thing
                # (compare, go left or right)
                # Insert value into node.left
                left_child = self.left
                left_child.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    # if the node passed in, has the same value as target we good
        if self.value == target:
            return True
        if self.value < target:
            if self.right == None:
                return False
            elif self.right.value == target:
                return True
            else:
                self.right.contains(target)
        else:
            if self.left == None:
                return False
            elif self.left.value == target:
                return True
            else:
                self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        bigger_node = self
        # keep moving right until right is none
        while bigger_node.right is not None:
            bigger_node = bigger_node.right
        return bigger_node.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn): # start here
        fn(self.value)   # hits the current node that's passed in
        if self.left is not None: # hit the left node first
            self.left.for_each(fn) # run the function (for_each) then goes back to the top and starts over
        if self.right is not None:
            self.right.for_each(fn)
        
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # lowest number is always the furthest to the left
        # base case
        # if node is None
        #recursive case
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Create a var to hold the Queue calss
        queue = Queue()
        # Add the first node to the queue
        queue.enqueue(self)
        # A while loop to iterate over the Tree
        while len(queue) != 0:
            # On enter of the queue dequeue/remove the node value from the Queue - Curr still holds the value of the node being removed
            curr = queue.dequeue()
            # print the current value
            print(curr.value)
            # Look to see if the current value has a left node
            if curr.left:
                # if it does add it to the queue and run the while loop again
                queue.enqueue(curr.left)
            # Look to see if the current value has a Right node
            if curr.right:
                # if it does add it to the queue and run the while loop again
                queue.enqueue(curr.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # use the stack class
        # start your stack with the root node
        # while loop that checks the stack size
            # use a pointer variable and keep updating it
        stack = Stack()
        stack.push(self)
        while len(stack) > 0:
            curr = stack.pop()
            print(curr.value)
            if curr.left is not None:
                stack.push(curr.left)
            if curr.right is not None:
                stack.push(curr.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

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

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
