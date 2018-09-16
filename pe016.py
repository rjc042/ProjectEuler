
def add_digits(n):
    sum_digits = 0

    while n > 0:
        chopped_n = n // 10
        digit = n - 10 * chopped_n
        sum_digits += digit

        n = chopped_n

    return sum_digits

def main():
    POWER = 1000
    sum_digits = add_digits(1 << POWER)
    print ("ANSWER: %d") % sum_digits

main()
