# Driven code 
#Creating the node class 
class Node():
    def __init__(self,value):
        self.value=value 
        self.next=None 
# Creating the Queueu class
class Queue:
    def __init__(self,value):
        new_node= Node(value)
        self.first=new_node 
        self.last=new_node 
        self.length=1 

    # printing the Queue 
    def print_queue(self):
        temp=self.first 
        while temp is not None:
            print(temp.value)
            temp=temp.next 
    #adding the value in Queue
    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node 
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1 
        return True 
    #removing the value for the Queue
    def dequeue(self):
        if self.length==0:
            return None 
        temp=self.first
        if self.length==1:
            self.first=None 
            self.last=None 
        else:
            self.first=self.first.next 
            temp.next=None 
        self.length-=1
        return True

#Driver Code 
New_queue=Queue(1)
New_queue.enqueue(3)
New_queue.enqueue(2)
#New_queue.dequeue()
#New_queue.dequeue()
New_queue.print_queue()
