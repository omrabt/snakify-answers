#2.1 Last digit of integer
a = int(input())
print(a%10)

#2.2 Tens digit
a = int(input())
print((a%100)//10)

#2.3 Sum of digits
a = int(input())
sonuc= a//100 + (a//10)%10 + a%10
print(sonuc)

#2.4 Fractional part
a = float(input())
import math
sonuc= a- int(a)
print(sonuc)

#2.5 First digit after decimal point
a = float(input())
print(int((a*10)%10))

#2.6 Car route
import math
n,k=int(input()),int(input())
print(math.ceil(k/n))

#2.7 Digital clock
a = int(input())
print(a//60,a%60)

#2.8 Total cost
a,b,n = int(input()),int(input()),int(input())
dollar = a*n+(b*n)//100
cent = (b*n)%100
print(dollar,cent)

#2.9 Clock face - 1
h,m,s = int(input()),int(input()),int(input())
print(h*30+m*30/60+s*30/3600)

#2.10 Clock face - 2
a = float(input())
print((a%30)*360/30)
