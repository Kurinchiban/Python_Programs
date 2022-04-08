
def Linear_search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            return(f"{n} is present in the position of {i}") 
    return (f"{n} is not present in the list")
arr = [2, 3, 4, 10, 40]
n=int(input("Enter the number: "))
print(Linear_search(arr,n))