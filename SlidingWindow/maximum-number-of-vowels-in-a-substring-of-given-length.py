class Solution:
     def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in vowels: # Time Complexity = O(1)
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans = max(cnt, ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels("abciiidef", 3))