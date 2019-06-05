import collections
collec = collections.Counter(input())
string = sorted(collec.items(), key=lambda x: x[0])
string = sorted(string, reverse=True, key=lambda x: x[1])
for i in range(3):
    print(*string[i])

#30