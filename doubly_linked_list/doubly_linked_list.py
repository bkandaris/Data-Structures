"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)
        # If None
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return value
        # If one
        else:
            oldHead = self.head
            self.head = newNode
            newNode.next = oldHead
            self.length +=1
            return value

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        current_value = self.head
        # if none
        if self.length == 0:
            return None
        # if one
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return current_value.value
            # if more than one
        else:
            current_head = self.head
            # change the current head to have no stuffs
            current_head.head = None
            current_head.tail = None
            self.length -= 1
            return current_value.value

   
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode.value
        # if none
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return value
        # if one
        else:
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
            self.length +=1
            return value

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current_tail = self.tail
        # if none
        if self.length == 0:
            return None
        # if one
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return current_tail.value
        # if many
        else:
            # take what's currently the tail and boop it change values to none
            new_tail = current_tail.prev
            new_tail.next = None
            # find the new current_tail and change the values of prev, value, next 
            current_tail.prev = None
            # update current tail of DLL
            self.tail = new_tail
            self.length -= 1
            # update the length and tail value of DLL
            return new_tail.value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            return node.value
        else:
            movedNode = node
            oldHead = self.head
            toTheLeft = movedNode.prev
            toTheRight = movedNode.next
            toTheLeft.next = toTheRight
            
            self.head = movedNode
            newNode.prev = None
            newNode.next = oldHead
            oldHead.prev = 
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass