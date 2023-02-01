#string
# 'hello' is the same as "hello"('' = "")
print("Hello")
print('Hello')

a = "Hello"   #we can use variable
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#string as array
a = "Hello, World!"
print(a[1])

#loop
for x in "banana":
  print(x) 

#length
a = "Hello, World!"
print(len(a))

#check
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if NOT present
txt = "The best things in life are free!"
print("expensive" not in txt)

#slicing
b = "Hello, World!"
print(b[2:5]) #output elements in range

b = "Hello, World!"
print(b[:5])   #output from the start (first index is 0)

b = "Hello, World!"
print(b[2:])   #output from the end

b = "Hello, World!"
print(b[-5:-2])    #start string from end

#modify strings
a = "Hello, World!"
print(a.upper())   #upper case

a = "Hello, World!"
print(a.lower())   #lower case

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" / remove space that not needed

a = "Hello, World!"
print(a.replace("H", "J"))    #replace elements of string

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] / split string after needed element

#string concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#складывает strings
a = "Hello"
b = "World"
c = a + b
print(c)

#string format
"""age = 36
txt = "My name is John, I am " + age
print(txt) """ #we cannot combine different types of variables

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

#escape characters
""" txt = "We are the so-called "Vikings" from the north." """
#You will get an error if you use double quotes inside a string that are surrounded by double quotes
#can be fixed by "/"
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

#Single Quote	
txt = 'It\'s alright.'
print(txt) 
#Backslash	
txt = "This will insert one \\ (backslash)."
print(txt)
#New Line	
txt = "Hello\nWorld!"
print(txt)
#Carriage Return	
txt = "Hello\rWorld!"
print(txt) 
#Tab	
txt = "Hello\tWorld!"
print(txt) 
#Backspace	
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#Octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 	
#Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 










