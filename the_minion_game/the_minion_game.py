def minion_game(string):
    # your code goes here
    n = len(string)
    my_list = "AEIOU"
    first, second = 0, 0
    for x in range(n):
        if string[x] in my_list:
            first += (n - x)
        else:
            second += (n - x)
    if first > second:
        print('Kevin',first)
    elif second > first:
        print('Stuart',second)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

#40pt