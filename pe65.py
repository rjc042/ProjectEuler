
def iterList(k):
    evens = [2*i for i in range(1,k)]
    lst = [1]
    for even in evens:
        lst += [even, 1, 1]
    return lst

def nextFrac(k, lst):
    '''
    return fraction to be added to s0 for term k
    '''
    k += 1
    frac_list = lst[0:k]
    frac_list = frac_list[::-1]

    num = 1
    den = frac_list[0]
    for i in range(1,k):
        addnums = frac_list[i]*den + num
        num = den
        den = addnums

    return [num, den]





def apprSeq(n,s0,lst):
    '''
    n == number of terms in sequence to generate
    s0 == value to be added to each term
    lst == list to iterate over
    '''

    seq_fracs = [[s0,1]]

    for numterms in range(n):
        next_frac = nextFrac(numterms,lst)
        frac_num = next_frac[0]
        frac_den = next_frac[1]

        term = [s0*frac_den + frac_num, frac_den]
        seq_fracs.append(term)
    return seq_fracs

def addDigits(c, seq):
    '''
    Add digits of cth convergent
    '''
    frac = seq[c-1]
    num_string = str(frac[0])
    total = sum([int(char) for char in num_string])
    return total



def main():
    n = 100                 # number of terms to generate
    s0 = 2
    convergent = 100

    lst = iterList(n)
    seq = apprSeq(n, s0, lst)

    sum_digits = addDigits(convergent, seq)
    print "ANSWER: " + str(sum_digits)

main()
