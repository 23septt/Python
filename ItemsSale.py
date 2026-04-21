item = []
dp = {}
def backtrack(index,target,bag) :
    state = (index,bag)
    if state in dp :
        return dp[state]
    if bag == target :
        return 1
    if index >= len(item) or bag > target :
        return 0
    count = 0
    value , c = item[index]
    for k in range(c+1) :
        new_bag = bag+value*k
        if new_bag <= target :
            count+=backtrack(index+1,target,new_bag)
        else : 
            break
    dp[state] = count
    return count

m , target= input().strip().split()
m , target = int(m) , int(target)
if target == 0 :
    print(1)
else :
    for i in range(m) :
        value , c = input().strip().split()
        value , c = int(value) , int(c)
        if value < 0 :
            continue
        item.append((value,c))
    print(backtrack(0,target,0))