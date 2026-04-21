lost = {}
gain = {}
score = {}
while True :
    line = input().strip()
    if line == "end" :
        break
    part = line.split()
    teamA = part[0]
    scoreA = int(part[1])
    scoreB = int(part[2])
    teamB = part[3]
    gain[teamA] = gain.get(teamA,0) + scoreA
    gain[teamB] = gain.get(teamB,0) + scoreB
    lost[teamA] = lost.get(teamA,0) + scoreB
    lost[teamB] = lost.get(teamB,0) + scoreA
    score[teamA] = score.get(teamA,0)
    score[teamB] = score.get(teamB,0)
    if scoreA > scoreB :
        score[teamA] = score.get(teamA,0) +3
    elif scoreB > scoreA :
        score[teamB] = score.get(teamB,0) +3
    else :
        score[teamA] = score.get(teamA,0) +1
        score[teamB] = score.get(teamB,0) +1
output = []

for team in score :
    output.append([team,score[team],gain[team]-lost[team]])
output.sort(key = lambda x : (-x[1] , -x[2] , -gain[x[0]] ,x[0]))

for i in range(len(output)) :
    t , s , p = output[i]
    print(t,s,p)
