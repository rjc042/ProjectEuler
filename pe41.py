import itertools

def iterString(n):
    dig = 1
    s = ''
    while dig <= n:
        s += str(dig)
        dig += 1
    return s

def getPandigitals(s):
    pans = list(itertools.permutations(s))
    pans = [list(p) for p in pans if p[0] != '0']
    for i in range(len(pans)):
        pans[i] = int(''.join(pans[i]))
    return pans

def checkPrime(n):
    j = 2
    bool = True
    while j <= int(n**0.5 + 1):
        if n%j == 0:
            bool = False
            break
        j += 1
    return bool


def getPrimePans(n):
    s = iterString(n)
    pandigitals = getPandigitals(s)
    pan_primes = [p for p in pandigitals if checkPrime(p)]
    return pan_primes


def main():
    pan_primes = []
    for n in range(1,10):
        pan_primes += getPrimePans(n)
    print "ANSWER: ", max(pan_primes)

main()
