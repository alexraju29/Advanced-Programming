#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # code here
        i = 0
        while i < len(arr):
            if i+1 == arr[i]:
                i+=1
            else:
                return (i+1)
        return i+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
n = 8
arr = [1,3,4,5,6,7,8]
s = Solution().missingNumber(n, arr)
print(s)

# } Driver Code Ends