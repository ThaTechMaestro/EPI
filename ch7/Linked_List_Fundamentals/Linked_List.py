class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class SingleLinkedList:

    def __init__(self):
        self.head = None 

    
    def display_list(self):
        if self.head is None:
            print("List is empty")
            return 
        else:
            print("List is : ")
            current_node = self.head 
            while current_node:
                print(current_node.value, " ", end='')
                current_node = current_node.next
            print()
        









