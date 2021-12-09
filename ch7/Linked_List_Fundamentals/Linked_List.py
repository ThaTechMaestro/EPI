class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class SingleLinkedList:

    def __init__(self):
        self.head = None 

#----------------------------------------------
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
        
#----------------------------------------------  
    def count_nodes(self):
        if self.head is None:
            print('List is empty')
        else:
            number = 0
            current_node = self.head 
            while current_node:
                number+=1
                current_node=current_node.next
            print("Length of list: ", number)
    

#----------------------------------------------
    def search(self, x):
        pass
    

#----------------------------------------------
    def add_element(self, value):

        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head 
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = Node(value)


        









