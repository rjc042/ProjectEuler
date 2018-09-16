
def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def get_chain_len(start_num):
    chain_len = 1
    while start_num > 1:
        start_num = collatz(start_num)
        chain_len += 1
    return chain_len

def get_max_chain_len(max_start_num):
    max_chain_len = 0
    max_chain_len_num = 0
    for start_num in range(2, max_start_num):
        chain_len = get_chain_len(start_num)
        if chain_len > max_chain_len:
            max_chain_len = chain_len
            max_chain_len_num = start_num
    return max_chain_len_num

def main():
    MAX_START_NUM = int(1e6)
    max_chain_len_num = get_max_chain_len(MAX_START_NUM)
    print ("ANSWER: %d") % max_chain_len_num

main()
