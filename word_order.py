if __name__ == '__main__':
    dict = {}
    for i in range(int(input())):
        word = input()
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    print(len(dict))
    for i in dict:
        print(dict[i], end=' ')

#50pt
