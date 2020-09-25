#11.1 Number of occurrences
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

#11.2 Dictionary of synonyms
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

#11.3 Elections in the USA
d = {}
k=int(input())

for i in range(k):
    p,o =[s for s in input().split()]
    o=int(o)
    d[p]= d.get(p,0)+o

for candidate, votes in sorted(d.items()):
    print(candidate, votes)

#11.4 The most frequent word
n = int(input())
d=dict()
for i in range(n):
    a =[s for s in input().split()]
    for j in a:
        d[j]=d.get(j,0)+1
buyuk=max(d.values())

most_frequent = [k for k, v in d.items() if v == buyuk]
print(min(most_frequent))
        
#11.5 Access rights
OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    operation, file = input().split()
    if OPERATION_PERMISSION[operation] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

#11.6 Countries and cities
d = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        d[city]= country

for i in range(int(input())):
    print(d[input()])

#11.7 Frequency analysis
n = int(input())

counts = {}
for _ in range(n):
    for word in input().split():
        counts[word] = counts.get(word, 0) + 1
freqs = [(-count, word) for (word, count) in counts.items()]

for c, word in sorted(freqs):
    print(word)

#11.7 English-Latin dictionary
from collections import defaultdict

latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)
  
print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))
