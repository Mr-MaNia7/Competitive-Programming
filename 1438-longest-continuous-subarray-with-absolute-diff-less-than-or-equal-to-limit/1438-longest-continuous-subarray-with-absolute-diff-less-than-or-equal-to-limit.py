class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        min_deque, max_deque = deque(), deque()
        l = r = 0
        for r in range(len(nums)):
            curr = nums[r]
            while min_deque and curr <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and curr >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
            res = max(res, r - l + 1)
        return res