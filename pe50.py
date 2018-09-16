
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

def maxFromStart(ind, limit, primes_list):
    '''
    returns [max length, total] starting from ind
    '''
    consec_primes = [primes_list[ind]]
    seq_total = primes_list[ind]
    # max_length = 0
    while seq_total < limit:                                  # sum consecutive primes
        if checkPrime(seq_total):                             # if total is prime, update maximum length for
            max_length = len(consec_primes)
            total = seq_total
        ind += 1
        consec_primes += [primes_list[ind]]
        seq_total += primes_list[ind]
    return [max_length, total]

def maxForEachStart(limit, primes_list):
    '''
    return list of list of max_lengths and totals for each starting indices
    '''
    totals = []
    max_lengths = []
    start_index = 0
    while primes_list[start_index] < limit/2:
        longest_seq = maxFromStart(start_index, limit, primes_list)
        max_lengths.append(longest_seq[0])
        totals.append(longest_seq[1])
        start_index += 1
    return [max_lengths, totals]

def main():
    limit = int(1e6)
    primes_list = rwh_primes2(int(5.0*limit/9.0))

    longest_sums = maxForEachStart(limit, primes_list)
    max_lengths = longest_sums[0]
    totals = longest_sums[1]
    maxmax_length = max(max_lengths)
    index = max_lengths.index(maxmax_length)
    total_prime = totals[index]
    print "ANSWER: ", total_prime

main()
