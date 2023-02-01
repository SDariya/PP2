#numbers
x = 1
y = 2.8
z = 1j

print(type(x)) #int
print(type(y)) #float
print(type(z)) #complex

#int
x = 167
y = 39867562554887711
z = -323450982

print(type(x))
print(type(y))
print(type(z))

#floats
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#type conversion
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#random number
import random
print(random.randrange(1, 10))

import random
print(random.randrange(35, 60))