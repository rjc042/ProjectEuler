
def check_prime(n):
    j = 2
    while j * j <= n:
        if n % j == 0:
            return False
        j += 1
    return True

def find_prime(N):
    prime_num = 1
    i = 2
    while True:
        if check_prime(i):
            # print i, " is the ", prime_num, " prime"
            if prime_num == N:
                return i
            prime_num += 1
        i += 1

def main():
    N = 10001
    return find_prime(N)

ans = main()
print "ANSWER: " + str(ans)
