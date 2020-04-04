#1.1 Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#1.2  Hi John
a = input()
print("Hi",a)

#1.3 Square
a = int(input())
print(a*a)

#1.4 Area of right-angled triangle
b,a = int(input()),int(input())
print((a*b)/2)

#1.5 Hello, Harry!
name = input()
print("Hello,",name+"!")

#1.6 Apple sharing
n = int(input())
k = int(input())
print(k // n)
print(k%n)

#1.7 Previous and next
a = int(input())
print("The next number for the number", a, "is", str(a+1)+".")
print("The previous number for the number", a ,"is", str(a-1)+".")

#1.8 Two timestamps
s1,d1,sa1 = int(input()),int(input()),int(input())
s2,d2,sa2 = int(input()),int(input()),int(input())
sonuc = (s2-s1)*3600+(d2-d1)*60+(sa2-sa1)
print(sonuc)

#1.9 School desks
a,b,c = int(input()),int(input()),int(input())
sonuc = (a//2)+(a%2)+(b//2)+(b%2)+c//2+c%2
print(sonuc)