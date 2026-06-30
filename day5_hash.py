#mp.begin(); -> first element iterator
#shorthand

# leetcode 128

# subarray with sum 0 (gfgs)
def subArrayExists(self,arr):
        pre_sum=0
        freq={0:-1}
        for i in range(len(arr)):
            num=arr[i]
            pre_sum+=num
            
            if pre_sum in freq:
                return True
                
            freq[pre_sum]=0
        
        return False
    
    
# largest subarray with sum 0 (gfgs)
def maxLength(self, arr):
        pre_sum=0
        max_length = 0
        freq={0:-1}
        for i in range(len(arr)):
            num=arr[i]
            pre_sum+=num
            
            if pre_sum in freq:
                length = i - freq[pre_sum] 
                if length > max_length:
                    max_length = length
            
            else:
                freq[pre_sum]=i
                
        return max_length

# largest subarray with sum k (gfgs)
def longestSubarray(self, arr, k):  
        pre_sum=0
        max_length = 0
        freq={0:-1}
        for i in range(len(arr)):
            pre_sum+=arr[i]
            
            if (pre_sum-k) in freq:
                length = i - freq[pre_sum-k] 
                max_length = max(max_length, length)
            
            if pre_sum not in freq:
                freq[pre_sum]=i
                
        return max_length
    
# largest subarrays of 0s and 1's
def maxLen(self, arr):
        pre_sum=0
        max_length = 0
        freq={0:-1}
        for i in range(len(arr)):
            if arr[i]==0:
                pre_sum+=-1
                
            else:
                pre_sum+=1
            
            if pre_sum in freq:
                length = i - freq[pre_sum] 
                max_length = max(max_length, length)
            
            else:
                freq[pre_sum]=i
                
        return max_length