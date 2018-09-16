import math

def count_routes(side_len):
    return math.factorial(2 * side_len) / (math.factorial(side_len) * math.factorial(side_len))

def main():
    SIDE_LEN = 20
    num_routes = count_routes(SIDE_LEN)
    print ("ANSWER: %d") % num_routes

main()
