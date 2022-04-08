# Creating thr function for the bubble sort
def bubblesort(list):
    #Itrating the value form the reverse order (5,4,3,2,1)
    for i in range(len(list)-1,0,-1):
        #Itrating the value of i (5,4,3,2,1)(4,3,2,1)...
        for j in range(i):
            #comparing the value to the next value
            if list[j]>list[j+1]:
                #Trasfering the value if the value is bigger than the given
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp 
    return list 

#Calling the function 
print(bubblesort([4,2,5,6,3,1]))
