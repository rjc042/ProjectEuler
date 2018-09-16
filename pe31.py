# DONE #

def get_target(coin_pool, target):
    if len(coin_pool) == 1:
        return [1] * target
    else:
        add_coin = coin_pool[0]
        num_coins = target / add_coin
        add_coins = [add_coin] * num_coins
        new_target = target % add_coin
        return add_coins + get_target(coin_pool[1:], new_target)

def first_not_one_idx(combo):
    reverse_combo = combo[::-1]
    idx_1 = 0
    while reverse_combo[idx_1] == 1:
        idx_1 += 1
    return len(combo) - idx_1 - 1

def get_num_ways(all_coins, target):
    combo = get_target(all_coins, target)
    num_ways = 1
    coin_pool = all_coins
    while len(combo) < target:
        idx_1 = first_not_one_idx(combo)
        not_1 = combo[idx_1]
        idx_not_1 = coin_pool.index(not_1)
        new_target = sum(combo[idx_1:])
        new_coin_pool = coin_pool[idx_not_1 + 1:]
        combo = combo[:idx_1] + get_target(new_coin_pool, new_target)
        num_ways += 1
    return num_ways

def main():
    COINS = [200, 100, 50, 20, 10, 5, 2, 1]
    TARGET = 200
    coin_pool = COINS
    num_ways = get_num_ways(COINS, TARGET)
    print ("ANSWER: %d" % num_ways)

main()
