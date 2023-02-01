x=int(input())
y=int(input())
z=int(input())
if (x==y and x==z):
    print(3)
elif ((x==y and x!=z) or (x==z and x!=y) or (z==y and x!=z)):
    print(2)
else :
    print(0)