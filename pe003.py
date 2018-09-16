
def is_prime(p):
    j = 2
    while j * j <= p:
        if p %j == 0:
            return False
        j += 1
    return True

def get_divisors(n):
    divisors = []
    j = 2
    while j * j <= n:
        if n % j == 0:
            divisors += [j, n / j]
        j += 1
    return divisors

def get_max_prime_divs(n):
    divisors = get_divisors(n)
    max_prime_div = 0
    for div in divisors:
        if is_prime(div) and div > max_prime_div:
            max_prime_div = div
    return max_prime_div

def main():
    N = 600851475143
    max_prime_div = get_max_prime_divs(N)
    print ("ANSWER: %d" % max_prime_div)

main()
