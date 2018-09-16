
def get_prime_factorization(n):
    '''
    Return prime factorization
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

def get_prime_divs(N):
    prime_divs = []
    for d in range(2, N + 1):
        prime_factorization_d = get_prime_factorization(d)
        prime_divs += prime_factorization_d
    prime_divs = list(set(prime_divs))
    return prime_divs

def check_factors(test, N):
    test_div = 2;
    for test_div in range(2, N+1):
        if test % test_div != 0:
            return False
        elif test_div == N:
            return True

def get_ans(N):
    prime_divs = get_prime_divs(N)

    check_num = 2
    while True:
        if check_factors(check_num, N):
            return check_num
        elif check_num % 10000000 == 0:
            print check_num
        check_num += 1

def main():
    N = 20
    ans = get_ans(N)
    print ("ANSWER: %d") % ans

main()
