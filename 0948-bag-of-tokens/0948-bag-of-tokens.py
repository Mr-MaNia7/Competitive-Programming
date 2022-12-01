class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        l = 0
        r = len(tokens) - 1
        run = 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                run += 1
                l += 1
            elif run > 0:
                power += tokens[r]
                run -= 1
                r -= 1
            else:
                break
            score = max(score, run)
        return score