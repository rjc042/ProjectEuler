import itertools

def checkPrime(n):
    '''
    return True if n is prime
    '''
    j = 2
    while j*j < n + 1:
        if n%j == 0:
            return False
        j += 1
    return True


def replaceDigits(n):
    '''
    Lists of indices to be replaced in num
    '''
    indices = [i for i in range(len(str(n))-1)]
    replace_digits = []

    for i in xrange(1, len(indices)+1):
        els = [list(x) for x in itertools.combinations(indices, i)]
        replace_digits.extend(els)
    return replace_digits


def nextNum(n):
    '''
    returns next number to try
    '''
    if str(n)[-1] in ['1', '7', '9']:
        return n + 2
    else:
        return n + 4

def countPrimes(n, combo):
    '''
    Given n and indices to replace, return number that are prime
    '''
    count_primes = 0
    start = 0
    if 0 in combo:
        start += 1

    check_nlist = list(str(n))
    for i in range(start, 10):
        for ind in combo:
            check_nlist[ind] = str(i)
        check_n = int(''.join(check_nlist))

        if checkPrime(check_n):
            count_primes += 1
    return count_primes

def finalAnswer(n, combo):
    '''
    '''
    start = 0
    if 0 in combo:
        start += 1

    check_nlist = list(str(n))
    for i in range(start, 10):
        for ind in combo:
            check_nlist[ind] = str(i)
        check_n = int(''.join(check_nlist))
        if checkPrime(check_n):
            return check_n



def main():
    target = 8

    n = 11
    replace_digits = replaceDigits(n)
    while True:
        for combo in replace_digits:
            num_primes = countPrimes(n, combo)
            if num_primes == target:
                ans = finalAnswer(n, combo)
                return ans

        if len(str(n)) < len(str(nextNum(n))):
            n = nextNum(n)
            replace_digits = replaceDigits(n)
        else:
            n = nextNum(n)



ans = main()
print "ANSWER: " + str(ans)
