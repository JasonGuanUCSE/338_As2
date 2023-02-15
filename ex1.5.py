import timeit
import matplotlib.pyplot as plt

def slow(n):
    if n==0 or n==1:
        return n
    else:
        return slow(n-1)+slow(n-2)



cache ={}
def fast(n):
    if n==0 or n==1:
        return n
    if n in cache.keys():
        return cache[n]
    else:
        cache[n]= fast(n-1)+fast(n-2)
        return cache[n]

slow_time=[]
fast_time=[]

for input in range(0,35):
    timing_slow =timeit.timeit(lambda:slow(input),number=1)
    slow_time.append(timing_slow)
    timing_fast=timeit.timeit(lambda:fast(input),number=1)
    fast_time.append(timing_fast)


plt.plot(slow_time)
plt.plot(fast_time)
plt.legend(["Slow time","Fast time"])
plt.show()



