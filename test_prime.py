import math
import re
import pytest
from prime import gen_prime_eratosthenes, is_prime_simple, is_prime_re
from sympy import isprime

gpe = gen_prime_eratosthenes()
@pytest.mark.parametrize("n", [next(gpe) for i in range(15)])
def test_prime_gpe(n):
    assert isprime(n)

@pytest.mark.parametrize("n", [x for x in range(2,15) if is_prime_simple(x)])
def test_prime_simple(n):
    assert isprime(n)

@pytest.mark.parametrize("n", [x for x in range(2,15) if is_prime_simple(x)])
def test_prime_re(n):
    assert isprime(n)


@pytest.mark.parametrize("n", [x for x in range(15) if not is_prime_simple(x)])
def test_not_prime_simple(n):
    assert not isprime(n)

@pytest.mark.parametrize("n", [x for x in range(15) if not is_prime_simple(x)])
def test_not_prime_re(n):
    assert not isprime(n)