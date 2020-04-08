#8.1 The length of the segment
def distance(x1, y1,x2,y2):
    print(((x1-x2)**2+(y1-y2)**2)**0.5)
x1,y1,x2,y2=float(input()),float(input()),float(input()),float(input())
distance(x1,y1,x2,y2)

#8.2 Negative exponent
def power(a,n):
    return(a**n)
print(power(float(input()),int(input())))

#8.3 Uppercase
def capitalize(lwr):
    global b
    b.append(chr(ord(lwr[0])-32))
    for i in range(1,len(lwr)):
        if lwr[i-1]==" ":
            b.append(chr(ord(lwr[i])-32))
        else:
            b.append(lwr[i])
    print("".join(b))

b=[]
capitalize(input())

#8.4 Exponentiation
def power(a, n):
    if n == 0:
        return 1
    else:
        return (a * power(a, n - 1))


a = float(input())
n = int(input())
print(power(a, n))

#8.5 Reverse the sequence
def reserve():
    a =int(input())
    if a == 0:
        print("0")
        return 0
    else:
        reserve()
        print( a)
reserve()

#8.7 Fibonacci numbers
def fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(int(input())))