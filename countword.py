count = {}
while True :
    line = input().strip()
    if line == "End" :
        break
    part = line.split()
    for word in part :
        count[word] = count.get(word, 0) + 1
n = int(input())
count = sorted(count.items() ,key = lambda x : (-x[1] , x[0]))
for i in range(n) :
    word , c = count[i]
    print(f"{word} : {c}")

