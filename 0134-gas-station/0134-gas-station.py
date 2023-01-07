class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return -1 if sum(gas) - sum(cost) < 0 else start