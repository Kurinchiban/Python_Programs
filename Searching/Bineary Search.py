"""
# method 1

list_1=[22,34,45,67,78,89,99]
a=int(input("Enter the number : "))
mid=len(list_1)//2
good=True
while good==True:
    if list_1[mid]==a:
        print(f"{a} is present in the position of {mid}")
        good=False
    elif list_1[mid]>a:
        mid=mid-1
    elif list_1[mid]<a:
        mid=mid+1

"""

#method 2

def binearySearch(arr,n):
    L=0
    H=len(arr)-1
    while L<=H:
        mid=(L+H)//2
        if arr[mid]==n:
            return f"{n} is present in the position of {mid+1}"
        else:
            if arr[mid]<n:
                L=mid +1
            else:
                H=mid-1
            
a=int(input("enter the number to find in the list : "))
list_1=[22,34,45,67,78,89,99]
print(binearySearch(list_1,a))

