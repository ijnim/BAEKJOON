n = int(input())
n_lst = [i for i in range(n,1,-1)] + [i for i in range(1,n+1)]
for i in n_lst:
    print(' '*(n-i) + '*'*(2*i-1))