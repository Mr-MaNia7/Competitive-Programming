from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            print(basket)
        return right - left + 1

if __name__ == "__main__":
    s = Solution()
    print(s.totalFruit([1,2,3,2,2]))
    # print(s.totalFruit([0,1,2,2]))
    # print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
    # print(s.totalFruit([1,2,1]))
    # print(s.totalFruit([3,3,1,1,3]))