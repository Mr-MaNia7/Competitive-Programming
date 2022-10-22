from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                currIdx = stack.pop()
                answer[currIdx] = idx - currIdx
            stack.append(idx)
        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))