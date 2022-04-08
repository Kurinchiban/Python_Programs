# creating the hash class 
class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*7 

    # seting the adress for the keys
    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)% len(self.data_map)
        return my_hash

    # printing the hash table
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)

    #seting the keys and value
    def set_items(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])
    #getting the values 
    def get_items(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1] 
        return None

New_Hashtable=HashTable()
New_Hashtable.set_items("bolts",1000)
New_Hashtable.set_items("washers",50)
New_Hashtable.set_items("lumber",100)
New_Hashtable.print_table()
print(New_Hashtable.get_items("lumber"))
print(New_Hashtable.get_items("bolts"))
print(New_Hashtable.get_items("washers"))
print(New_Hashtable.get_items("paint"))
