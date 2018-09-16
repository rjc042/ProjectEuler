from itertools import *
import numpy as np

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
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

# def getLists(primes_list, n):
#     combos = list(combinations(primes_list, n))
#     # combos = list(combinations_with_replacement(primes_list, n))
#     # combos = sorted(combos)
#     # combos = [list(combo) for combo in combos]
#     return combos

# def checkBadPairs(combo, badpairs):
#     '''
#     check for any bad pairs in list of n primes
#     returns True if combo contains no bad pairs
#     '''
#     for badpair in badpairs:
#         if badpair[0] in combo and badpair[1] in combo:
#             print combo, " contains a bad pair ", badpair[0], badpair[1] , " returning False"
#             return False
#     # print "No bad pairs in ", combo
#     return True

def checkPair(pair, badpairs):
    '''
    check if pair works
    '''
    if set(pair) in badpairs:
        # print set(pair), "is a badpair"
        return [False, badpairs]
    else:
        newnum1 = int(str(pair[0]) + str(pair[1]))
        newnum2 = int(str(pair[1]) + str(pair[0]))
        if not checkPrime(newnum1) or not checkPrime(newnum2):
            # print newnum, " is not prime"
            # print "Appending " + str([pair[0], pair[1]]) + " to badpairs"
            badpairs.append(set([pair[0], pair[1]]))
            # print "Badpairs is now ", badpairs
            return [False, badpairs]
        # print pair, " is good"
        return [True, badpairs]



def checkPairs(combo, badpairs):
    '''
    return True if all pairs concatenated are prime
    '''
    # print "Bad pairs: ", badpairs
    # if not checkBadPairs(combo, badpairs):
    #     return [False, badpairs]

    pairs = list(permutations(combo, 2))
    for pair in pairs:
        # print "Checking pair: ", pair
        if set(pair) in badpairs:
            # print pair, " is a badpair"
            return [False, badpairs]
        newnum = str(pair[0]) + str(pair[1])        # concatenate pair
        newnum = int(newnum)
        if not checkPrime(newnum):
            # print newnum, " is not prime"
            # print "Appending " + str([pair[0], pair[1]]) + " to badpairs"
            badpairs.append(set([pair[0], pair[1]]))
            # print "Badpairs is now ", badpairs
            return [False, badpairs]
    return [True, badpairs]

def main():
    n = 5
    primes_list = rwh_primes2(1000)                         # list of first ? primes
    primes_list.remove(2)
    primes_list.remove(5)
    # print "Done generating list of primes"
    # combos = getLists(primes_list, n)                       # list of lists of n primes
    # print "Done generating list of lists of 4 primes"
    badpairs = []
    # for combo in combos:                                    # check each list of n primes
    #     print "\nChecking list of 4 primes: ", combo
    #     checkedPairs = checkPairs(combo, badpairs)
    #     badpairs = checkedPairs[1]
    #     if checkedPairs[0]:
    #         print "Winner"
    #         print combo
    #         print "ANSWER: ", sum(list(combo))
    #         return sum(list(combo))

    combo = np.zeros(n, dtype = int)
    for i in range(len(primes_list)):
        combo[0] = primes_list[i]
        for j in range(i):
            combo[1] = primes_list[j]
            test_pair = [combo[0], combo[1]]
            check_test = checkPair(test_pair, badpairs)
            if not check_test[0]:
                badpairs = check_test[1]
            else:
                for k in range(j):
                    combo[2] = primes_list[k]
                    test_pair1 = [combo[1], combo[2]]
                    check_test1 = checkPair(test_pair1, badpairs)
                    test_pair2 = [combo[0], combo[2]]
                    check_test2 = checkPair(test_pair2, badpairs)
                    if not check_test1[0]:
                        badpairs = check_test1[1]
                    if not check_test2[0]:
                        add = [pair for pair in check_test2[1] if pair not in badpairs]
                        badpairs += add
                    else:
                        for l in range(k):
                            combo[3] = primes_list[l]
                            for m in range(l):
                                combo[4] = primes_list[m]
                                # combo = list(combo)
                                # print "\nChecking list of 4 primes: ", combo
                                checkedPairs = checkPairs(combo, badpairs)
                                badpairs = checkedPairs[1]
                                if checkedPairs[0]:
                                    print "Winner"
                                    print combo
                                    print "ANSWER: ", sum(list(combo))
                                    return sum(list(combo))


main()
