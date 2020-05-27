import math

# Program for Amicable numbers

from functools import reduce

def factorize(n) :
    step = 2 if n % 2 else 1
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n ** 0.5) + 1, step) if n % i == 0))))


count = 0
n = 2
s = set()
l = []

while count != 10 :
    if n in s :
        n = n + 1
    set1 = factorize(n)
    summation1 = sum(set1) - n
    if summation1 == n :
        n = n + 1
        continue
    set2 = factorize(summation1)
    summation2 = sum(set2) - summation1
    if summation2 == n :
        s.add(n)
        s.add(summation1)
        s1 = (n, summation1)
        l.append(s1)
        count = count + 1
    n  = n + 1

print(l)