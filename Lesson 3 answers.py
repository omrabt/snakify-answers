#3.1 Minimum of two numbers
a,b = int(input()),int(input())
if a>b:
    print(b)
else:
    print(a)

#3.2 Sign function
a = int(input())
if a>0:
    print(1)
elif a<0:
    print(-1)
else:
    print(0)

#3.3 Minimum of three numbers
a,b,c = int(input()),int(input()),int(input())

if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)

#3.4 Equal numbers
a,b,c = int(input()),int(input()),int(input())
if a==b==c:
    print(3)
elif a==b or b==c or c==a:
    print(2)
else:
    print(0)

#3.5 Rook move
x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

#3.6 Chess board - same color
x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if(x1+y1)%2 == (x2+y2)%2:
    print("YES")
else:
    print("NO")
#3.7 King move
x1,y1,x2,y2 =int(input()),int(input()),int(input()),int(input())
if x1==x2 and abs(y1-y2)==1:
    print("YES")
elif y1==y2 and abs(x1-x2)==1:
    print("YES")
elif abs(x1-x2)==1 and abs(y1-y2)==1:
    print("YES")
else:
    print("NO")

#3.8 Bishop moves
x1,y1,x2,y2 =int(input()),int(input()),int(input()),int(input())
if abs(x1-x2)==abs(y2-y1):
    print("YES")
else:
    print("NO")

#3.9 Queen move
x1,y1,x2,y2 =int(input()),int(input()),int(input()),int(input())
if abs(x1-x2)==abs(y1-y2):
    print("YES")
elif y1==y2 or x1==x2:
    print("YES")
else:
    print("NO")

#3.10 Knight move
x1,y1,x2,y2 =int(input()),int(input()),int(input()),int(input())
if x1==x2 or y1 ==y2:
    print("NO")
elif abs(x1-x2) == (abs(y1-y2)+1) or abs(y1-y2) == (abs(x1-x2)+1):
    print("YES")
else:
    print("NO")

#3.11 Chocolate bar
a,b,c=int(input()),int(input()),int(input())
if a*b<=c:
    print("NO")
elif (c%a)==0 or (c%b)==0:
    print("YES")
else:
    print("NO")

#3.12 Leap year
a = int(input())
if a%100 == 0 and (a//100)%4!=0:
    print("COMMON")
elif a%4 == 0 :
    print("LEAP")
else:
    print("COMMON")