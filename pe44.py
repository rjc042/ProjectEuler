
def pentNums(N):
    '''
    returns list of first N pentagonal numbers
    '''
    return [n*(3*n-1)/2 for n in range(1,N+1)]


def minD(pent_nums):
    '''
    Find first satisfactory case
    '''
    k = 1
    while True:
        pk = pent_nums[k-1]
        j = 1
        while j <= k:
            pj = pent_nums[j-1]
            if pk + pj in pent_nums and pk - pj in pent_nums:
                return pk - pj
            j += 1
        k += 1


def main():
    N = 1e4
    pent_nums = pentNums(int(N))
    D = minD(pent_nums)
    print "ANSWER: ", D

main()
