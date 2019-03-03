def tree(filename):
    f = open(filename,"r")
    d = dict()
    for line in f:
        for c in line:
            if c == "\n": continue
            if c in d:
                d[c] += 1
                continue
            d[c] = 1
    f.close()
    return sort(d)

def sort(d):
    d1 = dict()
    while d != dict():
        m = ""
        for key, value in d.items():
            if m == "":
                m = [key, value]
                continue
            if type(m[1]) == list:
                if type(value) == list:
                    if m[1][0] > value[0]:
                        m = [key, value]
                    continue
                if m[1][0] > value:
                    m = [key, value]
                continue
            if type(value) == list:
                if m[1] > value[0]:
                    m = [key, value]
                continue
            if m[1] > value:
                m = [key, value]
        d1[m[0]] = m[1]
        del d[m[0]]
    return d1

def pack(d):
    while len(d) > 2:
        key1 = ""
        for key, value in d.items():
            if key1 == "":
                key1 = key
                val1 = value
                continue
            key2 = key
            val2 = value
            break
        del d[key2]
        del d[key1]
        liste = []
        if type(val1) == list:
            if type(val2) == list:
                liste = [val1[0]+val2[0],sort({key1:val1,key2:val2})]
            else:
                liste = [val1[0]+val2,sort({key1:val1,key2:val2})]
        elif type(val2) == list:
            liste = [val1+val2[0],sort({key1:val1,key2:val2})]
        else:
            liste = [val1+val2,sort({key1:val1,key2:val2})]
        d[key1+key2] = liste
        d = sort(d)
    return sort(d)

def chart(d):
    if len(d) != 2:
        return -1
    i = 0
    d1 = dict()
    for key, value in d.items():
        if type(value) == list:
            for key1, value1 in chart(value[1]).items():
                d1[key1]=str(i)+value1
            i+=1
            continue
        d1[key] = str(i)
        i+= 1
    return d1

def zip1(filename):
    d = chart(pack(tree(filename)))
    f = open(filename,"r")
    f1 = open(filename[:-4]+".zip"+filename[-4:],"w")
    for line in f:
        s = ""
        for c in line:
            if c == "\n":
                s += c
                continue
            s += d[c]
        f1.write(s)
    f1.close()
    f.close()
    f = open(filename[:-4]+".key.csv","w")
    for key, value in d.items():
        f.write("\""+value+"\";"+key+"\n")
    f.close()

def uzip(filename):
    f = open(filename[:-8]+".key.csv","r")
    d = dict()
    for line in f:
        n = 0
        for i in line:
            if i == ";":
                break
            n += 1
        l1 = [line[:n], line[n+1:-1]]
        s = ""
        for i in l1[0]:
            if i == "\"":
                continue
            s += i
        l1[0] = s
        d[l1[0]] = l1[1]
    f.close()
    f = open(filename,"r")
    f1 = open(filename[:-8]+".txt","w")
    for line in f:
        s = ""
        for c in line:
            if c == "\n":
                f1.write(c)
                continue
            s += c
            if s in d:
                f1.write(d[s])
                s = ""
    f1.close()
    f.close()

def start():
    f = open("init.txt","r")
    for line in f:
        if line[-1] != "\n": line+= "\n"
        if line[:4] == "zip ":
            zip1(line[4:-1])
        if line[:6] == "unzip ":
            uzip(line[6:-1])
    f.close()

if __name__ == "__main__":
    start()
