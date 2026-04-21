dayy = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
monthh = [31,28,31,30,31,30,31,31,30,31,30,31]
first_day=int(input())
m = int(input())
tab = first_day
for i in range(m-1) :
    tab+=monthh[i]
tab=tab%7
for i in range(tab) :
    print("\t",end="")
for i in range(monthh[m-1]) :
    if (i+tab)%7==0 and not i+tab == 0 : print()
    print(i+1,end="\t")
print()