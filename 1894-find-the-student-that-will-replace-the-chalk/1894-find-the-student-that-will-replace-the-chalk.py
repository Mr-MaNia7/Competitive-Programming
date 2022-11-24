class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        r = k % sum(chalk)
        # if r == 0:
        #     return 0
        # else:
        prefixsum = [0] * (len(chalk) + 1)
        for i in range(len(chalk)):
            prefixsum[i+1] = prefixsum[i] + chalk[i]
        for i, p in enumerate(prefixsum[1:]):
            if p > r:
                return i