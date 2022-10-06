class Solution:
    def select(self, words, i):
        minIdx = i
        for idx in range(i + 1, len(words)):
            if int(words[idx][-1]) <  int(words[minIdx][-1]):
                minIdx = idx
        return minIdx

    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        i = 0
        while i < len(words):
            selPos = self.select(words, i)
            words[selPos], words[i] = words[i], words[selPos]
            i += 1
        for i in range(len(words)):
            word = words[i]
            word = word.translate(word.maketrans(str(i + 1), " ", ""))
            words[i] = word.rstrip()
        return " ".join(words)

if __name__ == "__main__":
    soln = Solution()
    print(soln.sortSentence("KTFkUVVrmYMSo2 wXlQraUqblfhCfDLK3 IfTuftYVualQ6 NhpQ5 HlRjClVtQrTFcwbx4 fi1"))
