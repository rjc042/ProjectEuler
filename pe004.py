
def is_palindrome(n):
    reverse_n = str(n)[::-1]
    return n == int(reverse_n)

def get_max_palindrome(num_digits):
    start, end = 10 ** (num_digits - 1), 10 ** num_digits
    max_pal = 0
    for a in range(start, end):
        for b in range(a, end):
            check_palindrome = a * b
            if is_palindrome(check_palindrome) and check_palindrome > max_pal:
                max_pal = check_palindrome
    return max_pal

def main():
    NUM_DIGITS = 3
    max_pal = get_max_palindrome(NUM_DIGITS)
    print ("ANSWER: %d" % max_pal)

main()
