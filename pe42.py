
def getWords():
    '''
    returns list of words
    '''
    words_file = open('p042_words.txt')
    words = words_file.read()
    words = words.split(",")
    words = [word[1:-1] for word in words]
    words_file.close()
    return words

def alphaPositions():
    '''
    return dictionary for alphabet positions
    '''
    dict = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alpha)):
        dict[alpha[i]] = i+1
    return dict


def countTriNums(words, alpha_dict, tri_nums):
    '''
    count how many words are triangular
    '''
    num_triangles = 0
    for word in words:
        word_value = 0
        for char in word:
            word_value += alpha_dict[char]
        if word_value in tri_nums:
            num_triangles += 1
    return num_triangles



def main():
    N = 1000
    tri_nums = [int(0.5*n*(n+1)) for n in range(1,N)]
    words = getWords()
    alpha_dict = alphaPositions()
    num_triangles = countTriNums(words, alpha_dict, tri_nums)
    print "ANSWER: ", num_triangles

main()
