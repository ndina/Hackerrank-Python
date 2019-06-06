s = input()
n = int(input())
for i in range(0, len(s) + 1, n):
    print(s[i:i + n])

