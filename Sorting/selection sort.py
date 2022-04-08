# Creating thr function for the selsection sort
def selectionsort(list):
    #Itrating the value form the front order (0,1,2,3,4,5)
    for i in range(len(list)-1):
        #creating the min value and assigning the index value
        min_index=i
        #Itrating the next index of i
        for j in range(i+1,len(list)):
            #comparing the value to the next value
            if list[min_index]>list[j]:
                min_index=j 
        if min_index!=i:
            #tranfer the values
            temp=list[i]
            list[i]=list[min_index]
            list[min_index]=temp
    return list 

#Calling the function 
print(selectionsort([4,3,5,2,6,1]))
