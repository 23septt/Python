def permu(n,now,num) :
    if len(now) == n :
        for i in now:
            print(i,end="")
        print()
        return
    for i in range(len(num)) :
        if not used[i] :
            used[i] = True
            now.append(num[i])
            permu(n,now,num)
            now.pop()
            used[i] = False
    

inn , n = input().strip().split()
n = int(n)
num = []
for i in inn :
    num.append(i)
used = [False]*len(num)
permu(n,[],num)
    