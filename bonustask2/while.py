#1
N=int(input())
i = 1
while (i*i <= N):
    print (i*i)
    i = i + 1

#2
N=int(input())
i = 2
while (N % i != 0):
    i += 1
print(i)

#3
n = int(input())
i = 1
while 2**i <= n:
    i += 1
print(i-1, 2**(i-1))

#4
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)

#5
n = 0
while int(input()) != 0:
    n += 1
print(n)

#6
sum = 0
i = int(input())
while i != 0:
    sum += i
    i = int(input())
print(sum)

#7
sum = 0
n = 0
x = int(input())
while x != 0:
    sum += x
    n += 1
    x = int(input())
print(sum / n)

#8
n = int(input())
max = n
while n != 0:
    if n > max:
        max = n
    n = int(input())
print(max)

#9
max = 0
i = -1
x = -1
n = 0
while x != 0:
    x = int(input())
    if x > max:
        max = x
        i =n
    n += 1
print(i)

#10
n = -1
x = -1
while x != 0:
    x = int(input())
    if x % 2 == 0:
        n += 1
print(n)

#11
p = int(input())
a = 0
while p != 0:
    n = int(input())
    if n != 0 and p < n:
        a += 1
    p = n
print(a)

#12
max1=0
max2=0
a=int(input())
while a != 0:
    if a>max1:
        max2=max1
        max1=a
    elif a>max2 :
        max2=a
    a=int(input())
print(max2)

#13
max = 0
n = 0
x = -1
while x != 0:
    x = int(input())
    if x > max:
        max, n = x, 1
    elif x == max:
        n += 1        
print(n)

#14
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)

#15
a = int(input())
if a == 0:
    print(0)
else:
    p, n = 0, 1
    x = 1
    while n <= a:
        if n== a:
            print(x)
            break
        p, n = n, p + n
        x += 1
    else:
        print(-1)

#16
p=int(input())
c=1
b=0
while p!=0:
    v=int(input())
    p,v=v,p
    if v==p:
        c+=1
    if c>b:
        b=c
    if p!=v:
        c=1
print(b)

#17
from math import sqrt
sum = 0
sum_squares = 0
i = int(input())
n = 0
while i != 0:
    n += 1
    sum += i
    sum_squares += i ** 2
    i = int(input())
print(sqrt((sum_squares - sum ** 2 / n) / (n - 1)))
