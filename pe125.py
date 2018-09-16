
def is_palindrome(n):
    return str(n)[::-1] == str(n)

def squares_below(max_n):
    return [i * i for i in range(1, int(max_n ** 0.5) + 3)]

def get_palindromes(max_n, squares):
    palindromes = []
    for square_i in range(len(squares)):
        check_pal = squares[square_i]

        if is_palindrome(check_pal):
            square_i += 1
            check_pal += squares[square_i]

        while check_pal < max_n:
            if is_palindrome(check_pal):
                palindromes.append(check_pal)
            square_i += 1
            check_pal += squares[square_i]
    palindromes = list(set(palindromes))
    return palindromes



def main():
    N = int(1e8)
    squares = squares_below(N)
    palindromes = get_palindromes(N, squares)
    sum_pals = sum(palindromes)
    print ("ANSWER: %d" % sum_pals)



main()
