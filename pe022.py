import numpy as np

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


dict = {}
for i in range(len(alp)):
    dict[alp[i]] = i + 1

def score(name):
    total = 0
    for char in name:
        # print "CHAR", char
        total += dict[char]
    return total


f = open('p022_names.txt')
names = f.read()
f.close()

names = names.split(',')
names = [name[1:len(name) - 1] for name in names]
names = np.sort(names)

grand = 0
for i in range(len(names)):
    sc = score(names[i])
    pos = i + 1
    grand += sc*pos

print "ANSWER:", grand
