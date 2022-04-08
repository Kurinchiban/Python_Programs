#globle and local variable

a=100         #globle variable
def number():
    a=90      #local variable 
    print(a)

print(a)
number()

#------#
#globle keyword

a=100         #globle variable
def number():
    global a  #accesing the variable for the entire program
    a=90      #local variable
    print(a)

number()
print(a)



    