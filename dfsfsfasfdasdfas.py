def isSevenUp(x) :
    if x%7 == 0 :
        return ("True")
    else :
        return ("False")
    pass
def nextSevenUp(x) :
    if x%7 == 0 :
        return (x)
    else :
        while x%7 !=0 :
            x+=1
        return x
    pass
exec(input().strip())