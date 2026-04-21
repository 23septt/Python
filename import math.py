import math
n = int(input())
temp = []
for i in range(n) :
    temp.append(float(input()))
sum = 0
for i in range(n) :
    sum+=temp[i]
avg = sum/n
sd = 0
for i in range(n) :
    sd += pow(temp[i]-avg,2)
sd /=n
sd = math.sqrt(sd)
print(f"average = {avg} sd = {sd}")


