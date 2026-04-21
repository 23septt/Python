import sys
enmy = set()
parent = {}
def findd(i) :
    if i not in parent : 
        parent[i]=i
    if parent[i] == i :
        return i
    parent[i] = findd(parent[i])
    return parent[i]

def unionn(i,j) :
    root_i = findd(i)
    root_j = findd(j)
    if(root_i != root_j) :
        parent[root_i]=root_j

for line in sys.stdin:
    parts = line.strip().split()
    if parts[0] == "End" :
        break
    cmd = parts[0]
    if cmd == "Ally" :
        prated = parts[1:]
        for i in range(len(prated)-1) :
            unionn(prated[i],prated[i+1])
    elif cmd == "Enemy" :
        a = parts[1]
        b = parts[2]
        enmy.add((a,b))
    elif cmd == "Table" :
        table = parts[1:]
        ok = True
        for i in range(len(table)) :
            l = findd(table[i])
            r = findd(table[(i+1)%len(table)])
            if (l,r) in enmy :
                ok = False
                break
        if ok :
            print("OK")
        else :
            print("NO")
    
