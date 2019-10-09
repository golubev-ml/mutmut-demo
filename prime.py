# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_prime_eratosthenes():
    d, q = {}, 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else: 
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


import math
def is_prime_simple(n):
    q = int(math.sqrt(n)+1)
    for x in range(2, q):
        if n % x == 0:
            return False
    return True

import re
def is_prime_re(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is  None
