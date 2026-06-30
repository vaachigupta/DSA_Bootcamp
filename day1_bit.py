''' n = 24
i = 5
bit = 1

#mask
mask = n | (bit<<5)   #OR
print(mask)

print(n ^ mask)   #Toggle

print(n & (~ mask))
'''

#To check if a given bit is ON or OFF
# n = 01110100
'''
n = 116
i = 2
if (n&(1<<i)):
    print('ON')

else:
    print('OFF')
'''

#to calculate the right most set bit mass -> ex- 110110 = 000010
# n = 24 0s - 01101100 -> 00000100
'''
n = 108
mask = (~n + 1)  # 2's complement
print(n&mask)

# to calculate number of set bits in the number (no. of 1s in the number)
res = 0

for i in range(32):             # while (n!=0):n&(n-1) count += 1
    if (n>>i) & 1:
        res += 1

print(res)
'''


