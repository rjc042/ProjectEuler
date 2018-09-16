
def main():
    N = 100
    sum_of_squares = sum([i**2 for i in range(N+1)])
    square_of_sum = sum(range(N+1))**2
    return square_of_sum - sum_of_squares

ans = main()
print "ANSWER: " + str(ans)
