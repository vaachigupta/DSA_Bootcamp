# Subarrays with equal 1s and 0s (gfg)
def countSubarray(self, arr):
        pre_sum=0
        count = 0
        freq={0:1}
        for num in arr:
            if num==0:
                pre_sum+=-1
                
            else:
                pre_sum+=1
            
            if pre_sum in freq:
                count+=freq[pre_sum]      
            
            freq[pre_sum] = freq.get(pre_sum,0)+1
            
        return count


# valid anagrams (leetcode 242)
def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}

        for i in s:
            freq1[i]=freq1.get(i,0)+1

        for j in t:
            freq2[j]=freq2.get(j,0)+1

        if freq1==freq2:
            return True
        else:
            return False

    
# Group anagrams (leetcode 49)
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups={}
        for word in strs:
            key=''.join(sorted(word))

            if key not in groups:
                groups[key]=[]

            groups[key].append(word)

        return list(groups.values())
  
    
# group shifted strings (gfg)
def groupShiftedString(self, arr):
        groups = {}
        for word in arr:
            key=[]
            for i in range(1, len(word)):
                diff = (ord(word[i]) - ord(word[i-1]) + 26) % 26
                key.append(diff)
            
            key=tuple(key)
            if key not in groups:
                groups[key]=[]
            
            groups[key].append(word)
        return list(groups.values())
    

# leetcode 781
def numRabbits(self, answers: list[int]) -> int:
        freq={}
        for num in answers:
            freq[num]=freq.get(num,0)+1

        total = 0
        for key in freq:
            group_size=key+1
            groups =(freq[key] + group_size-1) // group_size
            total += groups*group_size

        return total