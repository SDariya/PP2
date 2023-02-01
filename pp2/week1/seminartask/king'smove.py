a=int(input())
b=int(input())
c=int(input())
d=int(input())
if ((a==c and (b+1==d or b-1==d)) or (b==d and (a+1==c or a-1==c)) or ((a-1==c and b-1==d) or (a+1==c and b-1==d) or (c==a-1 and d==b+1) or (c==a+1 and d==b+1))):
    print("YES")
else:
    print("NO")