class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None  

class Doubly_linked_list():
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node 
        self.tail=new_node 
        self.length=1

    # printing the double linked list
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next 
    # appending the value in doubly linked list 
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node 
        else:
            new_node.prev=self.tail 
            self.tail.next=new_node 
            self.tail=new_node
        self.length+=1 
        return True
    # pop the value in the doubly linked list 
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail 
        if self.length==1:
            self.head=None 
            self.tail=None 
        else:
            self.tail=self.tail.prev 
            self.tail.next= None
            temp.prev=None 
        self.length-=1
        return True 
    # adding the value at first of linked list 
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node 
        else:
            new_node.next=self.head 
            self.head=self.head.prev 
            self.head=new_node 
        self.length+=1 
        return True
    # Removing the value at first 
    def pop_first(self):
        if self.length==0:
            return None 
        temp=self.head 
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next 
            temp.next=None 
            self.head.prev=None 
        self.length-=1 
        return True 
    # seting the value 
    def get(self,index):
        if (index<0 or index>self.length):
            return None 
        temp=self.head 
        if index<self.length/2:
            for _ in range (index):
                temp=temp.next 
        else:
            temp=self.tail 
            for _ in range(self.length-1,index,-1):
                temp=temp.prev 
        return temp
    # geting or changing the value 
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value 
            return True 
        return False 
    # inserting the value at the middle 
    def insert(self,index,value):
        if (index<0 or index>self.length):
            return None  
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        before=self.get(index-1)
        after=before.next
        before.next=new_node 
        after.prev=new_node 
        new_node.next=after 
        new_node.prev=before
        self.length+=1 
        return True
    # Removing the node form the list
    def remove(self,index):
        if (index<0 or index>=self.length):
            return None  
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        before=self.get(index-1)
        after=before.next
        before.next=temp.next
        after.prev=temp.prev 
        temp.next=None 
        temp.prev=None
        self.length-=1
        return True
        


New_doubly_linked_list=Doubly_linked_list(1)
New_doubly_linked_list.append(2)
New_doubly_linked_list.append(3)
New_doubly_linked_list.append(4)
#New_doubly_linked_list.pop()
#New_doubly_linked_list.pop()
#New_doubly_linked_list.prepend(0)
#New_doubly_linked_list.pop_first()
#New_doubly_linked_list.pop_first()
#print(New_doubly_linked_list.set(3))
#New_doubly_linked_list.insert(1,100)
#New_doubly_linked_list.insert(3,200)
#New_doubly_linked_list.remove(1)
New_doubly_linked_list.print_list()

