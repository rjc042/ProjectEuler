
def is_prime(n):
    j = 2
    while j * j <= n:
        if n % j == 0:
            return False
        j += 1
    return True

def get_sum_primes(max_n):
    sum_primes = 0
    for i in range(2, max_n):
        if is_prime(i):
            sum_primes += i
    return sum_primes

def main():
    N = int(2e6)
    sum_primes = get_sum_primes(N)
    print ("ANSWER: %d" % sum_primes)

main()
