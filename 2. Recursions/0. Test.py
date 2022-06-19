def get_nod(max_n, min_n):
    if max_n%min_n == 0:
        return min_n
    nod = max_n%min_n
    return get_nod(max_n=min_n, min_n=nod)


print(get_nod(81, 48))