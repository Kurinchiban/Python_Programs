# crating the class for Node
from multiprocessing.sharedctypes import Value
from operator import ne


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
# creating the linked list class
class Linkedlist():
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

#Newlinkedlist=Linkedlist(4)
#Newlinkedlist=Linkedlist(5)    
 
    # print the whole list
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    # append in linkedlist
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node 
            self.tail=new_node 
        else:
            self.tail.next=new_node 
            self.tail=new_node 
        self.length+=1
        
    # pop the value at the end
    def pop(self):
        if self.length==0:
            return None 
        temp=self.head 
        pre=self.head
        while (temp.next):
            pre=temp 
            temp=temp.next 
        self.tail=pre 
        self.tail.next=None 
        self.length-=1
        if self.length==0:
            self.head=None 
            self.tail=None 
    # add value in first
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node 
            self.tail=new_node 
        else:
            new_node.next=self.head 
            self.head=new_node
        self.length+=1 
    # rempve the value at first
    def pop_first(self):
        if self.length==0:
            return None 
        temp=self.head 
        self.head=self.head.next
        temp.next=None 
        self.length-=1
        if self.length==0:
            self.tail=None
    # geeting the value through index
    def get(self,index):
        if (index<0 or index>=self.length):
            return None 
        temp=self.head 
        for _  in range(index):
            temp=temp.next
        return temp
    # seting or changing the value 
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value 
            return True 
        return False 
    #inserting the value in the middel
    def insert(self,index,value):
        if (index<0 or index >=self.length):
            return None 
        if index==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next 
        temp.next=new_node 
        self.length +=1 

    # removing the value from the middle 
    def remove(self,index):
        if (index<0 or index>=self.length):
            return None 
        if index==0:
            return self.pop_first(index)
        if index==self.length:
            return self.pop(index) 
        pre=self.get(index-1)
        temp=pre.next 
        pre.next=temp.next 
        temp.next=None 
        self.length-=1 
        
    # reverse the linked list 
    def reverse(self):
        temp=self.head 
        self.head=self.tail 
        self.tail=temp 
        after=temp.next
        before=None 
        for _ in range(self.length):
            after=temp.next
            temp.next=before 
            before=temp 
            temp=after 

Newlinkedlist=Linkedlist(5) 
Newlinkedlist.append(6)        #O(1)
Newlinkedlist.append(7)        #O(1) 
Newlinkedlist.append(8)        #O(1) 
#Newlinkedlist.pop()           #O(n)
#Newlinkedlist.prepend(300)    #O(n) 
#Newlinkedlist.pop_first()     #O(1) 
#Newlinkedlist.set(1,100)      #O(n) 
#Newlinkedlist.insert(3,200)   #O(n) 
#Newlinkedlist.remove(2)       #O(n) 
#Newlinkedlist.reverse()       #O(n) 
#print(Newlinkedlist.get(1))   #O(n) 
Newlinkedlist.print_list()


