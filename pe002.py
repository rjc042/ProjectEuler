
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def count_evens(N):
    total = 0
    i = 0
    term = fib(i)
    while term < N:
        if term%2 == 0:
            total += term
        i += 1
        term = fib(i)
    return total

def main():
    N = 4e6
    return count_evens(N)


ans = main()
print "ANSWER: " + str(ans)
