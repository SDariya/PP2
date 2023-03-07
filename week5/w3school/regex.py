#1
import re

txt = "London is the capital of Great Britain"
x = re.search("^London.*Britain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#Metacharacters
#[]
import re

txt = "London is the capital of Great Britain"

x = re.findall("[a-m]", txt)
print(x)

#\
import re

txt = "That will be cost 1458 tg"

x = re.findall("\d", txt)
print(x)

#.
import re

txt = "Hello, World"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("Wo..d", txt)
print(x)

#^
import re

txt = "Hello, World"

x = re.findall("^Hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#$
import re

txt = "Hello, World"

x = re.findall("World$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

#*
import re

txt = "Hello, World"
x = re.findall("He.*o", txt)
print(x)

#+
import re

txt = "Hello, World"
x = re.findall("He.+o", txt)
print(x)

#?
import re

txt = "Street dancers"
x = re.findall("Str.?t", txt)
print(x)

#{}
import re

txt = "Street dancers"
x = re.findall("Str.{2}t", txt)
print(x)

#|
import re

txt = "Yes, there is at least one match!"
x = re.findall("two|one", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Special Sequences
#\A
import re

txt = "The sun in Italy"
x = re.findall("\AThe", txt)

print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")

#\b
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\bing", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#\b2
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"ing\b", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\B
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\Bing", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#\B2
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"ing\B", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\d
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\d", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\D
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\D", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\s
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\s", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\S
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\S", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\w
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\w", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\W
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"\W", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#\Z
import re

txt = "The sun is shining in United Kingdom"
x = re.findall(r"Kingdom\Z", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")