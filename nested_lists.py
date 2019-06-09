first = []
second = []
if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        first += [[name, score]]
        second += [score]
    b = sorted(list(set(second)))[1]

    for n, s in sorted(first):
        if s == b:
            print(n)