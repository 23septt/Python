dic = {}
n = int(input())
for i in range(n) :
    temp = int(input())
    dic[temp]=dic.get(temp,0)+1
mx = -1
print()
index = []
for i in dic :
    if(dic[i]>mx) :
        mx = dic[i]
        index.clear()
        index.append(i)
    elif(dic[i]==mx) :
        index.append(i)
print(f"Key is {index} and Max Value is {mx}")