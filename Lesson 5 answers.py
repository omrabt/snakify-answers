#5.1 Slices
a = input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[:-2])
print(a[::2])
print(a[1::2])
print(a[::-1])
print(a[::-2])
print(len(a))

#5.2 The number of words
a=input()
say=0
s = a.split()
for i in range(len(s)):
    say+=1
print(say)

#5.3 The two halves
a = input()
b = len(a)
if (b%2)==0:
    print(a[b//2:]+a[:b//2])
elif (b%2)==1:
    print(a[b//2+1:]+a[:b//2+1])

#5.4 To swap the two words
a = input()
a = a.split()
print(a[1],a[0])

#5.5 The first and last occurrence
a=input()
say = a.count("f")
x1 = a.find("f")
x2= a.rfind("f")
if say ==0:
    print()
elif x1!=x2:
    print(x1,x2)
elif x1 ==x2:
    print(x1)

#5.6 The second occurrence
a = input()
b = a.find("f")
say = a.count("f")
if say ==1:
    print("-1")
elif say == 0:
    print("-2")
elif say >=2:
    print(a[b+1:].find("f")+b+1)

#5.7 Remove the fragment
a = input()
print(a[:a.find("h")]+a[a.rfind("h")+1:])

#5.8 Reverse the fragment
a = input()
print(a[:a.find("h")+1]+a[a.rfind("h")-1:a.find("h"):-1]+a[a.rfind("h"):])

#5.9 Replace the substring
a=input()
print(a.replace("1","one"))

#5.10 Delete a character
a = input()
print(a.replace("@",""))

#5.11 Delete a character
a = input()
print(a.replace("@",""))

#5.12 Replace within the fragment
a = input()
print(a[:a.find("h")+1]+a[a.find("h")+1:a.rfind("h")].replace("h","H")+a[a.rfind("h"):])

#5.13 Delete every third character
a = input()
for i in range(len(a)):
    if i%3 != 0:
        print(a[i],end="")
