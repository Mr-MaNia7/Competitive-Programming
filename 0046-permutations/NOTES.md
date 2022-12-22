It is not clear the recursive part:
```
nums[start], nums[i] = nums[i], nums[start]
backtrack(start+1, end)
nums[start], nums[i] = nums[i], nums[start]
```