
def getPrimes(n):
    lst = [2,3]
    for i in range(4,n):
        j = 2
        while j <= int(i**0.5) + 1:
            if i%j == 0:
                break
            elif j == int(i**0.5):
                lst.append(i)
            j += 1
    return lst

def testPrimes(lst):
    test_primes = lst[4:]
    checkedRtoL = []
    for p in test_primes:
        a = p
        while len(str(a)) > 1:
            a = int(str(a)[:-1])
            if a not in lst:
                break
            elif len(str(a)) == 1:
                checkedRtoL.append(p)

    trunc_primes = []
    for p in checkedRtoL:
        b = p
        while len(str(b)) > 1:
            b = int(str(b)[1:])
            if b not in lst:
                break
            elif len(str(b)) == 1:
                trunc_primes.append(p)
    return trunc_primes



def main():
    n = 800000
    primes_list = getPrimes(n)                  # get all primes below n
    trunc_primes = testPrimes(primes_list)
    print trunc_primes
    print "ANSWER:", sum(trunc_primes)



main()
