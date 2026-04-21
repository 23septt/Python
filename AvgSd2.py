n = int(input())
data = []
for i in range(n) :
    data.append(float(input()))
summ = sum(data)
avg = summ/n
sd = 0
for i in range(n) :
    sd+=(data[i]-avg)**2
sd /= n
import math
sd = math.sqrt(sd)
print(f"average = {round(avg,5)} sd = {round(sd,5)}")