
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


def getRatio(num_primes, diag_list):
    '''
    return ratio of prime diagonals
    '''
    return float(num_primes)/len(diag_list)

def main(cutoff):
    '''
    returns list of first n diagonals
    '''
    num_primes = 0
    diag_list = [1]
    inc = 2
    num = 1
    while True:
        for i in range(4):
            num += inc
            diag_list.append(num)
            if checkPrime(num):
                num_primes += 1
            ratio = getRatio(num_primes, diag_list)
            if ratio < cutoff:
                length = inc + 1
                return length
        inc += 2

cutoff = 0.10
print "ANSWER: ", main(cutoff)
