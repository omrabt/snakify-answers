#10.1 The number of distinct numbers
a =set(input().split())
print(len(a))

#10.2 The number of equal numbers
a = set(input().split())

b = set(input().split())
print(len(a.intersection(b)))

#10.3 The intersection of sets
print(*sorted(set(input().split()) & set(input().split())))

#10.4 Has the number been encountered before
a = [int(s) for s in input().split()]
K=set()
for i in range(len(a)):
    if (a[i] in K) ==True:
        print("YES")
        K.add(a[i])
    else:
        print("NO")
        K.add(a[i])

#10.5 Cubes
m,n = [int(s) for s in input().split()]
alice = set()
bob = set()
for i in range(m):
    alice.add(int(input()))
for i in range(n):
    bob.add(int(input()))
print(len(alice & bob))
print(*sorted(alice & bob))
print(len(alice-bob))
print(*sorted(alice-bob))
print(len(bob-alice))
print(*sorted(bob-alice))
    
#10.6 The number of distinct words in some text
n = int(input())
temp =set()
for i in range(n):
    temp|=set(input().split())

print(len(temp))

#10.7 Guess the number
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))

#10.8 Polyglots
n = int(input())
a=set()
c=set()
for i in range(int(input())):
    a.add(input())
c=a
for i in range(n-1):
    b=set()
    for j in range(int(input())):
        b.add(input())
    a&=b
    c|=b
    
print(len(a),"\n",*sorted(a),"\n",str(len(c)),"\n",*sorted(c))

