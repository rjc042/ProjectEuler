
terms = []
for a in range(2,101):
    for b in range(2,101):
        terms.append(a**b)

terms = list(set(terms))
print "ANSWER:", len(terms)
