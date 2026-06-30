# another way to calculate set bit
# codeforces raising bacteria
# kerningham algorithm
count = 0
n = 15
while (n!=0):
    ''' res = (x & (~x)) 
    n = n - res
    count += 1
    '''
    n = n&(n-1)
    count += 1

print(count)


# n = 00001100 OFF the right most set bit
n = 12
print(n&(n-1))      # n = 00001000

# to check if a number is in the power of 2
# it should only have 1 set bit
n = 14
if (n&(n-1) == 0):
    print("Yes")
else:
    print("No")


# given 2 int numbers and we have to convert a to b and to count the min. numbers of bits flipped in that conversion
a = 10
b = 7 
res = (a^b)
while (res!=0):
    res = res&(res-1)
    count += 1

print(count)