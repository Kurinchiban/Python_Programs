#Craeting the swaping function
from ast import Return
def swap(my_list,index1,index2):
    temp=my_list[index1]
    my_list[index1]=my_list[index2]
    my_list[index2]=temp 
    
#Creating the function to find the pivot_index where the left index value have smaller values and the right_index cvalue have the higher value
def pivot(my_list,pivot_index,end_index):
    swap_index=pivot_index
    for i in range(pivot_index+1,end_index+1):
        if my_list[i]<my_list[pivot_index]:
            swap_index+=1
            swap(my_list,swap_index,i)
    swap(my_list,pivot_index,swap_index)
    return swap_index
#Creating the function to sort the values in the list 
def quick_sort_helper(my_list,left,right):
    if left<right:
        #Calling the pivot function to find the pivot point
        pivot_index=pivot(my_list,left,right)
        quick_sort_helper(my_list,left,pivot_index-1)
        quick_sort_helper(my_list,pivot_index+1,right)
    return my_list 
#creating the function that gives the (list,first_index,last_index)    
def quick_sort(my_list):
    #calling the quick_sort_helper function
    return quick_sort_helper(my_list,0,len(my_list)-1) 

#calling the function
print(quick_sort([4,6,1,7,3,2,5]))
