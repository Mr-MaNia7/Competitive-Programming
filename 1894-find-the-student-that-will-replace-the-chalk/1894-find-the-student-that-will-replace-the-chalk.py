class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        r = k % sum(chalk)
        for i, c in enumerate(chalk):
            if c > r:
                return i
            r -= c
