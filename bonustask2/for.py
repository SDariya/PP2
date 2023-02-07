#1
A=int(input())
B=int(input())
for i in range(A, B+1):
    print(i)

#2
A=int(input())
B=int(input())
if (A<B):
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1,-1):
        print(i)

#3
A=int(input())
B=int(input())
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i)

#4
sum=0
for i in range(10):
    n=int(input())
    sum+=n
print(sum)

#5
sum=0
n=int(input())
for i in range(n):
    sum+=int(input())
print(sum)

#6
sum=0
n=int(input())
for i in range(1,n+1):
    sum+=i**3
print(sum)

#7
b=1
n=int(input())
for i in range(1, n+1):
    b*=i
print(b)

#8
b=1
sum=0
n=int(input())
for i in range(1, n+1):
    b*=i
    sum=sum+b
print(sum)


#9
n = 0
for i in range(int(input())):
    if int(input()) == 0:
        n += 1
print(n)

#10
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()


#11
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)
