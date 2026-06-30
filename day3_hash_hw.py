# number of times m appears in n
'''
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0]*11
for num in n:
    hash_list[num] += 1
    
for num in m:
    if ((num<1) | (num>10)):
        print(0)
        
    else:
        print(hash_list[num])
'''

#frequency maps
'''
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
#b = ['apple','orange']

for item in data:
    freq[item] = freq.get(item, 0) + 1

#for i in b:
#    print(freq.get(i,0))

print(freq) 
'''

#Union of two arrays
'''
arr1 = [1,2,2,3,4]
arr2 = [5,5,2,5,6,1]
freq = {}

for i in arr1:
    freq[i] = freq.get(i,0)+1
    
for j in arr2:
    freq[j] = freq.get(j,0)+1
    
print(list(freq.keys()))   
'''

#Intersection of two arrays
arr1 = [1,2,2,3,4]
arr2 = [5,5,2,5,6,1]
freq = {}
ans = []

for i in arr1:
    freq[i] = freq.get(i,0)+1
    
for j in arr2:
    if freq.get(j,0)>0:
        ans.append(j)
        freq[j] = 0
    
print(ans)  

#winner of an election
#gfg
def winner(self,arr,n):
    freq = {}
    for i in arr:
        freq[i]=freq.get(i,0)+1
            
    max_count = max(freq.values())
    answer=""
        
    for name in freq:
        if freq[name]==max_count:
            if answer=="" or name < answer:
                answer=name
                    
    return [answer,str(max_count)]