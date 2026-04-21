bank = {}
while True :
    line = input().strip()
    if line == "End" :
        break
    part = line.split()
    cmd = part[0]
    name = part[1]
    money = int(part[2])
    if cmd == "deposit" :
        bank[name] = bank.get(name,0) + money
    elif cmd == "withdraw" :
        if bank.get(name,0) >= money :
            bank[name] -= money
priority = sorted(bank.items(),key = lambda x : (-x[1] , x[0]))
for n , m in priority :
    print(n,m)