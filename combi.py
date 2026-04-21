now = []
def combi(idx,now,num) :
    if len(now) == n :
        for i in now :
            print(i,end="")
        print()
        return
    if idx >= len(num) :
        return
    now.append(num[idx])
    combi(idx+1,now,num)
    now.pop()
    combi(idx+1,now,num)
    
inn , n = input().strip().split()
n = int(n)
num = []
for i in inn :
    num.append(i)
combi(0,now,num)

