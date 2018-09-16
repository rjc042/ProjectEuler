
def get_prime_list(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def get_r(primes_list, n):
    pn = primes_list[n]
    r = ((pn - 1) ** n + (pn + 1) ** n) % (pn ** 2)
    return r

def get_min_n(primes_list, target):
    n = 3
    r = get_r(primes_list, n)
    while r < target:
        n += 1
        r = get_r(primes_list, n)
    return n

def main():
    primes_list = [2] + get_prime_list(1000000)
    TARGET_REMAINDER = 10 ** 10

    min_n = get_min_n(primes_list, TARGET_REMAINDER)

    print "ANSWER: ", min_n



main()
