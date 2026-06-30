# an array with numbers repeating thrice except one number. Find that one number
# leetcode 137

#codeforces new years eve
#max xor sum = max no of 1s in binary. Ex- for n=13 (1101) -> max can only be 15 (1111) no matter how many k
n = 13      #00001101
k = 3
count = 0
while(n!=0):        # to calculate number of bits used to represent the number.
    n=n>>1
    count+=1

print((2**count)-1)     #((2^count)-1) = 15


# Given int number, swap the even and odd bits
# ex: n = 10011001 -> 01100110
n=153
mask1=0x55555555    #01010101
mask2=0xAAAAAAAA    #10101010

even = (n&mask2)
odd = (n&mask1)

even<<=1
odd>>=1

print(odd|even)
