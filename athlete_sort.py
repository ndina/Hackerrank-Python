table = list(map(int, input().split()))

arr = list()

for i in range(table[0]):
    arr.append(list(map(int, input().split())))

k = int(input())

sorte = sorted(arr, key=lambda record: record[k])

for i in sorte:
    print(*i)

#30pt