#7.1 Even indices
a =[s for s in input().split()]
print(" ".join(a[::2]))

#7.2 Even elements
a =[int(s) for s in input().split()]

for i in a:
    if i%2 ==0:
        print(i)

#7.3 Greater than previous
a = [int(s) for s in input().split()]

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        print(a[i+1])

#7.4 Neighbors of the same sign
a = [int(s) for s in input().split()]

for i in range(len(a)-1):
    if a[i]*a[i+1]>0:
        print(a[i],a[i+1])
        break

#7.5 Greater than neighbours
a = [int(s) for s in input().split()]
say = 0
for i in range(len(a) - 2):
    if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:
        say += 1
print(say)

#7.6 The largest element
a = [int(s) for s in input().split()]
temp,top =a[0],0

for i in range(len(a)):
    if temp < a[i]:
        temp = a[i]
        top =i
print(temp,top)

#7.7 The number of distinct elements
a = [int(s) for s in input().split()]
counter=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        counter+=1
print(counter)

#7.8 Swap neighbours
a = [int(s) for s in input().split()]

for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]

print(" ".join([str(i) for i in a]))

#7.9 Swap min and max
a = [int(s) for s in input().split()]
max_value = max(a)
min_value = min(a)
max_index,min_index = 0,0
for i in range(len(a)):
    if a[i]==max_value:
        max_index =i
    elif min_value ==a[i]:
        min_index = i
a[min_index],a[max_index]=a[max_index],a[min_index]
print(" ".join([str(s) for s in a]))

#7.10 The number of pairs of equal
a = [int(s) for s in input().split()]
counter=0
for i in range(len(a)):
    for j in a[i+1:]:
        if a[i]==j:
            counter+=1
print(counter)

#7.11 Unique elements
a = [int(s) for s in input().split()]

for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i])

#7.12 Queens
x, y = [], []
sonuc = "NO"
for i in range(8):
    m, n = [int(s) for s in input().split()]
    x.append(m)
    y.append(n)
for i in range(7):
    for j in range(i + 1, 7):
        if (x[i] == x[j]) or (y[i] == y[j]):
            sonuc = "YES"
        elif abs(x[i] - x[j]) == abs(y[j] - y[i]):
            sonuc = "YES"
print(sonuc)

#7.13 The bowling alley
m,n = [int(s) for s in input().split()]
a=["I"]*m
for i in range(n):
    y,z=[int(s) for s in input().split()]
    for j in range(y-1,z):
        a[j]="."
print("".join(a))
