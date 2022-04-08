# Driven code 
#craeting the node class 
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
#creating the class for binary Tree 
class Binary_Tree:
    def __init__(self):
        self.root=None 
    #inserting the value in the tree 
    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node 
            return True 
        temp=self.root 
        while (True):
            if new_node.value==temp.value:
                return False 
            if new_node.value<temp.value:
                if temp.left is None: 
                    temp.left=new_node 
                    return True 
                temp =temp.left 
            else:
                if temp.right is None: 
                    temp.right=new_node 
                    return True 
                temp =temp.right  
    #Contains the value in the tree 
    def contain(self,value):
        if self.root==None:
            return False
        temp=self.root 
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            if value>temp.value:
                temp=temp.right
            else:
                return True
        return False  
    #Removing the value for the tree
    def deleteNode(self, current_node, value):
        if current_node == None: 
            return None
        elif value < current_node.value:
            current_node.left = self.deleteNode(current_node.left, value)
        elif value > current_node.value: 
            current_node.right = self.deleteNode(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                current_node = None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                temp = self.minimum_value(current_node.right)
                current_node.value = temp.value
                current_node.right = self.deleteNode(current_node.right, temp.value)
        return current_node

    #Finding the Minimum Value 
    def minimum_value(self,current_node):
        while current_node.left is not None:
            current_node=current_node.left 
        return current_node.value 
    #Finding the maximum Value 
    def maximum_value(self,current_node):
        while current_node.right is not None:
            current_node=current_node.right 
        return current_node.value
    
    #Breath first search 
    def BFS(self):
        current_Node=self.root
        queue=[]
        results=[]
        queue.append(current_Node)
        while(len(queue)>0):
            current_Node=queue.pop(0)
            results.append(current_Node.value) 
            if current_Node.left is not None:
                queue.append(current_Node.left)
            if current_Node.right is not None:
                queue.append(current_Node.right)
        return results
    #creating the function for the depth first search preorder
    def DFS_preorder(self):
        results=[]
        current_Node=self.root
        def trasverse(current_Node):
            results.append(current_Node.value)
            if current_Node.left is not None:
                trasverse(current_Node.left)
            if current_Node.right is not None:
                trasverse(current_Node.right)
        trasverse(self.root)
        return results
    #creating the function for the depth first search postorder
    def DFS_postorder(self):
        results=[]
        current_Node=self.root
        def trasverse(current_Node):
            if current_Node.left is not None:
                trasverse(current_Node.left)
            if current_Node.right is not None:
                trasverse(current_Node.right)
            results.append(current_Node.value)
        trasverse(self.root)
        return results
    #creating the function for the depth first search inorder (incresing order)
    def DFS_inorder(self):
        results=[]
        current_Node=self.root
        def trasverse(current_Node):
            if current_Node.left is not None:
                trasverse(current_Node.left)
            results.append(current_Node.value)
            if current_Node.right is not None:
                trasverse(current_Node.right)
        trasverse(self.root)
        return results


My_Tree=Binary_Tree()
My_Tree.insert(47)
My_Tree.insert(21)
My_Tree.insert(18)
My_Tree.insert(27)
My_Tree.insert(7)
My_Tree.insert(28)
My_Tree.insert(76)
My_Tree.insert(52)
My_Tree.insert(82)
print(My_Tree.deleteNode(My_Tree.root,7))
#print(My_Tree.contain(2))
#print(My_Tree.contain(3))
#print(My_Tree.contain(100))
#print(My_Tree.root.value)
#print(My_Tree.root.right.value)
#print(My_Tree.root.left.value)
#print(My_Tree.maximum_value(My_Tree.root))
print(My_Tree.BFS())
print(My_Tree.DFS_preorder())
print(My_Tree.DFS_postorder())
print(My_Tree.DFS_inorder())
