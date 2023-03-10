#4
'''def file_length(name):
    with open(name, 'r') as f:
        for i, l  in enumerate(f):
            pass
    return (i+1)
print("Number of lines in the file: ", file_length('C:\\Users\\asus\\Desktop\\pp2\\week6\\lines.txt'))
'''
#5
countries = ['Japan', 'Kazakhstan', 'Spain']
with open('list.txt', 'a') as a:
    for i in countries:
        a.write("\n")
        a.write(i)
text = open('list.txt')
print(text.read())

#6
import string
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.write(letter)
