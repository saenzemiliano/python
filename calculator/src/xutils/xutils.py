def sum_n(nn):
    total = 0
    for n in range(1, nn+1):
        total +=n
    return total

def sum_n_smart(n):
    return (n*(n + 1)) /2