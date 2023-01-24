#variables
x=17
y="Arailym"
print(x)
print(y)


x=56       #int type
x="String" #now x is string type
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x)) #output type of variable
print(type(y))


x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)


a = 4
A = "Sally"
print(a) # a and A different variables
print(A)

#legal variables
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#illegal variables
"""
2myvar = "John"
my-var = "John"
my var = "John"   #This example will produce an error in the result
"""

#Multi Words Variable
myVariableName = "John"   #Each word, except the first, starts with a capital letter
MyVariableName = "John"    #Each word starts with a capital letter
my_variable_name = "John"   #Each word is separated by an underscore character


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output od variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

"""
x = 5
y = "John"
print(x + y)     #different type give error
"""

x = 5
y = "John"
print(x, y)     # separate them with commas, output even different types



#global variables
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()      # 


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)



x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)









