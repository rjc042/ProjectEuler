

def primes(n):
    '''
    return prime factorization
    '''
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


# def checkPrime(n):
#     '''
#     Return True if n is prime
#     '''
#     if n == 2:
#         return True
#     j = 2
#     while j < int(n**0.5 + 1):
#         if n%j == 0:
#             return False
#             break
#         j += 1
#     return True



def checkAllComposite(lst):
    '''
    return True if (consecutive) integers in list are all composite
    '''
    bool = True
    for i in lst:
        if checkPrime(i):
            bool = False
    return bool


def checkLengths(test_list, n):
    '''
    return True if there are n distinct primes for each elt in test_list
    '''
    bool = True
    j = 0
    while j < len(test_list):
        comp = test_list[j]
        prime_factors = primes(comp)
        distinct_primes = list(set(prime_factors))
        if len(distinct_primes) < n:
            bool = False
            break
        j += 1
    return bool


def main(n):
    i = 2
    while True:
        test_list = [j for j in range(i, i+n)]                              # list of consecutive integers
        if checkLengths(test_list, n):
                # check if all the integers have n distinct primes
                break
        i += 1
    print "ANSWER: ", test_list[0]


n = 4
main(n)
