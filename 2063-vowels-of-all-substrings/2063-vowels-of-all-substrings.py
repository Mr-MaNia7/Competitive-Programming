class Solution:
    def countVowels(self, word: str) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        n = len(word)
        for i, c in enumerate(word):
            if c in vowel:
                res += (n-i) * (i+1)
        return res
