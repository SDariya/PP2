#Sets
#[arn]
import re

txt = "The sun is shining in United Kingdom"
x = re.findall("[arn]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[a-n]
import re

txt = "The sun is shining in United Kingdom"
x = re.findall("[a-n]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[^arn]
import re

txt = "The sun is shining in United Kingdom"
x = re.findall("[^arn]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[1234]
import re

txt = "The sun is shining in United Kingdom"
x = re.findall("[1234]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[0-9]
import re

txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[0-5][0-9]
import re

txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[a-zA-Z]
import re

txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#[+]
import re

txt = "8 times before 11:45 AM"
x = re.findall("[+]", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#2
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#3
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#4
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

#5
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#6
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#7
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#8
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#9
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#10
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

#11
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#12
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#13
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())




