
def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def get_sum_digits(n):
    sum_digits = 0
    while n:
        sum_digits += n % 10
        n //= 10
    return sum_digits


def main():
    N = 100
    fact_n = factorial(N)
    sum_digits = get_sum_digits(fact_n)
    print ("ANSWER: %d") % (sum_digits)

main()
