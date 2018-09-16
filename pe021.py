from math import sqrt

def d(n):
    sum_divs = 1
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            sum_divs += j + n / j

    sqrt_n = n ** 0.5
    if sqrt_n.is_integer():
        sum_divs -= int(sqrt_n)
    return sum_divs

def get_amic_sum(max_n):
    sum_amic_nums = 0
    for a in range(2, max_n):
        sum_divs_a = d(a)
        if sum_divs_a > a:
            b = d(sum_divs_a)
            if b == a:
                sum_amic_nums += a + sum_divs_a

    return sum_amic_nums

def main():
    MAX_N = 10000
    sum_amic_nums = get_amic_sum(MAX_N)

    print ("ANSWER: %d") % (sum_amic_nums)




main()
