#4.1 Series - 1
a =int(input())
b =int(input())+1
for i in range(a,b):
    print(i)

#4.2 Series - 2
a,b = int(input()),int(input())
if a<=b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)

#4.3 Sum of ten numbers
sum = 0
for i in range(10):
    sum += int(input())
print(sum)

#4.4 Sum of N numbers
sum =0
for i in range(int(input())):
    sum += int(input())
print(sum)

#4.5 Sum of cubes
sum = 0
for i in range(1,int(input())+1):
    sum += i**3
print(sum)

#4.6 Factorial
sum = 1
for i in range(2,int(input())+1):
    sum*=i
print(sum)

#4.7 The number of zeros
count =0
n=int(input())
for i in range(n):
    a =int(input())
    if a==0:
        count+=1
print(count)

#4.8 Adding factorials
top = 1
temp = 0
for i in range(1,int(input())+1):
    top *=i
    temp +=top
print(temp)

#4.9 Ladder
a=""
for i in range(1,int(input())+1):
    a += str(i)
    print(a)

#4.10 Lost card
n = int(input())
temp = 0
for i in range(n - 1):
    temp += int(input())
temp2 = 0
for i in range(1, n + 1):
    temp2 += i

print(temp2 - temp)