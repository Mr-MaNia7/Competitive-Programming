class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        run_count = 0
        run_max = 0
        for n in nums:
            if seen and n in seen:
                step = run_max - n + 1
                n += step
                run_count += step
            seen.add(n)
            run_max = max(run_max, n)
        return run_count