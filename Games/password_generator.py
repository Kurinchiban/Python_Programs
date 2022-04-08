# Password Generator 

from re import T

import random
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="[]{}()!@#$%^&*_-=+><?/.,';:"

all=""

if upper_letters:
    all+=upper_letters 
if lower_letters:
    all+=lower_letters 
if numbers:
    all+=numbers
if symbols:
    all+=symbols 

length=1 
for i in range(length):
    password="".join(random.sample(all,10))
    print(password)
