from prime import is_prime

primes = [ 2, 3, 5, 19, 23]
non_primes = [ 4, 9, 15, 18]

def test_is_prime():
    for p in primes:
        assert is_prime(p)
    for p in non_primes:
        assert not is_prime(p)
