#Max Sum Subarray of size K (gfg)
def maxSubarraySum(self, arr, k):
        i=j=lsum=0
        sum = float('-inf')
        
        while(j<len(arr)):
            lsum+=arr[j]
            
            if(j-i+1<k):
                j+=1
            
            elif (j-i+1)==k:
                sum=max(sum,lsum)
                lsum-=arr[i]
                i+=1
                j+=1
                
        return sum
    

# Chocolate Distribution Problem (gfg)
def findMinDiff(self, arr, m):
        arr.sort()

        ans = float('inf')
        for i in range (len(arr) - m + 1):
            diff=arr[i+m-1]-arr[i]
            ans=min(ans,diff)
                
        return ans