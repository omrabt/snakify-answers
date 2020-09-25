#9.1 Maximum
a = [int(s) for s in input().split()]
b =[]
for i in range(a[0]):
    b.append([int(j) for j in input().split()])
temp =b[0][0]
s,t =0,0

for i in range(a[0]):
    for j in range(a[1]):
       if temp < b[i][j]:
           temp=b[i][j]
           s,t=i,j
print(s,t)

#9.2 Snowflake
n = int(input())
a =[["."]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j or (i+j)==(n-1) or j==(n//2) or i==(n//2):
            a[i][j]="*"
for k in a:
    print(" ".join([str(s) for s in k]))

#9.3 Chess board
a = [int(s) for s in input().split()]
b = [["."]*a[1] for i in range(a[0])]

for i in range(a[0]):
    for j in range(a[1]):
        if (i+j)%2==1:
            b[i][j]="*"
for k in b:
    print(" ".join([s for s in k]))

#9.4 The diagonal parallel to the main
n = int(input())
a = [[0 for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=abs(i-j)
for k in a:
    print(" ".join([str(s) for s in k]))

#9.5 Side diagonal
n = int(input())
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i+j)==(n-1):
            a[i][j]=1
        elif (i+j)>=n:
            a[i][j]=2
for k in a:
    print(" ".join([str(s) for s in k]))

#9.6 Swap the columns
m,n=[int(s) for s in input().split()]
b=[]
for i in range(m):
    b.append([int(s) for s in input().split()])
y,z=[int(s) for s in input().split()]
for i in range(m):
    b[i][y],b[i][z] =b[i][z] ,b[i][y]

for k in b:
    print(" ".join([str(s) for s in k]))

#9.7 Scale a matrix
m,n=[int(s) for s in input().split()]
b=[]
for i in range(m):
    b.append([int(s) for s in input().split()])
y=int(input())
for i in range(m):
    for j in range(n):
        b[i][j]*=y

for k in b:
    print(" ".join([str(s) for s in k]))

#9.8 Multiply two matrices
m,n,r =[int(s) for s in input().split()]
a,b=[],[]
c = [0]*m
for i in range(m):
    c[i] = [0] * r
temp =0
for i in range(m):
    a.append([int(s) for s in input().split()])
for i in range(n):
    b.append([int(s) for s in input().split()])
for i in range(m):
    for k in range(r):
        temp =0
        for j in range(n):
            temp+=a[i][j]*b[j][k]
        c[i][k]=temp
for k in c:
    print(" ".join([str(s) for s in k]))