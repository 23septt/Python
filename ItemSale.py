item = []
def backtrack(idx,target,bag) :
    if bag == target :
        return 1
    if bag > target or idx >= len(item) :
        return 0
    value , c = item[idx]
    count = 0
    for i in range(c+1) :
        new_bag = bag+value*i
        if new_bag <= target :
            count += backtrack(idx+1,target,new_bag)
        else :
            break
    return count

n , target = input().split()
n , target = int(n) , int(target)

for i in range(n) :
        value , c = input().split()
        value , c = int(value) , int(c)
        item.append((value,c))

if target == 0 :
    print(1)
else :
    print(backtrack(0,target,0))
