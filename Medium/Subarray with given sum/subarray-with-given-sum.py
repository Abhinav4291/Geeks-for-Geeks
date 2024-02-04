#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        if((s == 0) and s in arr):
            return [arr.index(0)+1,arr.index(0)+1]

        if(sum(arr) == s):
            return [1,n]
        
        k = 0
        sum_c = 0           
        for i in range(n): 
            sum_c += arr[i]
            # print(sum_c)
            while(sum_c > s and i > k):
                sum_c = sum_c - arr[k]
                k += 1
            if(sum_c == s):
                return [k+1,i+1]
        return [-1]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends