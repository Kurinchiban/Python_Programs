
list=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,]
Dict={}
for i in list:
    if i in Dict:
        Dict[i]+=1 
    else:
        Dict[i]=1
print(Dict)
print(max(Dict,key=Dict.get))

########


item = [{
"item" : "1",
"features":[{"key":"value"}]
}
]
print(item[0]["features"][0])
print(item[0]["features"][0]["key"])
