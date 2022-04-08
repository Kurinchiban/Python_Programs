# ceating the function for the Merge 
def merge(left_list,right_list):
    combind=[]
    i=0
    j=0
    while ((i<(len(left_list))) and (j<(len(right_list)))):
        if (left_list[i]<right_list[j]):
            combind.append(left_list[i])
            i+=1
        else:
            combind.append(right_list[j])
            j+=1
    while (i<len(left_list)):
        combind.append(left_list[i])
        i+=1 
    while (j<len(right_list)):
        combind.append(right_list[j])
        j+=1
    return combind
# creating the function for the Merge sort
def mergesort(my_list):
    if len(my_list)==1:
        return my_list
    mid=int(len(my_list)/2)
    left=my_list[mid:]
    right=my_list[:mid]
    #using the recursion 
    return merge(mergesort(left),mergesort(right))

#Calling the function 
#merge sort can be done only if we have sorted values
print(mergesort([3,4,1,2,45,55]))
    

