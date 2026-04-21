def solve(idx,cur,num) :
    if cur == target :
        return 1
    if cur > target or idx >= len(num) :
        return 0
    count = 0
    count += solve(idx+1,cur+num[idx],num)
    count += solve(idx+1,cur,num)
    return count


n , target = map(int,input().strip().split())
num = []
for i in range(n) :
    num.append(int(input()))
print(solve(0,0,num))
