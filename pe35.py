

def rotate(n):
    '''
    Given integer, move last to first
    Return new integer
    '''
    n = str(n)[-1] + str(n)[:len(str(n))-1:]
    n = int(n)
    return n


def check_prime(n):
    '''
    Given integer, return True if prime
    '''
    j = 2
    while j <= int(n**0.5) + 1:
        if n%j == 0:
            return False
            break
        j += 1
    return True

def check_all(n):
    i = 0
    while i < len(str(n)):
        if not check_prime(n):
            return False
            break
        n = rotate(n)
        i += 1
    return True


def main():
    circular_primes = [2]
    for n in range(3,int(1e6)):
        if check_all(n):
            circular_primes.append(n)
    print "ANSWER: ", len(circular_primes)

main()
