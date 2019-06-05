from math import factorial
if __name__ == '__main__':
    n = int(input())
    cnt = 0
    char = input().split()
    for i in range(len(char)):
        if char[i] is 'a':
            cnt += n - i - 1
    k = int(input())
    c = factorial(n) / (factorial(n - k) * factorial(k))
    print(cnt / c)
#40