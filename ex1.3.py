cache ={}
def fast(n):
    if n==0 or n==1:
        return n
    if n in cache.keys():
        return cache[n]
    else:
        cache[n]= fast(n-1)+fast(n-2)
        return cache[n]