import sys
parent = {}
enmy = set()

def findd(i) :
    if i not in parent :
        parent[i] = i
    if parent[i] == i :
        return i
    parent[i] = findd(parent[i])
    return parent[i]
def unionn(i,j) :
    root_i = findd(i)
    root_j = findd(j)
    if root_i != root_j :
        parent[root_i] = root_j

for line in sys.stdin :
    part = line.strip().split()
    if part[0] == "End" :
        break
    cmd = part[0] 
    if cmd == "Ally" :
        country = part[1:]
        for i in range(len(country)-1) :
            unionn(country[i],country[i+1])
    elif cmd == "Enemy" :
        a = part[1]
        b = part[2]
        enmy.add((a,b))
    elif cmd == "Table" :
        ok = True
        table = part[1:]
        for i in range(len(table)-1) :
            x = findd(table[i])
            y = findd(table[(i+1)%len(table)])
            if (x,y) in enmy :
                ok = False
                break
        if ok :
            print("OK")
        else :
            print("NO")