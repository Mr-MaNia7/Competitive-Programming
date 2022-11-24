class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        r = k % sum(chalk)
        prefixsum = [0] * (len(chalk) + 1)
        for i in range(len(chalk)):
            prefixsum[i+1] = prefixsum[i] + chalk[i]
            if prefixsum[i+1] > r: return i
        # for i, p in enumerate(prefixsum[1:]):
        #     if p > r:
        #         return i