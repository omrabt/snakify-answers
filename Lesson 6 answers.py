#6.1 List of squares
n = int(input())
i=1
while i**2 <=n:
    print(i**2)
    i=i+1

#6.2 Least divisor
n = int(input())
i = 2
while True:
    if n%i==0:
        print(i)
        break
    else:
        i=i+1
#6.3 The power of two
n = int(input())
t = 2
u = 0
u2 = 0
sonuc=1
sonuc2 = 0
while sonuc <= n:
    sonuc*=t
    u +=1
sonuc2 = sonuc//2
u2 = u-1
print(u2,sonuc2)

#6.4 Morning jog
x = int(input())
y = int(input())
sayac = 1
if y < x:
    print(sayac)
else:

    while (x < y):
        x += (x / 10)
        sayac += 1
    print(sayac)

#6.5 The length of the sequence
sayac = 0
a = int(input())
while a != 0:
    a = int(input())
    sayac += 1
print(sayac)

#6.6 The sum of the sequence
a = int(input())
f=a

while( a != 0):
    a =int(input())
    f +=a
print(f)

#6.7 The average of the sequence
a = int(input())
top =a
count = 1
while a !=0:
    a = int(input())
    top +=a
    count+=1
print(top/(count-1))

#6.8 The maximum of the sequence
a = int(input())
temp = 0
while a != 0:
    if a > temp:
        temp = a
    a = int(input())
print(temp)

#6.9 The index of the maximum of a sequence
a = int(input())
temp = 0
index = 0
index_maks = 0
while a != 0:
    index += 1
    if a > temp:
        temp = a
        index_maks = index
    a = int(input())
print(index_maks)

#6.10 The number of even elements of the sequence
a = int(input())
say =0
while a!=0:
    if a%2 == 0:
        say+=1
    a=int(input())
print(say)

#6.11 The number of elements that are greater than the previous one
a = int(input())
say = -1
temp = 0
while a != 0:

    if temp < a:
        say += 1
    temp = a
    a = int(input())
print(say)

#6.12 The second maximum
a = int(input())
temp = 0
b = 0
while a != 0:
    if a > temp:
        b = temp
        temp = a
    a = int(input())
    if b < a:
        b = a
print(b)

#6.13 The number of elements equal to the maximum
a = int(input())
temp = 0
b = 0
while a != 0:
    if a > temp:
        b = temp
        temp = a
    a = int(input())
    if b < a:
        b = a
print(b)

#6.14 The number of elements equal to the maximum
a = int(input())
temp = 0
say = 1
while a != 0:
    if a > temp:
        temp = a
        say = 1
    a = int(input())
    if temp == a:
        say += 1
print(say)

#6.15 Fibonacci numbers
n = int(input())
i =1
p = 1
c=1
temp=1
if n == 0:
    temp =0
else:
    while i<(n-1):
        temp = p+c
        p=c
        c=temp
        i+=1
print(temp)

#6.16 The index of a Fibonacci number
n = int(input())
sayi = 0
a,b=0,1
if n ==0:
    print("0")
else:
    while b < n:
        a,b = b,a+b
        sayi+=1
    if b==n:
        print(sayi+1)
    else:
        print("-1")

#6.17 The maximum number of consecutive equal elements
a = int(input())
temp, temp2 = 1, 0
while a != 0:
    b = int(input())
    if a == b:
        temp += 1

    elif a != b and temp2 <= temp:
        temp2 = temp
        temp = 1
    elif a != b:
        temp = 1
    a = b
print(temp2)