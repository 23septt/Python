n = int(input())
mistake = {}
penalty = {}
done = {}
teamscore ={}
for i in range(n) :
    line = input()
    info = line.strip().split()
    time = info[0]
    team = info[1]
    ex = info[2]
    result = info[3]
    key = (team,ex)
    if done.get(key,0) == 0 :
        if result == "F" :
            mistake[key] = mistake.get(key,0) + 1
        elif result == "T" :
            penalty[team] = penalty.get(team,0) + int(time) + mistake.get(key,0)*20
            done[key] = 1
for key , point in done.items() :
    teamm = key[0]
    exx = key[1]
    if point == 1 :
        teamscore[teamm] = teamscore.get(teamm,0) +1
ans = []
for teammm , scoreee in teamscore.items() :
    ans.append([teammm,scoreee,penalty[teammm]])
ans.sort(key = lambda x :(-x[1] , x[2] , x[0]))
count = 0
ii = 0
while ii < len(ans) :
    t , s , p = ans[ii] 
    ii += 1
    print(f"{t} {s} {p}")
    count += 1
    if count >= 3 :
        break
while ii<len(ans) :
    t , s , p = ans[ii-1]
    nt , ns , np = ans[ii]
    if ns == s and np == p :
        print(f"{nt} {ns} {np}")
        ii+=1
    else :
        break