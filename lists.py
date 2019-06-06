if __name__ == '__main__':
    N = int(input())

    list = []

    for i in range(N):
        item = input().split()
        if item[0] == 'print':
            print(list)
        elif item[0] == 'sort':
            list.sort()
        elif item[0] == 'remove':
            list.remove(int(item[1]))
        elif item[0] == 'append':
            list.append(int(item[1]))
        elif item[0] == 'insert':
            list.insert(int(item[1]), int(item[2]))
        elif item[0] == 'reverse':
            list.reverse()
        elif item[0] == 'pop':
             list.pop()

#10