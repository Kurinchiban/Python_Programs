"""
"r"-open file for reading (default mode)
"w"-used for writing even the file is not exist
"x"-create file if not exists
"a"-(append) add more content ath the end
"t"-text mode (default mode)
"b"-binary mode 
"+"-read and write
"""
f=open("file.txt","r")
content=f.read() # (arguments - no of charcter)
print(content)

"""By using the readline() we can iterate through line by line""" 
f=open("file.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())

for line in content: # print character by character
    print(line)


with open("file.txt") as f:
    content=f.read()
    print(content)
    
f=open("file.txt","r")
print(f.readlines()) # using this keword we convert the lines int a list"

# creating the new file closed we cannot use it again then it will overwrite 

f=open("new.txt","w")
f.write("hellow i am kumar!\n")
f.write("working in python")
f.close()

#instead of overwriting we can use append mode

f=open("new.txt","a")
f.write("\ngood guy")
f.close()

# tell()-function is used to tell where is our pointer
# seek()-function is used to where our pointer have to start from that point

f=open("file.txt","r")
print(f.tell())
print(f.readline())
f.seek(12)
print(f.readline())
print(f.tell())
f.close()