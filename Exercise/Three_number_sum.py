
# Three number Sum

list_1=[-8,-6,1,2,3,5,6,12]
targetsum=0
triplets=[]
for i in range(len(list_1)-2):
    l=i+1 
    r=len(list_1)-1
    while l<r :
        if list_1[i]+list_1[l]+list_1[r]==targetsum:
            triplets.append([list_1[i],list_1[l],list_1[r]])
            l+=1
            r-=1
        elif list_1[i]+list_1[l]+list_1[r]<targetsum:
            l+= 1 
        elif list_1[i]+list_1[l]+list_1[r]>targetsum:
            r-=1
print(triplets)

# Four number sum 

list_1=[-8,-6,1,2,3,4,5,6,12]
targetsum=0
tetrad=[]
for i in range(1,len(list_1)-3):
    for j in range(i+1,len(list_1)-2):
        l=j+1 
        r=len(list_1)-1 
        while l<r :
            current_sum = list_1[i]+list_1[j]+list_1[l]+list_1[r]
            if current_sum==targetsum:
                tetrad.append([list_1[i]+list_1[j]+list_1[l]+list_1[r]])
                l+=1
                r-=1 
            elif current_sum<targetsum:
                l+=1
            elif current_sum>targetsum:
                r-=1
print(tetrad)
