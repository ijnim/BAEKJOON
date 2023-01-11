n = int(input())
str_lst = [input() for i in range(n)]
for I in str_lst:
    lst = [0]
    for i in I:
        if i=='O':
            lst.append(lst[-1]+1)
        else:
            lst.append(0)
    print(sum(lst))