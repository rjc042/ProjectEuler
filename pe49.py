from primes import get_primes

def primes_func(n,m):
    '''
    Get all primes between n and m
    '''
    all_primes = get_primes(m)
    i = 0
    while all_primes[i] < n:
        i += 1
    return all_primes[i::]

def check(a,b,primes):
    '''
    Generate next number (c)
    Check if c is prime
    Then check if a,b,c are prime permutations
    '''
    c = b + (b - a)
    if c in primes:
        if sorted(str(c)) == sorted(str(a)) == sorted(str(b)):
            return str(a) + str(b) + str(c)
        else:
            return False
    else:
        return False



def main():
    n,m = 1000, 10000
    primes = primes_func(n,m)

    i = 0
    while i < len(primes) - 2:
        if primes[i] == 1487:
            i += 1
        j = i + 1
        while j < len(primes) - 1:
            result = check(primes[i], primes[j], primes)
            if result:
                return result

            j += 1
        i += 1


ans = main()
print "ANSWER: " + ans
