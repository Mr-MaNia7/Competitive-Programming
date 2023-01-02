class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = False
        small = False
        for i, c in enumerate(word):
            if i > 0 and 65 <= ord(c) <= 90:
                capital = True
            elif 97 <= ord(c) <= 122:
                small = True
        return False if capital and small else True