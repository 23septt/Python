n = int(input())
pits = 0
num = []
for i in range(n) :
    num.append(int(input()))
count = 0
mark = []
nothave = True
if num[0] < num[1] and num[0] < num[n-1] :
    mark.append(0)
    nothave = False
for i in range(1,n) :
    if num[i] < num[i-1] and num[i] < num[(i+1)%n] :
        mark.append(i)
        nothave = False
if nothave :
    print("No pits")
else :
    for i in mark :
        print(i)