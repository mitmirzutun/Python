def jump_probabilities(hops):
    if hops <= 0: return 0
    h = all_probable_jumps(hops)
    probabilities = dict()
    for i in range(hops):
        i1 = h[i+1]
        probabilities[i+1]=0
        for j in i1:
            curr_pos = 0
            curr_prob = 1/float(hops)
            for k in j:
                curr_pos += k
                if curr_pos == hops: continue
                curr_prob *= 1/float(hops-curr_pos)
            probabilities[i+1]+=curr_prob
    return probabilities

def all_probable_jumps(hops):
    if hops == 1: return {1:[[1]]}
    liste1 = []
    liste2 = []
    d = dict()
    for i in range(hops):
        liste2.append([i+1])
    while liste2 != []:
        for i in liste2:
            if sum(i) == hops:
                if len(i) not in d:
                    d[len(i)] = [i]
                    continue
                d[len(i)].append(i)
            else: liste1.append(i)
        liste2 = []
        for i in liste1:
            for j in range(hops-sum(i)):
                i1 = i[:]
                i1.append(j+1)
                liste2.append(i1)
        liste1 = []
    return d

def e_wert(hops):
    l1 = all_probable_jumps(hops)
    l2 = jump_probabilities(hops)
    s = 0
    for i in range(hops):
        s += l2[i+1]*(i+1)
    return s
