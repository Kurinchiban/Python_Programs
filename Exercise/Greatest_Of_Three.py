
from audioop import reverse


def Greatestofthree(list):
    blank_list=[None,None,None]
    for num in list:
        """creating the new function and passing the blank 
        list and the values in the list(iterable)"""
        bestofthree(blank_list,num)
    return blank_list 

def bestofthree(blank_list,num):
    #Three test cases
    """Test case will pass when blanklist value is None or 
     blanklist value is lesser than the values in the list"""
    if blank_list[2] is None or blank_list[2]<num:
        """creating the function to shift the 
         values if the test case is passed""" 
        shiftvalues(blank_list,num,2)
    elif blank_list[1] is None or blank_list[1]<num:
        shiftvalues(blank_list,num,1)
    elif blank_list[0] is None or blank_list[0]<num:
        shiftvalues(blank_list,num,0)

def shiftvalues(blank_list,num,index):
    """Itrating the values of blank_list at 0 so we
     are adding the extra index in range value so that
      we can reach the 2 index
    """
    for i in range(index+1):
        # if condition is to assign the value
        if i==index:
            blank_list[i]=num 
        else:
            """This else part to change the values 
            inside the blanklist then only we can the
             max of three""" 
            blank_list[i]=blank_list[i+1]

def got(list):
    a=sorted(list,reverse=True)
    return a[:3]


def second_largest(list):
    a=max(list)
    list_1=list.remove(a)
    b=max(list_1)
    return b

list=[5,4,3,7,8,9]
print(Greatestofthree(list))
print(got(list))
print(second_largest(list))