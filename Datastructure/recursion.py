#creating the multiple function using the recursion 
def multiple(a,b):
    if b==1:
        return a 
    return a + multiple(a,b-1)

print(multiple(10,2))

#creating the factorial function using recursion
def factorial(n):
    if n==1:
        return 1 
    return n*(factorial(n-1))
    
print(factorial(4))

#creating the fibonacci series using recursion 

def fibonaci(n):
    if n==1 or n==0:
        return n 
    return fibonaci(n-2)+fibonaci(n-1)

print(fibonaci(3))

"""
#palindrom program 
def ispalindrome(a):
    b=a[::-1]
    if a==b:
        return "palindrom"
    else:
        return "non-palindrom"

a=str(input("Enter the value : "))
print(ispalindrome(a)) 
"""

#palindome using recursion 


def is_palindrome(a):
    if len(a) == 1:
        return True
    else:
        if a[0] == a[-1]:
            return is_palindrome(a[1:-1])
        else:
            return False
            
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")