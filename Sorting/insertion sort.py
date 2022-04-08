#Creating the function for the insertion sort 
def insertionsort(list):
    #Itrating the value for front order(1,2,3,4,5)
    for i in range(1,len(list)):
        temp=list[i]
        # Assigning the befor index of i to the j
        j=i-1
        # Comparing the last value with the currentvalue and adding the special condition 
        while temp < list[j] and j>-1:
            list[j+1]=list[j]
            list[j]=temp
            j-=1
    return list 

#Calling the function 
print(insertionsort([3,5,6,4,2,1]))
