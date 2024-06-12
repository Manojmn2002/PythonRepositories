def div(dividend,diviser):
    negative=(dividend<0)^(diviser)
    qt=0
    while dividend>=diviser:
        dividend-=diviser
        qt+=1

    if negative==-1:
        qt=-qt

    return qt


result=div(10,3)
print(result)