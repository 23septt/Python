n = int(input())
arr = []
mark=[]
pit = 0
for i in range(n) :
    arr.append(int(input()))
for i in range(1,n-1) :
    if arr[i-1] > arr[i] and arr[i+1] > arr[i] :
        pit += 1
        mark.append(i)
if arr[1] > arr[0] and arr[n-1] > arr[0] :
    pit+=1
    mark.append(0)
if arr[0] > arr[n-1] and arr[n-2] > arr[n-1] :
    pit+=1
    mark.append(n-1)
if pit == 0 :
    print("No pits")
else :
    for a in mark :
        print(a)
