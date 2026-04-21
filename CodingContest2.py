n = int(input())
mistake = {}
done = {}
penalty = {}
count = {}
for i in range(n) :
    line = input().strip()
    part = line.split()
    time = int(part[0])
    team = part[1]
    question = part[2]
    result = part[3]
    key = (team,question)
    if done.get(key,False) == False :
        if result == "F" :
            mistake[key] = mistake.get(key,0) +1
        elif result == "T" :
            penalty[team] = penalty.get(team,0) + time + mistake.get(key,0)*20
            done[key] = True
            count[team] = count.get(team,0) +1
output = []
for teamm in count :
    output.append((teamm,count[teamm],penalty[teamm]))
output.sort(key = lambda x : (-x[1] , x[2] , x[0]))

i = 0
while i < len(output) :
    if i == 3 :
        break
    t , s , p = output[i]
    print(t,s,p) 
    i += 1
while i < len(output) :
    nt , ns , np = output[i]
    if ns == s and np == p :
        print(nt,ns,np)
        t , s , p  = nt , ns , np
        i+=1
    else :
        break


    
