"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        self.size = self.storage.length
        return self.size

    def enqueue(self, value):
        # add to the tail,keep count, remove head, return value
        self.storage.add_to_tail(value)
        self.size = self.storage.length
        return value

    def dequeue(self):
        #remove head, keep count, return removed value
        if self.size == 0:
            return None
        removed = self.storage.head.value
        self.storage.remove_head()
        self.size = self.storage.length
        return removed
     
        
