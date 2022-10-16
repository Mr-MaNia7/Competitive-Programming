class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        dic = {}
        longest = 0
        while right < len(s):
            if s[right] in dic:
                left = max(left, dic[s[right]]+1)
            longest = max(longest, right - left + 1)
            dic[s[right]] = right
            right += 1
        return longest
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
