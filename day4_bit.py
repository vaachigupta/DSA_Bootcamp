# 7 soldiers named from 1-7 standing in a circular manner. king stands at 1st position and kills alternatee soldiers in clockwise direction
# at last only one soldier is left. so at what position should we keep the soldier so that he is safe
n = 10
power=1
while power*2<=n:
    power*=2

safe = 2*(n-power)+1
print(safe)

#given two numbers A=10101010101, B=10010011001 o/p = 10011011101
x=1365
y=1177
l=2
r=6
m=1
m<<=(r-l+1)  #3 times shift (00010000)
m=m-1
m<<=l
mask=x&m
print(mask|y)
