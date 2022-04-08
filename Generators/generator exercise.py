"""
f=open("new_file.txt","w")
f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
f.close() 
"""

def open_folder_yield(string):
    with open ("new_file.txt") as a:
        list_1=[]
        count=0
        for word in a:
            numbers=word.split(" ")
            for i in numbers:
                if i==string:
                    count+=1
                    yield ("{}:{}".format(string,count))
    

def open_folder_return(string):
    with open ("new_file.txt") as a:
        list_1=[]
        count=0
        for word in a:
            numbers=word.split(" ")
            for i in numbers:
                if i==string:
                    count+=1
        return count

a=open_folder_yield("Lorem")
try:
  for _ in range(5):
    print(a.next())
except:
  print("An exception occurred")

b=open_folder_return("Lorem")
print ("count :{}".format(b))

