#Driven code
class Node():
    def __init__(self,value):
        self.value=value 
        self.next=None 
#creating the stack class 
class Stack():
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1 

    #printing the values
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next 
    #pushing an item to the linked list
    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node 
        else:
            new_node.next=self.top 
            self.top=new_node 
        self.height+=1 
        return True 
    #deleting the element to the linked_list 
    def pop(self):
        if self.height==0:
            return None 
        if self.height==1:
            self.top=None 
        temp=self.top 
        self.top=self.top.next
        temp.next=None
        self.height-=1
        return True

#Driver Code                
Newstack=Stack(1)
Newstack.push(2)
Newstack.push(3)
Newstack.pop()
Newstack.pop()
Newstack.print_stack()
