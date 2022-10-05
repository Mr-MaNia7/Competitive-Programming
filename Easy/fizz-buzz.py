from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0 for i in range(n)]
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                answer[num - 1] = "FizzBuzz"
            elif num % 3 == 0:
                answer[num - 1] = "Fizz"
            elif num % 5 == 0:
                answer[num - 1] = "Buzz"
            else:
                answer[num - 1] = str(num)
        return answer

if __name__ == "__main__":
    soln = Solution()
    print(soln.fizzBuzz(1))