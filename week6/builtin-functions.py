#1
import math

a = [1,2,3,4,5,5]
def multiply(a):
    result = math.prod(a)
    print(result)

#2
str = " ShAripKazY"
def count(str):
    low = 0
    up = 0
    for i in range(len(str)):
        if str[i].islower():
            low += 1
        elif str[i].isupper():
            up += 1
    print("Lowercase letters: "+ low)
    print("Uppercase letters: "+up)

#3
str1 = "madam"
revstr = reversed(str1)      
print(revstr)  
if str1 == revstr:
    print("String is polidrome ")
else:
    print("String is not polidrome ")

#4
import math
import time
x = 21500
ms = 258
s = math.sqrt(x) 
def square_root(x, ms):
    time.sleep(ms/1000) 
    print("Square root of" + x + "after" + ms + " miliseconds is: " + s)

#5
x1 = (True, True, True)
r = all(x1)
print(r)


