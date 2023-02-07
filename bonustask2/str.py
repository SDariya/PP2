#1
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

#2
print(input().count(' ') + 1)

#3
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

#4
s = input()
first = s[:s.find(' ')]
second = s[s.find(' ') + 1:]
print(second + ' ' + first)

#5
x = str(input())
i = x.find('f')
j = x.rfind('f')
if i == -1:
    print('')
elif i == j:
    print(i)
else:
    print(i, j)

#6
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
    
#7
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)

#8
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)

#9
print(input().replace('1', 'one'))

#10
s = input()
print(s.replace('@',''))

#11
s = input()
s = s.replace('h', 'H', s.count('h') - 1)
s = s.replace('H', 'h', 1)
print(s)

#12
s=input()
n=len(s)
for i in range(n):
    if i%3==0:
        s=s.replace(s[i], '3', 1)
print(s.replace('3', ''))
