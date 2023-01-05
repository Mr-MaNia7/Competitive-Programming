class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        end = anchor = 0
        ans = []
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                ans.append(end-anchor+1)
                anchor = end + 1
        return ans