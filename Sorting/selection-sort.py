#User function Template for python3
class Solution: 
    def select(self, arr, i):
        minIdx = i
        for i in range(i + 1, len(arr)):
            if arr[minIdx] > arr[i]:
                minIdx = i
        return minIdx
    def selectionSort(self, arr,n):
        i = 0
        while i < n:
            selPos = self.select(arr, i)
            arr[selPos], arr[i] = arr[i], arr[selPos]
            i += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends