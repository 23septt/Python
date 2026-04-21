import math
n = int(input())
num = []
for i in range(n) :
    num.append(float(input()))
avg = sum(num)/n
sd = 0
for i in range(n) :
    sd+=(num[i]-avg)**2
sd /= n
sd = math.sqrt(sd)
print("average =",round(avg,5),"sd =",round(sd,5))
